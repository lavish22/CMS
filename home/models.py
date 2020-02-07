from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel,StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import RichTextField,StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from streams import blocks

class HomePageCarouselImages(Orderable):
    '''
    between 1 and 5 images for home page carousel
    '''

    page = ParentalKey("home.HomePage", related_name = "carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    panels = [
        ImageChooserPanel("carousel_image")
    ]

class HomePage(Page):
    '''
    Home page title
    '''
    #max_count = 1 
    templates = "home/home_page.html"
    banner_title = models.CharField(max_length = 100,blank=False,null=True )
    banner_subtitle = RichTextField(features=["bold","italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
                PageChooserPanel("banner_cta"),
            ], heading = "Banner Options"
        ),
        StreamFieldPanel("content"),
        MultiFieldPanel(
            [
                InlinePanel("carousel_images", max_num=5, min_num=1, label="Image"),        
            ], heading = "Carousel Images"
        )
    ]

    content =  StreamField (
        [
            ("cta",blocks.CTAblock()),
        ],
        null = True,
        blank = True 
    )

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

