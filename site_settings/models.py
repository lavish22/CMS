from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting,register_setting

# Create your models here.

@register_setting
class SocialMediaSettings(BaseSetting):
    '''
    Social media setting for our custom website
    '''

    Linkedin = models.URLField(blank=True, null=True, help_text="Linkedin Social Media URL") 
    Twitter = models.URLField(blank=True, null=True, help_text="Twitter Social Media URL") 
    Instagram = models.URLField(blank=True, null=True, help_text="Instagram Media URL") 

    panels = [
        MultiFieldPanel([
            FieldPanel("Linkedin"),               
            FieldPanel("Twitter"),               
            FieldPanel("Instagram"),               
        ], heading = "Social Media Settings")
    ]

