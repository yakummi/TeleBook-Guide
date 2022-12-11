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
            DATABASE.insert_python(name=title, image=image)


    def parser_java(self):
        response = requests.get(url=URL, headers=headers, params=java_params)
        soup = BeautifulSoup(response.text, 'html.parser')
        container = soup.find_all('div', 'product-list__item')
        for elements in container:
            title = elements.find('a', 'product-card__name smartLink').text
            image_parser = elements.find('source', {'type': 'image/jpg'}).get('data-srcset') # доделать
            image = ('https:'+image_parser).split(' ')[0]
            DATABASE.insert_java(name=title, image=image)

    def parser_javascript(self):
        response = requests.get(url=URL, headers=headers, params=javascript_params)
        soup = BeautifulSoup(response.text, 'html.parser')
        container = soup.find_all('div', 'product-list__item')
        for elements in container:
            title = elements.find('a', 'product-card__name smartLink').text
            image_parser = elements.find('source', {'type': 'image/jpg'}).get('data-srcset') # доделать
            image = ('https:' + image_parser).split(' ')[0]
            DATABASE.insert_javascript(name=title, image=image)



c = ClientParser()
c.parser_javascript()

