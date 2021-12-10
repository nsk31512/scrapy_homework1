from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from booksparser import settings
from booksparser.spiders.labirintru import LabirintruSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    prcess = CrawlerProcess(settings=crawler_settings)
    prcess.crawl(LabirintruSpider)
    prcess.start()