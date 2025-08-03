import scrapy
from scrapy_piplines.items import items

class QuoteSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            item = items()
            item['author'] = quote.css("small.author::text").get()
            item['text'] = quote.css("span.text::text").get()
            item['tags'] = quote.css("div.tags a.tag::text").getall()
            yield item
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
        pass
