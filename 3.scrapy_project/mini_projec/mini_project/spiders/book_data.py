import scrapy
from mini_project.items import MiniProjectItem

class BookDataSpider(scrapy.Spider):
    name = "bood_data"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):

        page = response.css('article.product_pod')
        

        for book in page:
            items = MiniProjectItem()
            items['title'] = book.css('h3 a::attr(title)').get()
            items['price'] = book.css('p.price_color::text').get()
            availability = book.css('p.instock.availability::text').getall()
            items['availability'] = ''.join(availability).strip()

            items['rating'] = book.css('p.star-rating::attr(class)').get()
            yield items
        pass

        next_page = response.css('li.next a::attr(href)').get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)


