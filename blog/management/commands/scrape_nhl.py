from django.core.management.base import BaseCommand
from blog.nhl_scraper import scrape_nhl

class Command(BaseCommand):
    help = 'Scrape NHL player stats from NHL.com'

    def handle(self, *args, **kwargs):
        scrape_nhl()
        self.stdout.write(self.style.SUCCESS('Successfully scraped NHL player stats'))
