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
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ['SENDGRID_USER']
    MAIL_PASSWORD = os.environ['SENDGRID_PASSWORD']
    MAIL_RECIPIENTS = ["ass51@case.edu"]
