import requests

#verify cities registered in api on this token
def verifyCitiesAddedInApi(token:str):
    url =  'http://apiadvisor.climatempo.com.br/api-manager/user-token/'+token+'/locales'
    r = requests.get(url)
    #verify if th response is a error, if it's return none, else returne the cities id registered in api
    if r.status_code == 400:
        return None
    else:
        return r.json()['locales']
    
def nameCityByiD(token: str, cityId: int):
    url =  'http://apiadvisor.climatempo.com.br/api/v1/locale/city/3477?token='+token
    r = requests.get(url)
    
    if r.status_code == 400:
        return None 
    else:
        return r.json()['name']
    
def currentWeather(token: str, cityId: int):
    url=  'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/3477/current?token='+token
    r = requests.get(url)
    
    if r.status_code == 400:
        return None
    else: 
        return r.json()['data']