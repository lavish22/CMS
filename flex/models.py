from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.fields import StreamField
from streams import blocks
# Create your models here.

class FlexPage(Page):
    ''' 
    Flexible page class.
    '''

    template  = "flex/flex_page.html"
    subpage_types = ['flex.FlexPage', 'contact.ContactPage']        #this will prevent anyone from 
    parent_page_types = [                                           #creating any page, anywhere
        'flex.FlexPage',                                            #kind of force page structure, hirarchy
        'home.HomePage',
    ]

    content =  StreamField (
        [
            ("title_and_text",blocks.TitleAndTextBlock()),
            ("full_richtext",blocks.RichTextBlock()),
            ("simple_richtext",blocks.SimpleTextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta",blocks.CTAblock()),
            ("button", blocks.ButtonBlock()),
        ],
        null = True,
        blank = True 
    )

    subtitle = models.CharField(max_length = 100,blank=True,null=True ) 

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"

