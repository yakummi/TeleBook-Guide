from fake_useragent import UserAgent

URL = 'https://book24.ru/search/'

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

c_plus2_params = {
    'q': 'C++'
}