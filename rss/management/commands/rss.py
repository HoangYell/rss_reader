from django.core.management.base import BaseCommand
from rss.services import RssService


class Command(BaseCommand):
    help = 'Scrawl RSS info from urls'

    def add_arguments(self, parser):
        parser.add_argument(
            '--scrawl',
            help='Scrawl data from urls',
        )

    def handle(self, *args, **options):
        try:
            list_url = set(options.get('scrawl').split(','))
            for url in list_url:
                RssService.scrawl_service(url)
                self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % url))
        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Error while running command "%s"' % e))