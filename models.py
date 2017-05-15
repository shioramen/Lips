from cms.models.pluginmodel import CMSPlugin

from django.db import models


class Submission(CMSPlugin):
    content = models.TextField(default='')
