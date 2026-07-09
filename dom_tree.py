import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup


class StructureSpider(scrapy.Spider):
    name = "structure"

    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):

        soup = BeautifulSoup(response.text, "html.parser")

        body = soup.body

        for tag in body.find_all(recursive=False):
            print(tag.name)


process = CrawlerProcess(settings={
    "LOG_ENABLED": False
})

process.crawl(StructureSpider)
process.start()