import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://openaccess.thecvf.com/CVPR2018.py',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        print (page)
        filename = 'cvpr-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        #self.log('Saved file %s' % filename)