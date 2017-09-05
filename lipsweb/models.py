from cms.models.pluginmodel import CMSPlugin

from django.db import models


class Submission(CMSPlugin):
    content = models.TextField(default='')
    upvoteCount = models.PositiveIntegerField(default=0)
    
class AboutLips(CMSPlugin):
    text = models.TextField(default='')
