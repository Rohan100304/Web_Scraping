# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyPiplinesPipeline:
    def process_item(self, item, spider):
        return item


class  quotePipeline:
    def process_item(self, item, spider):
        # Here you can process the item, e.g., clean data, validate, etc.
        item['text'] = item['text'].strip().replace('“','"').replace('”','"')
        return item