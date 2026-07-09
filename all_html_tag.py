import scrapy
from scrapy.crawler import CrawlerProcess


class BooksSpider(scrapy.Spider):
    name = "books"

    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):
        with open("page.html", "wb") as f:
            f.write(response.body)

        print("Đã lưu HTML.")


process = CrawlerProcess(settings={"LOG_ENABLED": False})
process.crawl(BooksSpider)
process.start()