import subprocess
from os.path import exists

from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Lint Code with pycodestyle'

    def get_modules(self):
        app_labels = [app.label for app in apps.app_configs.values()]
        self_modules = [app for app in app_labels if exists(app)]
        print(app_labels)
        print(self_modules)
        return self_modules

    def handle(self, *args, **options):
        modules = self.get_modules()
        print(modules)
        self.stdout.write('module list: {}'.format(modules))
        self.stdout.write('start pycode lint')

        for module in modules:
            subprocess.call(['pycodestyle', module])
