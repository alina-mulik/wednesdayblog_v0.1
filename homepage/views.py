from django.conf import settings
from django.shortcuts import render, redirect

from blogpage.urls import urlpatterns
from .models import Event, Like
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.models import User
import random
from django.conf.urls.static import static


def home(request):
    events = Event.objects.all()
    print(events.first().post_image.url, 222222222222222222)
    user = request.user
    return render(request, "homepage/home.html", {'events': events, 'user': user,
                                                  'static_files': ["Addams-Family.jpg", "poison.png",
                                                                   "romantic.jpg"], })


def error404(request, exception):
    page = render(request, 'homepage/404.html')
    return HttpResponseNotFound(page)


def like_event(request):
    user = request.user
    if request.method == "POST":
        event_id = request.POST.get('event_id')
        event_obj = Event.objects.get(id=event_id)
        if request.user.is_anonymous:
            anonuser = User.objects.create_user(username="anon" + str(random.randint(1, 100000000000000)), email="none",
                                                first_name="none", last_name="none")
            user = anonuser
            user.save()

        if user in event_obj.liked.all():
            event_obj.liked.remove(user)
        else:
            event_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, event_id=event_id)

        if not created:
            if like.value == "Like":
                like.value == "Unlike"
            else:
                like.value == "Like"
        like.save()
    return redirect("home")
