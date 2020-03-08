from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel,StreamFieldPanel, InlinePanel, MultiFieldPanel, ObjectList, TabbedInterface
from wagtail.core.fields import RichTextField,StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.api import APIField

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

    api_fields = [
        APIField("carousel_image"),
    ]

class HomePage(RoutablePageMixin, Page):
    '''
    Home page title, for APIv2 you can also GET specific keys only by extending search_fields here. Usefull in Single Page Applications
    '''
    #max_count = 1 
    subpage_types = [
        'blog.BlogListingPage',
        'contact.ContactPage',
        'flex.FlexPage',
    ]
    parent_page_type = [
        'wagtailcore.Page'
    ]
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
        StreamFieldPanel("content"),
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=5, min_num=1, label="Image")],
            heading="Carousel Images",
            help_text="45 : 16"
        ),
    ]

    banner_panels=[
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
                PageChooserPanel("banner_cta"),
            ], heading = "Banner Options"
        ),
    ]

    # This is how you'd normally hide promote and settings tabs
    # promote_panels = []
    # settings_panels = []

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading='Content'),
            ObjectList(banner_panels, heading="Banner Settings"),
            ObjectList(Page.promote_panels, heading='Promotional Stuff'),
            ObjectList(Page.settings_panels, heading='Settings Stuff'),
        ]
    )

    content = StreamField([
        ("cta", blocks.CTAblock()),
        ("simple_richtext",blocks.RichTextBlock()),
        ("title_and_text_block",blocks.TitleAndTextBlock()),
    ], null=True, blank=True)

    api_fields = [
        APIField("banner_title"),
        APIField("banner_subtitle"),
        APIField("banner_image"),
        APIField("banner_cta"),
        APIField("carousel_images"),
        APIField("content"),
    ]

    @route(r'^subscribe/$')
    def the_subscribe_page(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        return render(request, "home/subscribe.html", context)

    # # Here we are removing the help text. But to change it, simply change None to a string.
    # HomePage._meta.get_field("title").help_text = None
    
    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

