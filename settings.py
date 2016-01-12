import os

class Common:
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    CONFIG_DIR = os.path.join(APP_ROOT, 'config')
    STATIC_DIR = 'static'
    GALLERY_DIR = 'img/gallery'
    GALLERY_DIR_ABSOLUTE = os.path.join(APP_ROOT, STATIC_DIR, GALLERY_DIR)
    STRIPE_KEYS = {
        'secret': os.environ['STRIPE_SECRET'],
        'publishable': os.environ['STRIPE_PUBLISHABLE']
    }
