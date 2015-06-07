import datetime

from django.shortcuts import render, get_object_or_404
from django.utils.timezone import utc
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from stories.models import Story
from stories.forms import StoryForm

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
    if request.user.is_authenticated():
        liked_stories = request.user.liked_stories.filter(id__in=[story.id for story in stories])
    else:
        liked_stories = []
    return render(request, 'stories/index.html', {'stories': stories, 'user' : request.user, 'liked_stories' : liked_stories}) 

@login_required    
def story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST) 
        if form.is_valid():
            story = form.save(commit=False)
            story.moderator = request.user
            story.save()
            return HttpResponseRedirect('/')
    else:
        form = StoryForm() 
    return render(request, 'stories/story.html', {'form': form})        


@login_required
def vote(request):
    story = get_object_or_404(Story, pk=request.POST.get('story'))
    story.points += 1
    story.save()
    user = request.user
    user.liked_stories.add(story)
    user.save()
    return HttpResponse()
