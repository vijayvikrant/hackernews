from rest_framework import viewsets, serializers
from stories.models import Story

class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ('title', 'url', 'moderator', 'createdat', 'updatedat')

class StoryViewSet(viewsets.ModelViewSet):
    model = Story
    queryset = Story.objects.all()
    serializer_class = StorySerializer


