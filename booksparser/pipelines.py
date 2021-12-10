# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class BooksparserPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase =client.labirint_books

    def process_item(self, item, spider):
        item['price'] = self.float_converting(item['price'])
        item['rating'] = self.float_converting(item['rating'])
        item['discount_price'] = self.process_new_price(item['discount_price'])

        collection = self.mongobase[spider.name]
        collection.insert_one(item)
        return item

    def float_converting(self, num):
        try:
            num = float(num)
            return num
        except:
            pass

    def process_new_price(self, price_list):
        try:
            float_price = float(price_list[1])
            return float_price
        except:
            pass

