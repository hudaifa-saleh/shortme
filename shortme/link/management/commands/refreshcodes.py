from django.core.management.base import BaseCommand
from shortme.link.models import ShortMe


class Command(BaseCommand):
    help = f"Refresh all {ShortMe} shortcodes"

    def add_arguments(self, parser):
        parser.add_argument("--items", nargs="+", type=int)

    def handle(self, *args, **options):
        return ShortMe.objects.refresh_shortcodes(items=options['items'])
