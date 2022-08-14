import requests
import json
from bs4 import BeautifulSoup


def getMetas(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, features='html.parser')

    list_meta = []
    for tag in soup.find_all('meta'):
        if 'property' in tag.attrs.keys() and tag.attrs['property'].strip().lower():
            list_meta.append({"name": tag.attrs['content'], "content": tag.attrs['property'][3:]})
    json_object = json.dumps(list_meta, indent=3)
    print(f' metaTags:{json_object}')
    print(type(json_object))


getMetas('http://zoomquilt.org')
