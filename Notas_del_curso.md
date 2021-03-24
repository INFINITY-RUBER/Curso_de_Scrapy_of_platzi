## Primero, instalemos todas las dependencias necesarias con este comando larguísimo dentro de tu terminal:



```sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev ```


 comando mkdir nombre_proyecto. Luego, con `cd nombre_proyecto` te ubicas dentro del directorio.
Una vez ahí, creas tu entorno virtual con:
 `python3 -m venv venv`. 
 `source venv/bin/activate`
 Este último comando creará una carpeta de nombre “venv” donde estarán los archivos internos de Python que usará tu proyecto. Verifica con ls que exista. ¿Todo correcto? Sigamos adelante actualizamos pip:.
 `python3 -m pip install pip --upgrade`

Ahora, podemos instalar Scrapy sin ningún problema. Otro paquete que instalaremos en el camino es autopep8, que nos servirá para formatear automáticamente nuestro código Python siguiendo los lineamientos de PEP 8, la guía de estilos oficial del lenguaje. Ambos paquetes los instalamos con el comando:
`pip3 install autopep8 scrapy`

### CREAR UN ENTORNO DE SCRAPY

`scrapy startproject NOMBRE_PROYECT`

Se crea un archivo.py  en la carpeta spiders 

```
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_url = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        with open('resultados.html', 'w', encoding='utf-8') as f:
            f.write(response.text) 
```
## EJECUTAR EL SPIDERS 
`scrapy crawl 'NOMBRE DATO EN LA CLASE'` 
EJ:
 `scrapy crawl quotes`


 ## SCRAPY XPATH CON SHELL

 `scrapy shell 'http://LA_PAGIONA_WEB'`
 COMANTOS:
 >>> `response.xpath('//h1/a/text()') `
 [<Selector xpath='//h1/a/text()' data='Quotes to Scrape'>]
>>> `response.xpath('//h1/a/text()').get()`
'Quotes to Scrape'
>>>  `response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()`

>>> `request.encoding`
'utf-8'
>>> `request.method`
'GET'
>>> `response.status`
200
>>> `response.headers`
cabeseras html
>>> `response.body`
HTML
--------------otros ejemplos de xpath--------------
>>>  `response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()`
>>>  `response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()`

## PROCESOS EN YIELD GUARDAR INFORMACION
Guardar en Json:
>>> `scrapy crawl quotes -o quotes.json`

Guardar en Csv:
>>> `scrapy crawl quotes -o quotes.csv`

## CONFIGURACIONES :
```
custom_settings = {
        'FEED_URI': 'quotes.json', # Nombre archivo
        'FEED_FORMAT': 'json',  # formato a guardar
        'CONCURRENT_REQUESTS': '24', # cantidad de reques maximos
        'MEMUSAGE_LIMIT_MB':'2048', # cantidad de memoria a usar
        'MEMUSAGE_NOTIFY_MAIL': ['ruberhernandez@gmail.com'], # correo de notificacion de alerta memoria 
        'ROBOTSTXT_OBEY': True, # reglas de informacion sencible
        'USER_AGENT': 'ruberInfinity', # firma de registro en la consulta
        'FEED_EXPQRT_ENCODING': 'utf-8' 
    } 
```


### PROYECTO DE CIA

`crapy shell 'https://web.archive.org/web/20201221015417/https://www.cia.gov/library/readingroom/historical-collections'`

links:--    
<!-- traer todos los etiquetas "a" que enpiecen con "href y collection" y sus padres     sean h3 y h2 -->
`response.xpath('//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href').getall()`
Titulos:
`response.xpath('//h1[@class="documentFirstHeading"]/text()').get()`
texto:
`response.xpath('//div[@class="field-item even"]//p[not(@class)][3]/text()').get()`


# SCRAPING HUB

https://app.zyte.com/p/511831/deploy?state=deploy

EN: 
/DOUCUMENTO/Scrapy platzi/platzi_intelligence_agency/platzi_intelligence_agenty
$ pip install shub
$ shub login
API key: *************************
$ shub deploy 511831


## EJECUTAR SCRAPY DESDE LA CONSOLA
`curl -u APIKEY: https://app.scrapinghub.com/api/run.json -d project=N_PROJECT -d spider=NAME_SPIDER`
EJ:
curl -u **************d3ad5e7515df: https://app.scrapinghub.com/api/run.json -d project=511831 -d spider=cia

## TRAER INFORMACION POR COMANDO
`curl -u APIKEY: https://storage.scrapinghub.com/items/PROYECT_ID/SPIDER_NUMBER/JOB_NUMBER`
EJ:
curl -u **************d3ad5e7515df: https://storage.scrapinghub.com/items/511831/1/2`