import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.co.uk']
    start_urls = ['http://amazon.co.uk/']

    def parse(self, response):
        pass
