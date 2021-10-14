from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from authentication.models import User

from events.models import Event, Organizer


# Create your tests here.
class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(
            name="Tomorrowland",
            start_date="2021-09-01T00:00",
            end_date="2021-09-02T00:00",
        )
        Event.objects.create(
            name="Dance Party",
            start_date="2021-09-01T00:00",
            end_date="2021-09-02T00:00",
        )

        self.normal_user = User.objects.create(
            email="normal_user@abc.com",
            password="normal_user",
            firstname="normal_user",
            lastname="normal_user",
        )
        self.superuser = User.objects.create(
            email="superuser@abc.com",
            password="superuser",
            firstname="superuser",
            lastname="superuser",
            is_superuser=True,
        )

    def test_existing_events(self):
        try:
            Event.objects.get(name="Tomorrowland")
            Event.objects.get(name="Dance Party")
        except Event.ObjectDoesNotExist:
            self.fail("One of the event didn't get created as expected")

    def test_permissions(self):
        token, _ = Token.objects.get_or_create(user=self.normal_user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        request = client.post(
            "/events/",
            {
                "name": "sample",
                "start_date": "2021-09-01T00:00",
                "end_date": "2021-09-02T23:00",
            },
            format="json",
        )
        self.assertEqual(request.status_code, 403)
        self.assertEqual(Event.objects.count(), 2)

    def test_event_creation(self):
        token, _ = Token.objects.get_or_create(user=self.superuser)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        request = client.post(
            "/events/",
            {
                "name": "sample",
                "start_date": "2021-09-01T00:00",
                "end_date": "2021-09-02T23:00",
            },
            format="json",
        )
        self.assertEqual(request.status_code, 201)
        self.assertEqual(Event.objects.count(), 3)


class OrganizersTestCase(TestCase):
    def setUp(self):
        event = Event.objects.create(
            name="Tomorrowland",
            start_date="2021-09-01T00:00",
            end_date="2021-09-02T00:00",
        )
        self.event_id = event.id

        self.normal_user = User.objects.create(
            email="normal_user@abc.com",
            password="normal_user",
            firstname="normal_user",
            lastname="normal_user",
        )
        Organizer.objects.create(
            event=event,
            user=self.normal_user,
        )
        self.superuser = User.objects.create(
            email="superuser@abc.com",
            password="superuser",
            firstname="superuser",
            lastname="superuser",
            is_superuser=True,
        )

    def test_existing_organizers(self):
        try:
            Organizer.objects.get(user=self.normal_user)
        except Event.ObjectDoesNotExist:
            self.fail("One of the organizer didn't get created as expected")

    def test_permissions(self):
        token, _ = Token.objects.get_or_create(user=self.normal_user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        request = client.post(
            "/organizers/",
            {"event": self.event_id, "user": self.superuser.id},
            format="json",
        )
        self.assertEqual(request.status_code, 403)
        self.assertEqual(Organizer.objects.count(), 1)

    def test_organizer_creation(self):
        token, _ = Token.objects.get_or_create(user=self.superuser)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        request = client.post(
            "/organizers/",
            {"event": self.event_id, "user": self.superuser.id},
            format="json",
        )
        self.assertEqual(request.status_code, 201)
        self.assertEqual(Organizer.objects.count(), 2)
