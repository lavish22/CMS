from django.db import models
from django import forms
from captcha.fields import ReCaptchaField


from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtail.contrib.forms.views import SubmissionsListView


class FormField(AbstractFormField):
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )

class CustomSubmissionsListView(SubmissionsListView):
    paginate_by = 50  # show more submissions per page, default is 20
    ordering = ('submit_time',)  # order submissions by oldest first, normally newest first
    ordering_csv = ('-submit_time',)  # order csv export by newest first, normally oldest first

    # override the method to generate csv filename
    def get_csv_filename(self):
        """ Returns the filename for CSV file with page slug at start"""
        filename = super().get_csv_filename()
        return self.form_page.slug + '-' + filename


class ContactPage(WagtailCaptchaEmailForm):

    template = "contact/contact_page.html"

    subpage_types = []
    parent_page_types = ['home.HomePage','wagtailcore.Page']       #this is to force page structure hirarchy

    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "contact/contact_page_landing.html"

    # set custom view class as class attribute
    submissions_list_view_class = CustomSubmissionsListView

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]