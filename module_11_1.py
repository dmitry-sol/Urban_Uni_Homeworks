# module_11_1
import os
import numpy as np
import requests
from matplotlib import pyplot as plt
from PIL import Image


# TASK-1, REQUESTS

city = 'Yuzhno-Sakhalinsk'
url1 = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
url2 = 'https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'
key = '< вставьте ключ >'  # Мой личный сгенерированный на сайте код

params = {'key': key,
          'q': city,
          'format': 'json',
          'num_of_days': 1,
          'lang': 'ru'}


def get_weather():
    r = requests.get(url1, params=params)
    the_weather = r.json()
    # print(the_weather)

    if 'data' in the_weather:
        if 'current_condition' in the_weather['data']:
            try:
                return the_weather['data']['current_condition'][0], the_weather['data']['weather'][0]
            except(IndexError, TypeError):
                print("что-то пошло не так")


def get_climate():
    r = requests.get(url1, params=params)
    the_climate = r.json()
    # print(the_climate)

    if 'data' in the_climate:
        if 'current_condition' in the_climate['data']:
            try:
                return the_climate['data']['ClimateAverages'][0]
            except(IndexError, TypeError):
                print("что-то снова пошло не так")


def get_image():
    image = requests.get(url2)
    with open('new_image.png', 'wb') as f:
        f.write(image.content)


def change_ext(infile, ext):
    f, e = os.path.splitext(infile)
    outfile = f + ext
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.show()
                im.save(outfile)
        except OSError:
            print("не могу конвертировать", infile)


def resize(infile, rati):
    try:
        with Image.open(infile) as im:
            new_width = int(im.width * rati)
            new_height = int(im.height * rati)
            im = im.resize((new_width, new_height))
            name_ending = f' {str(new_width)} x {str(new_height)}'
            f, e = os.path.splitext(infile)
            outfile = f + name_ending + e
            im.show()
            im.save(outfile)
    except OSError:
        print("опять что-то не так")


if __name__ == '__main__':
    current_condition, weather = get_weather()
    print('\nПрогноз погоды для:', city)
    print(f'Температура воздуха сейчас: {current_condition['temp_C']}{chr(176)}C')
    print(f'Ощущается как: {current_condition['FeelsLikeC']}{chr(176)}C')
    print(f'Максимальная/минимальная температура: {weather['maxtempC']}/{weather['mintempC']}{chr(176)}C')
    print(f'Облачность: {current_condition['lang_ru'][0]['value']}')
    print(f'Влажность: {current_condition['humidity']}%')
    print(f'Атмосферное давление: {current_condition['pressure']} hpa\n')
    print(f'Восход/заход солнца: {weather['astronomy'][0]['sunrise']} / {weather['astronomy'][0]['sunset']}')
    print(f'Восход/заход луны: {weather['astronomy'][0]['moonrise']} / {weather['astronomy'][0]['moonset']}')


# TASK-2, NUMPY, MATPLOTLIB

    climate = get_climate()
    climate_ = climate['month']

    a = np.array(climate_)
    month = [climate_[i]['name'] for i in range(len(climate_))]
    mon = [month[i][0:3] for i in range(len(month))]

    avr_min = [float(climate_[i]['avgMinTemp']) for i in range(len(climate_))]
    avr_max = [float(climate_[i]['absMaxTemp']) for i in range(len(climate_))]

    width1 = 0.6
    width2 = 0.6
    fig, ax = plt.subplots(ncols=1, figsize=(7, 5), layout='constrained')
    ax.bar(mon, avr_max, width2, label='средне-макс', color='r', alpha=0.5)
    ax.bar(mon, avr_min, width1, label='средне-мин', color='b', alpha=0.5)

    ax.set_ylabel('Темп')
    ax.set_title(f'График среднегодовой температуры в {city}')
    ax.legend(loc='lower left', title='Температура')

    plt.show()


# TASK-3, PILLOW

    file_name = 'pirate ship.jpg'
    new_ext = ".png"
    ratio = 0.5

    change_ext(file_name, new_ext)
    resize(file_name, ratio)
