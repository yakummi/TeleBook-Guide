from fake_useragent import UserAgent

URL = 'https://book24.ru/search/'
# URL = 'https://book24.ru/search/page-10/'


headers = {
    'User-Agent': UserAgent().chrome
}

python_params = {
    'q': 'Python'
}

javascript_params = {
    'q': 'JavaScript'
}

java_params = {
    'q': 'Java'
}