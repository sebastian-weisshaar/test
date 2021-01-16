# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class AlbertHeijnPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn=sqlite3.connect("items.db")
        self.cursor=self.conn.cursor()

    def create_table(self):
        query="""CREATE TABLE IF NOT EXISTS items_tb(
        name TEXT,
        price REAL,
        cat1 TEXT,
        cat2 TEXT, 
        cat3 TEXT, 
        cat4 TEXT, 
        cat5 TEXT,
        unit TEXT
        )"""
        self.cursor.execute(query)

        pass

    def process_item(self, item, spider):
        query=''' INSERT INTO items_tb(name,price,cat1,cat2,cat3,cat4,cat5,unit)
        VALUES(?,?,?,?,?,?,?,?)
        '''
        values=(item["name"],item["price"],item["category1"],item["category2"],item["category3"],item["category4"],item["category5"],item["unit"])
        self.cursor.execute(query,values)
        self.conn.commit()

        return item

    def extract_unit(self,word):
        elements=word.split(" ")



