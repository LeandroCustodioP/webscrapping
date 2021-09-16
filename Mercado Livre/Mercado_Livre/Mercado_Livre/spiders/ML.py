import scrapy

class MlSpider(scrapy.Spider):
    name = 'ML'
    
    start_urls = [f'https://www.mercadolivre.com.br/ofertas?page={i}' for i in range(1,210)]

    def parse(self, response, **kwargs):
        for i in response.xpath('//li[@class="promotion-item"]'):
            price = i.xpath('.//span[@class="promotion-item__oldprice"]//text()').getall()
            title = i.xpath('.//p[@class="promotion-item__title"]/text()').get()
            link = i.xpath('./a/@href').get()

            yield{
                'price':price,
                'Title':title,
                'Link':link
            }