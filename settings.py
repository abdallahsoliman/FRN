import os

class Common:
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    CONFIG_DIR = os.path.join(APP_ROOT, 'config')