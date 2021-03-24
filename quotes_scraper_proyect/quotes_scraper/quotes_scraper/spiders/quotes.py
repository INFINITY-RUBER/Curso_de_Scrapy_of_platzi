import scrapy

# titulo: //h1/a/text()
# citas: //span[@class="text" and @itemprop="text"]/text()
# top ten tags: //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()
# Autor tags: //span[@class="author" and @itemprop="author"]/text()
# Next page button : //ul[@class="pager"]//li[@class="next"]/a/@href
class QuotesSpider(scrapy.Spider):
    name='quotes'
    start_urls = [
        'http://quotes.toscrape.com/page/1/'        
    ]
    # configuracion para que guarde Automaticamente el resultado
    custom_settings = {
        'FEED_URI': 'quotes.json', # Nombre archivo
        'FEED_FORMAT': 'json',  # formato a guardar
        'CONCURRENT_REQUESTS': '24', # cantidad de reques maximos
        'MEMUSAGE_LIMIT_MB':'2048', # cantidad de memoria a usar
        'MEMUSAGE_NOTIFY_MAIL': ['ruberhernandez@gmail.com'], # correo de notificacion de alerta memoria 
        'ROBOTSTXT_OBEY': True, # reglas de informacion sencible
        'USER_AGENT': 'ruberInfinity', # firma de registro en la consulta
        'FEED_EXPQRT_ENCODING': 'utf-8'  # Codificacion para tildes
    }


    # def parse(self, response):
        # print('*' * 20)
        # print('\n\n\n') # tres saltos de linea
        # # print(response.status, response.headers)
        # title = response.xpath('//h1/a/text()').get() # por que es uno solo 
        # print(f'Titulo {title}')
        # print('\n\n')
        # quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall() # por que son varias
        # print('Citas: ')
        # for quote in quotes:
        #     print(f'- {quote}')
        # print('\n\n')        
        # top_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall() # por que son varias
        # print('top_tags: ')
        # for tag in top_tags:
        #     print(f'- {tag}')
        # print('\n\n')
        # print('*' * 20)
        # print('\n\n')

    def parse_only_quotes(self, response, **kwargs): # **kwargs >> significa que desenpaquetar diccionario de argumentos aqui
        if kwargs:
            quotes = kwargs['quotes'] # variable local guardo la citas
        quotes.extend(response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall())

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
        else:
            yield{ # guarde quotes
                'quotes': quotes
            }

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get() # por que es uno solo 
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall() # por que son varias
        top_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall() # por que son varias

        top = getattr(self, 'top', None)# si existe en el spider el atributo 'top' se guardara en la variable y si no es NONE
        if top:
            top = int(top)
            top_tags = top_tags[:top]

        yield{ # guarda la info
            'title': title,              
            'top_tags': top_tags
        }

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes})
            # .folow(next_page_button_link,) une la pagina web don la pagina siquiente
            # callback=self.parse) hace que haga llamado a la pagina siguiente y repita el proceso del metodo parce




