import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tienda.items import TiendaItem

class TiendaSpider(CrawlSpider):
    name = 'tienda'
    item_count = 0
    allowed_domain = ['www.listado.mercadolibre.com.pe']
    star_url = ['https://listado.mercadolibre.com.pe/laptops#D[A:laptops]'],

    rules ={
        Rule(LinkExtractor(allow =(), restrict_xpaths = ('//li[@class="andes-pagination__button andes-pagination__button--next shops__pagination-button"]/a '))),
        Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h2[@class="ui-search-item__title shops__item-title"]')),
             callback = 'parse_item', follow = False)
    }

    def parse_item():
        ml_item = TiendaItem()

        #informacion de producto 
        ml_item ['titulo'] = response.xpath('normalize-space(//h2[@class="ui-search-item__title shops__item-title"])')
        


