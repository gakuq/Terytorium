import requests
import datetime as dt


class Weather:

    def translate(self, miasto):
        city = miasto.replace(' ', '_')
        translated_string = city.translate(str.maketrans("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ", "acelnoszzACELNOSZZ"))
        # print(miasto)
        # print(translated_string)
        return translated_string

    def __init__(self, city):
        czas = dt.datetime.today()
        self.url = f'http://api.weatherapi.com/v1/history.json?key=ef3a360dc43d4036b3c143137232809&q={self.translate(city)}&dt={czas}'


    def get_data(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            info = r.json()['forecast']['forecastday'][0]['day']
            POGODA = {
                'maxtemp_c': info['maxtemp_c'],
                'mintemp_c': info['mintemp_c'],
                'avgtemp_c': info['avgtemp_c'],
                'maxwind_kph': info['maxwind_kph'],
                'avghumidity': info['avghumidity'],
                'avgvis_km': info['avgvis_km'],
                'img': info['condition']['icon'],
            }
            return POGODA
        else:
            raise ValueError(f'Response code is {r.status_code}')


# weather = Weather('Lwówek Śląski').get_data()
# print(weather)

