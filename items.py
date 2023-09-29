# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TiendaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    precio = scrapy.Field()
    envio = scrapy.Field()
    ubicacion = scrapy.Field()
    descripción = scrapy.Field()



    pass
