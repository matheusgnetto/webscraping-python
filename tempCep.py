import requests
from pycep_correios import get_address_from_cep, WebService

API_KEY = 'XXX'


def getTemperature(cep):
    address = get_address_from_cep(cep, webservice=WebService.APICEP)
    city = address['cidade']
    link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    req = requests.get(link)
    req_dic = req.json()
    desc = req_dic['weather'][0]['description']
    temperature = req_dic['main']['temp'] - 273.15
    print(f'Current temperature in {city}, {temperature:.0f}ºC {desc}.')


cep = str(input('Digite seu CEP: '))
getTemperature(cep)
