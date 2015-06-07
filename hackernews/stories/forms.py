from django.forms import ModelForm

from stories.models import Story

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = '__all__'
        exclude = ('points', 'moderator', 'voters')
