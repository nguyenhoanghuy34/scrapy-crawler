import scrapy
from scrapy.crawler import CrawlerProcess


class BooksSpider(scrapy.Spider):
    name = "books"

    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):
        body = response.css("body").get()

        with open("body.html", "w", encoding="utf-8") as f:
            f.write(body)

        print("Đã lưu thẻ <body>.")


process = CrawlerProcess(settings={"LOG_ENABLED": False})
process.crawl(BooksSpider)
process.start()