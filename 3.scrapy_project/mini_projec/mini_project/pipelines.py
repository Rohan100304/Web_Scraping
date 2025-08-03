# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MiniProjectPipeline:
    def process_item(self, item, spider):
        return item


class CleaningPipeline:
    def process_item(self, item, spider):
        # Clean the item data
        item['title'] = item['title'].strip() if item['title'] else None
        price = item['price'].replace('£', '').replace('$','').strip() if item['price'] else None

        # Convert price to float, handle potential conversion errors
        try:
            item['price'] = float(price) if price else None
        except ValueError:
            item['price'] = None

        rating_map = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        rating_val = item.get('rating', '')
        rating = rating_val.split()[-1] if rating_val else 'NA'
        item['rating'] = rating_map.get(rating, None)

        return item