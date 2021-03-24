import scrapy

# ************* xpath ********************************
# link = //a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href
# titulo = //h1[@class="documentFirstHeading"]/text()
# parrafo = //div[@class="field-item even"]//p[not(@class)][3]/text()


class SpiderCIA(scrapy.Spider):
    name = "cia"
    start_urls = [
        "https://web.archive.org/web/20201221015417/https://www.cia.gov/library/readingroom/historical-collections"
    ]
    custom_settings = {
        'FEED_URI': 'cia.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPQRT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        links_declassifield = response.xpath(
            '//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href').getall()
        for link in links_declassifield:
            # unir la url absoluta con la url del link
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath(
            '//h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath(
            '//div[@class="field-item even"]//p[not(@class)]/text()').get()
        N_pragram = 1
        if len(paragraph) < 30:
            paragraph = response.xpath(
                '//div[@class="field-item even"]//p[not(@class)][2]/text()').get()
            N_pragram = 2
        yield {
            'url': link,
            'title': title,
            'body': paragraph,
            'N_pragram': N_pragram
        }
