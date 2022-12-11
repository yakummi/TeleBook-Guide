import requests
from bs4 import BeautifulSoup
from parser_settings import URL, headers, python_params, javascript_params, java_params
from database.database import DATABASE

class ClientParser:

    def parser_python(self):
        response = requests.get(url=URL, headers=headers, params=python_params)
        soup = BeautifulSoup(response.text, 'html.parser')
        container = soup.find_all('div', 'product-list__item')
        for elements in container:
            title = elements.find('a', 'product-card__name smartLink').text
            image_parser = elements.find('source', {'type': 'image/jpg'}).get('data-srcset') # доделать
            image = ('https:'+image_parser).split(' ')[0]
            DATABASE.check_parser_python(name=repr(title), image=repr(image))


    def parser_java(self):
        response = requests.get(url=URL, headers=headers, params=java_params)
        soup = BeautifulSoup(response.text, 'html.parser')
        container = soup.find_all('div', 'product-list__item')
        for elements in container:
            title = elements.find('a', 'product-card__name smartLink').text
            image_parser = elements.find('source', {'type': 'image/jpg'}).get('data-srcset') # доделать
            image = ('https:'+image_parser).split(' ')[0]
            DATABASE.check_parser_java(name=repr(title), image=repr(image))

    def parser_javascript(self):
        response = requests.get(url=URL, headers=headers, params=javascript_params)
        soup = BeautifulSoup(response.text, 'html.parser')
        container = soup.find_all('div', 'product-list__item')
        for elements in container:
            title = elements.find('a', 'product-card__name smartLink').text
            image_parser = elements.find('source', {'type': 'image/jpg'}).get('data-srcset') # доделать
            image = ('https:' + image_parser).split(' ')[0]
            DATABASE.check_parser_javascript(name=repr(title), image=repr(image))

c = ClientParser()
c.parser_javascript()
c.parser_java()
c.parser_python()
