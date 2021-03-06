"""Flask configuration class."""
import os


class Config:
    """Base configuration variables."""
    def __init__(self):
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.KEY = os.environ.get('KEY')
        self.TOKEN = os.environ.get('TOKEN')
        self.LIST_ID = os.environ.get('LIST_ID')
        self.DONE_LIST_ID = os.environ.get('DONE_LIST_ID')
        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application. Did you forget to run setup.sh?")
