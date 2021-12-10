import scrapy
from scrapy.http import HtmlResponse
from booksparser.items import BooksparserItem


class LabirintruSpider(scrapy.Spider):
    name = 'labirintru'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/search/%D0%BF%D1%80%D0%B8%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D1%8F/?stype=0']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='pagination-next__text']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[@class='product-title-link']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.books_parse)

    def books_parse(self, response: HtmlResponse):
        name = response.xpath("//h1//text()").get()
        link = response.url
        author = response.xpath('//a[@data-event-label="author"]//text()').get()
        if response.xpath('//span[@class="buying-price-val-number"]//text()').get() is None:
            price = response.xpath('//div[@class="buying-priceold-val"]//text()').get()
            discount_price = response.xpath('//div[@class="buying-pricenew-val"]//text()').getall()
        else:
            price = response.xpath('//span[@class="buying-price-val-number"]//text()').get()
            discount_price = '-'
        rating = response.xpath('//div[@id="rate"]//text()').get()
        item = BooksparserItem(name=name, link=link, author=author, price=price,
                               discount_price=discount_price, rating=rating)
        yield item




