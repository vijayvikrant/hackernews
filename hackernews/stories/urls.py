from django.conf.urls import include, url
from rest_framework import routers
from stories.serializer import StoryViewSet



router =routers.DefaultRouter()
router.register(r'api', StoryViewSet)

urlpatterns = [
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name' : 'auth/login.html'}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/'}, name="logout"),
    url(r'^story/$', 'stories.views.story', name="story"),
    url(r'^vote/$', 'stories.views.vote', name="vote"),
    url(r'^$', 'stories.views.index', name="index"),
    url(r'^', include(router.urls)),
]
