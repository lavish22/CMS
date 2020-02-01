'''
StreamField live in here
'''

from wagtail.core import blocks
from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    '''
    Title and Text and nothing else
    '''

    title = blocks.CharBlock(required=True, help_text="add your text in here")
    text = blocks.TextBlock(required=True, help_text="add additional text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"

class RichTextBlock(blocks.RichTextBlock):
    '''
    Rich text with all the features
    '''
    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"

class CardBlock(blocks.StructBlock):
    '''
    Card with and image,text,buttons and link.
    '''
    title = blocks.CharBlock(required=True, help_text="add your text in here")
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True,max_length=40)),
                ("text", blocks.TextBlock(required=True,max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False,help_text="if the button page is selected. that will be used first.")),

            ]
        )
    )
    class Meta:                     #noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff cards"

class SimpleTextBlock(blocks.RichTextBlock):
    '''
    Simple text with limited the features
    '''

    def __init__(self,required=True,help_text=None,editer='default',features=None, **kwargs):
        super().__init__(**kwargs)
        self.features =[
            "bold",
            "italic",
            "link",
        ]

    class Meta:
        template = "streams/simple_richtext_block.html"
        icon = "edit"
        label = "Simple RichText"

class CTAblock(blocks.StructBlock):
    '''
    A simple call to action section
    '''

    title = blocks.CharBlock(required=True,max_length=60)
    text = blocks.RichTextBlock(required=True,Features=["bold","italic","link"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=150)

    class Meta:     #noqa
        template = "streams/cta_block.html"            
        icon = "placeholder"
        label = "Call to Action"

