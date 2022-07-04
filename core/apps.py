from django.apps import AppConfig
from dotenv import load_dotenv

from ethereum.scripts.utils import load_project


class CoreAppConfig(AppConfig):
    name = 'core'

    def ready(self):
        print("Load Configurations....")
        load_dotenv()
        load_project()
