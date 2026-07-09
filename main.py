import scrapy
from scrapy.crawler import CrawlerProcess


class BooksSpider(scrapy.Spider):
    name = "books"

    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):
        titles = response.css("h3 a::attr(title)").getall()

        for title in titles:
            print(title)


process = CrawlerProcess(settings={
    "LOG_ENABLED": False
})
process.crawl(BooksSpider)
process.start()