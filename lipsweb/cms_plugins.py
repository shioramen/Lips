from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import Submission


class SubmissionPlugin(CMSPluginBase):
    model = Submission
    render_template = "submission_plugin.html"
    cache = False
    name = _("Lips Submission!")

    def render(self, context, instance, placeholder):
        context = super(SubmissionPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(SubmissionPlugin)
