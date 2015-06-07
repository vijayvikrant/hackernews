import datetime

from django.shortcuts import render
from django.http import HttpResponse
from stories.models import Story
from django.utils.timezone import utc

# Create your views here.

def score(story, gravity=1.8, timebase=120):
    points = (story.points - 1)**0.8
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    age = int((now - story.createdat).total_seconds())/60
    return points/(age+timebase)**gravity

def top_stories(top=180, consider=1000):
    latest_stories = Story.objects.all().order_by('-createdat')[:consider]
    rank_stories = sorted([(score(story), story) for story in latest_stories], reverse=True)
    return [story for _, story in rank_stories][:top]

def index(request):
    stories = top_stories(top=30)
    response = '''
    <html>
    <head>
        <title>News..</title>
    </head>
    <body>
        <ol>
        %s
        </ol>
    </body>
    </html>
    ''' % '\n'.join(['<li>%s</li>' % story.title for story in stories])
    return HttpResponse(response)
    
