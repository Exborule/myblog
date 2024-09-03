# blog/tasks.py
from celery import shared_task
from .nhl_scraper import scrape_nhl

@shared_task
def run_nhl_scraper():
    scrape_nhl()
    return "Scraping completed"