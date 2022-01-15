from django import template

from ..models import SlideShow

register = template.Library()


@register.inclusion_tag('slideshow/partial/slideshow.html')
def slideshow():
    return {
        'slideshow': SlideShow.objects.filter(status=True, article__status=True)
    }
