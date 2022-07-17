import requests
import schedule 
from math import floor
from datetime import datetime
import time


def weather():

    api_key = 'YOUR_KEY_HERE'

    root_url = 'http://api.openweathermap.org/data/2.5/weather?'

    city_name = 'Los Mochis'
    
    url = f'{root_url}appid={api_key}&units=metric&q={city_name}'

    r = requests.get(url)

    data = r.json()

    if data['cod'] == 200:

        desc = data['weather'][0]['icon']

        # Mostrar una descripción y emoji acorde al icono.

        if desc == '01d' or desc == '01n':

            msg = '*Clima actual en Los Mochis* 🌞\n\n'
            msg = msg + '*Cielo despejado*\n'
        
        elif desc == '02d' or desc == '02n':

            msg = '*Clima actual en Los Mochis* 🌤\n\n'
            msg = msg + '*Pocas nubes*\n'
        
        elif desc == '03d' or desc == '03n':

            msg = '*Clima actual en Los Mochis* 🌥\n\n'
            msg = msg + '*Nubes dispersas*\n'
        
        elif desc == '04d' or desc == '04n':

            msg = '*Clima actual en Los Mochis* 🌥\n\n'
            msg = msg + '*Nubes dispersas*\n'
        
        elif desc == '09d' or desc == '09n':

            msg = '*Clima actual en Los Mochis* 🌦\n\n'
            msg = msg + '*Chispiteando*\n'
        
        elif desc == '10d' or desc == '10n':

            msg = '*Clima actual en Los Mochis* 🌧\n\n'
            msg = msg + '*Lloviendo*\n'

        elif desc == '11d' or desc == '11n':

            msg = '*Clima actual en Los Mochis* ⛈\n\n'
            msg = msg + '*Tormenta eléctrica*\n'
        
        elif desc == '50d' or desc == '50n':

            msg = '*Clima actual en Los Mochis* 🌫\n\n'
            msg = msg + '*Neblina*\n'

        # Emoji dependiendo de la temperatura.

        temp = data['main']['temp']

        if temp < 22:

            msg = msg + f'*Temperatura:* {floor(temp)}° ❄\n'
        
        elif temp > 22 and temp < 30:

            msg = msg + f'*Temperatura:* {floor(temp)}° 🌞\n'
        
        elif temp >= 30:

            msg = msg + f'*Temperatura:* {floor(temp)}° 🔥\n'

        # Emoji dependiendo de la sensación térmica.

        sensacion = data['main']['feels_like']

        if sensacion <= 22:

            msg = msg + f'*Sensación térmica:* {floor(sensacion)}° 🥶\n'

        elif sensacion > 22 and sensacion < 30:

            msg = msg + f'*Sensación térmica:* {floor(sensacion)}° 😜\n'
        
        elif sensacion >= 30:

            msg = msg + f'*Sensación térmica:* {floor(sensacion)}° 🥵\n'
            
    
        # Emoji dependiendo del nivel de humedad.

        humedad = data['main']['humidity']

        if humedad > 50:
        
            msg = msg + f'*Humedad:* {humedad}% 😰\n'
        
        else: 

            msg = msg + f'*Humedad:* {humedad}% 😎\n'

        # Emoji dependiendo del nivel de viendo.

        wind = data['wind']['speed']

        if wind > 10:

            msg = msg + f'*Viento:* {wind} km/h 🌬'
        
        else:

            msg = msg + f'*Viento:* {wind} km/h 🍃'

        sendMessage(msg)

def sendMessage(msj):

    bot_token = 'YOUR_KEY_HERE'
    bot_id = '1051998475'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_id + '&parse_mode=Markdown&text=' + msj

    response = requests.get(send_text)

    return response

if __name__ == '__main__':

    schedule.every().day.at('16:00').do(weather)
    schedule.every().day.at('18:30').do(weather)
    schedule.every().day.at('22:30').do(weather)
    schedule.every().day.at('02:30').do(weather)
    schedule.every().day.at('06:30').do(weather)

    while True: 
        print('Ejecutando...')
        schedule.run_pending()
        time.sleep(1)

