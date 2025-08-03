import scrapy


class QuoteExtractorSpider(scrapy.Spider):
    name = "quote_extractor"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        print(response.text[0:500])

        text = response.css('div.quote')
        
        for quote in text:
            quote_text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()
            yield{
                'quote': quote_text,
                'author': author,
                'tag': tags
            }
        next_pg = response.css('li.next a::attr(href)').get()
        if next_pg:
            yield response.follow(next_pg,callback=self.parse)
