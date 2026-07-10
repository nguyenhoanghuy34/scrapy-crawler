import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup, Tag


class StructureSpider(scrapy.Spider):
    name = "structure"

    start_urls = [
        "https://books.toscrape.com/"
    ]

    custom_settings = {
        "LOG_ENABLED": False
    }

    def parse(self, response):

        soup = BeautifulSoup(response.text, "html.parser")

        print("\n========== DOM TREE ==========\n")

        self.print_dom(
            soup.body,
            level=0,
            max_depth=8
        )


    def print_dom(self, node, level=0, max_depth=8):

        if not isinstance(node, Tag):
            return

        # tránh cây quá sâu
        if level > max_depth:
            return


        indent = "│   " * level


        # tên tag
        info = node.name


        # id
        if node.get("id"):
            info += f"#{node.get('id')}"


        # class
        if node.get("class"):
            classes = ".".join(node.get("class"))
            info += f".{classes}"


        # số con trực tiếp
        children = [
            child 
            for child in node.children
            if isinstance(child, Tag)
        ]


        # text trong node
        text = node.get_text(
            strip=True
        )

        text_length = len(text)


        print(
            f"{indent}├── {info}"
            f" | children={len(children)}"
            f" | text={text_length}"
        )


        # đệ quy xuống con
        for child in children:

            self.print_dom(
                child,
                level + 1,
                max_depth
            )



process = CrawlerProcess(
    settings={
        "LOG_ENABLED": False
    }
)


process.crawl(
    StructureSpider
)

process.start()