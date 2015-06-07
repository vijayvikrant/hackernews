from django.db import models
from django.contrib.auth.models import User
from urlparse import urlparse
# Create your models here.

class Story(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField()
	points = models.IntegerField(default=1)
	moderator = models.ForeignKey(User, related_name='moderated_stories') 
        voters = models.ManyToManyField(User, related_name='liked_stories')
	createdat = models.DateTimeField(auto_now_add=True)
	updatedat = models.DateTimeField(auto_now=True)

	@property
	def domain(self):
	    return urlparse(self.url).netloc


        def __unicode__(self):
            return self.title

        class Meta:
            verbose_name_plural = "stories"
