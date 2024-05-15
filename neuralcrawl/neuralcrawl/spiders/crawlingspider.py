import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MyCrawlerSpider(CrawlSpider):
    name = 'mycrawler'
    allowed_domains = ['etstur.com']
    start_urls = ['https://www.etstur.com/Yurtdisi-Tatil-Turlari']

    rules = (
        Rule(LinkExtractor(allow=('/Yurtdisi-Tatil-Turlari/.*'),deny=('/Kurban-Bayrami-Turlari', '/Balkanlar-Ve-Yunanistan-Turlari', '/Orta-Dogu-Turlari','/Avrupa-Turlari','/Amerika-Turlari','/Balayi-Turlari','/Uzak-dogu-turlari','/yunan-adalari-turlari','/Yilbasi-Turlari','/Kasim-Ara-Tatil','/Vizesiz-Yurt-Disi-Turlari','/Egzotik-Adalar-Turlari')), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=('/Yurtdisi-Tatil-Turlari/.*')), follow=True)
    )

    def parse_item(self, response):
        title = response.css('div.banner div.info h1::text').get()
        start_location = response.css('div.banner div.location span:nth-of-type(1)::text').get().strip()
        end_location = response.css('div.banner div.location span:nth-of-type(2)::text').get().strip()
        date = response.css('div.banner div.labels li:nth-of-type(2) span::text').get().strip()
        duration = response.css('div.banner div.labels li:nth-of-type(1) span::text').get().strip()

        yield {
            'title': title,
            'start_location': start_location,
            'end_location': end_location,
            'date': date,
            'duration': duration
        }
