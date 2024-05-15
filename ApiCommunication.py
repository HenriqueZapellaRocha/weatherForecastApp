from typing import List
from requests import *
import requests

#verify cities registered in api on this token
def verifyCitiesAddedInApi(token:str) -> List[str]:
    url =  'http://apiadvisor.climatempo.com.br/api-manager/user-token/'+token+'/locales'
    r = requests.get(url)
    #verify if th response is a error, if it's return none, else returne the cities id registered in api
    if r.status_code == 400:
        return None
    else:
        return r.json()['locales']

#return the name of the city by the id
def nameCityByiD(token: str, cityId: int) -> Response:
    url =  'http://apiadvisor.climatempo.com.br/api/v1/locale/city/'+str(cityId)+'?token='+token
    r = requests.get(url)
    #verify if th response is a error, if it's return none, else return the name of the city by id
    if r.status_code == 400:
        return None 
    else:
        print(r.json()['name'])
        return r.json()['name']

def cityIdByName(token:str, cityName:str):
    url = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name="+cityName+"&token="+token
    result = requests.get(url)
    
    print(result.json()[0]['id'])

#search the current wheater in api using city id
def currentWeather(token: str, cityId: int) -> Response:
    url=  'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/'+str(cityId)+'/current?token='+token
    
     #verify if th response is a error, if it's return none, else return the current wheater data 
    r = requests.get(url)
    if r.status_code == 400:
        return None
    else: 
        return r.json()['data']
    
def putCityInApi(token:str, cityId: int):
    url= 'http://apiadvisor.climatempo.com.br/api-manager/user-token/'+token+'/locales'
    head=  {'Content-Type':'application/x-www-form-urlencoded'}
    data = {'localeId[]': [str(cityId)]}
    
    response = requests.put(url, data=data,headers=head)
    print(response.text)