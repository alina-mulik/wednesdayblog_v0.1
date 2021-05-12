import mock
from django.core.files import File

from homepage.models import Event, Like
from django.contrib.auth.models import User

from django.test import TestCase


# Create your tests here.


class SimpleTest(TestCase):
    def setUp(self):
        file_mock = mock.MagicMock(spec=File)
        user_1 = User.objects.create_user(username="Test", email="someemail@gmail.com", password="12345")
        event_1 = Event.objects.create(post_image=file_mock, post_text="Mortisha is here")
        event_2 = Event.objects.create(post_text="Preparinga a poison")
        Like.objects.create(user=user_1, event=event_1, value='Like')

    def text_is_in_the_event(self):
        """Text is identified in th event"""
        mortisha = Event.objects.get(post_text="Mortisha is here")
        poison = Event.objects.get(post_texte="Preparing a poison")
        self.assertContains(self, mortisha, "Mortisha is here")
        self.assertContains(self, poison, "Preparinga a poison")

    # def test_details(self):
    #     response = self.client.get('/liked/')
    #     print(response)
    #     self.assertRedirects(response, response.url, status_code=302, target_status_code=200)
