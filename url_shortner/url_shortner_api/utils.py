import shortuuid
from .models import URL

def create_shortcode():
    shortcode = shortuuid.uuid()

    shortcode_exists = URL.objects.filter(shortcode=shortcode)

    if shortcode_exists:
        return create_shortcode()
    else:
        return shortcode
    