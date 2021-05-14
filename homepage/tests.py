from datetime import datetime
from mock import patch
import requests

from blogpage.models import BlogPost
from homepage.models import Event, Like
from django.contrib.auth.models import User
from homepage.views import like_event

from django.test import TestCase


# from rest_framework.test import APITestCase


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

    def test_redirect(self):
        response = self.client.get('/liked/')
        self.assertRedirects(response, response.url, status_code=302, target_status_code=200)

    # def test_like(self):
    #     like = Like.objects.get(value="Like")
    #     user_1 = User.objects.get(username="Tes2")
    #     like_event(user_1)
    #     if




class BlogTestCase(TestCase):
    now = datetime.now()

    def setUp(self):
        BlogPost.objects.create(title="One day in the woods", date=self.now,
                                text="It was a shiny and warm day, when i've decided to go to the woods")

    def test_blog_title(self):
        get_blog_post_title = BlogPost.objects.get(title="One day in the woods")
        self.assertEqual(get_blog_post_title.title, "One day in the woods")

    def test_blog_content(self):
        get_blog_post_text = BlogPost.objects.get(
            text="It was a shiny and warm day, when i've decided to go to the woods")
        self.assertEqual(get_blog_post_text.text, "It was a shiny and warm day, when i've decided to go to the woods")

    def test_date(self):
        get_blog_post_date = BlogPost.objects.get(date=self.now)
        post_date = get_blog_post_date.date
        convert_date_into_str = post_date.strftime("%d-%b-%Y (%H:%M:%S)")
        convert_date_into_str_2 = self.now.strftime("%d-%b-%Y (%H:%M:%S)")
        self.assertEqual(convert_date_into_str, convert_date_into_str_2)

    def check_status(url):
        r = requests.get(url)
        if r.status_code == 200:
            return True

        elif r.status_code == 404:
            return False

    def test_status_code(self):
        with patch('requests.get') as mock_request:
            url = self.client.get('posts/')
            mock_request.return_value.status_code = 200
            self.assertTrue(BlogTestCase.check_status(url))
