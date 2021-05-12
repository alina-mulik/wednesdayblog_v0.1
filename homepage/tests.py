
from homepage.models import Event, Like
from django.contrib.auth.models import User

from django.test import TestCase


class SimpleTest(TestCase):
    def setUp(self):
        user_1 = User.objects.create_user(username="Test", email="someemail@gmail.com", password="12345")
        user_2 = User.objects.create_user(username="Tes2", email="someemai2@gmail.com", password="132345")
        event_1 = Event.objects.create(post_text="Mortisha is here", author=user_1)
        event_2 = Event.objects.create(post_text="Preparing a poison", author=user_2)
        Like.objects.create(user=user_1, event=event_1, value='Like')
        Like.objects.create(user=user_2, event=event_2, value='Like')

    def test_text_is_in_the_event(self):  # all methods in the class must be named with test
        """Text is identified in th event"""
        mortisha = Event.objects.get(post_text="Mortisha is here")
        poison = Event.objects.get(post_text="Preparing a poison")
        self.assertEqual(mortisha.post_text, "Mortisha is here")
        self.assertEqual(poison.post_text, "Preparing a poison")

    def test_details(self):
        response = self.client.get('/liked/')
        self.assertRedirects(response, response.url, status_code=302, target_status_code=200)
