import requests

MainUrl = 'https://wooordhunt.ru/'
TargetUrl = 'https://wooordhunt.ru/'

def get_page(url=None):
    if url:
        resp = requests.get(url)
        return resp
    return True

