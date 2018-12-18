import scrapy


class QuotesSpider(scrapy.Spider):
    name = "paper"
    start_urls = []
    download_delay = 0.25
    
    def start_requests(self):
        urls = [
            'http://openaccess.thecvf.com/CVPR2018.py',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for url in response.xpath('//a/@href').extract():
            #self.log('************************ %s' % url)
            if 'pdf' in url:
                if 'supp' in url:
                    pass
                else:
                    yield scrapy.Request('http://openaccess.thecvf.com/' + url, callback=self.parse_deeper)
                
        page = response.url.split("/")[-1]
        filename = '%s.html' % page
        self.log('************************* %s' % page)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
    def parse_deeper(self, response):
        folder = response.url.split("/")[-3]
        page = response.url.split("/")[-1]
        filename = '{0}/{1}'.format(folder, page)
        self.log('************************* %s' % page)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)