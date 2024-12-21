"""📃
**Создание погодного приложения на Python.**

## Краткое содержание 
В данном задании вы разработаете погодное приложение, которое будет получать данные о погоде через API и отображать их пользователю. Вы будете использовать библиотеки `requests` и `plyer` для работы с API и уведомлениями. Также необходимо будет организовать разработку с помощью Git и создать проект на GitHub. Приложение упакуете в exe.

### Технологии: 🦾
- Python
- requests
- plyer
- Git
- GitHub
- PyInstaller

## Задание 👷‍♂️

### Классы и их функциональность

1. **Функция `get_weather`**
   - Аргументы:
     - `city: str`: Название города для получения прогноза погоды.
     - `api_key: str`: Ключ API для доступа к сервису.
   - Возвращает:
     - `dict`: Словарь с данными о погоде.
   - Описание: Выполняет запрос к API и возвращает данные о погоде в виде словаря.

2. **Функция `format_weather_message`**
   - Аргументы:
     - `weather_dict: dict`: Словарь с данными о погоде.
   - Возвращает:
     - `str`: Форматированное сообщение о погоде.
   - Описание: Форматирует данные о погоде в удобочитаемое сообщение.

3. **Функция `notify_weather`**
   - Аргументы:
     - `message: str`: Сообщение о погоде для уведомления.
   - Возвращает:
     - `None`
   - Описание: Отправляет уведомление пользователю с информацией о погоде.

4. **Функция `main`**
   - Описание: Запускает программу, выполняет вызовы вышеуказанных функций и обрабатывает вывод.

### Константы
- `API_KEY`: Ваш ключ API для OpenWeatherMap. Если у вас его нет, можете использовать мой: `23496c2a58b99648af590ee8a29c5348`
- `CITY`: Название города по умолчанию, например, `Москва`.

### Таблица функций:

| Функция                     | Описание                                                    |
| --------------------------- | ----------------------------------------------------------- |
| `get_weather(city, api_key)`| Получает данные о погоде для указанного города.           |
| `format_weather_message(weather_dict)`| Форматирует сообщение о погоде.               |
| `notify_weather(message)`   | Отправляет уведомление с информацией о погоде.             |
| `main()`                   | Запускает основную логику приложения.                      |

## Настройки и дополнительные указания
1. **Создайте новый проект** и настройте виртуальное окружение.
2. **Установите зависимости**: `pip install plyer requests pyinstaller`.
3. **Создайте файл `requirements.txt`** для управления зависимостями. `pip install -r requirements.txt`
4. **Создайте файл README.md**, описывающий ваш проект и его функциональность.
5. **Рефакторинг**: Разделите код на функции, как указано выше.
6. **Упаковка приложения**: Используйте `pyinstaller` для создания исполняемого файла (EXE).

### PyInstaller

Чтобы упаковать ваше приложение в исполняемый файл (EXE), выполните следующие шаги:

1. Убедитесь, что вы находитесь в корневой директории вашего проекта, где находится ваш основной файл приложения.
2. Запустите команду:

```bash
c <название файла.py>
```

- `--onefile`: Указывает PyInstaller собрать все в один исполняемый файл.
- `--noconsole`: Отключает консольное окно при запуске приложения (полезно для графических приложений).
- `--hidden-import plyer.platforms.win.notification`: Указывает на необходимость включения модуля plyer для работы с уведомлениями в Windows.

После выполнения этой команды в папке `dist` будет создан исполняемый файл вашего приложения. Вы можете запускать его на любом компьютере без необходимости установки Python или зависимостей.

**Проверьте, что ваше приложение работает корректно перед упаковкой в EXE. После упаковки так же проведите тестирование.**

>[!warning]
>### Критерии проверки 👌
>1. Приложение должно корректно получать и отображать данные о погоде.
>2. Уведомления должны правильно отображаться с актуальной информацией.
>3. Код должен быть структурирован и легко читаться.
>4. **Проект должен быть размещен на GitHub с не менее чем 5 коммитами.**
>5. **Архив с работой должен содержать код, файл зависимостей, EXE файл и текстовый документ где будет ссылка на репозиторий.**
>6. В архиве **НЕ** должно быть venv и всех служебных папок которые создает pyinstaller


## Код с урока для рефакторинга

python
"""
"""""
# Это погодное приложение, которое работает на Python библиотеке requests, plyer.

# pip install plyer requests pyinstaller

# Образец ссылки https://api.openweathermap.org/data/2.5/weather?q=Москва&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru

# {'coord': {'lon': 37.6156, 'lat': 55.7522}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'облачно с прояснениями', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 0.93, 'feels_like': -3.44, 'temp_min': 0.24, 'temp_max': 0.93, 'pressure': 1022, 'humidity': 61, 'sea_level': 1022, 'grnd_level': 1002}, 'visibility': 10000, 'wind': {'speed': 4.47, 'deg': 214, 'gust': 11.97}, 'clouds': {'all': 64}, 'dt': 1733247335, 'sys': {'type': 2, 'id': 2095214, 'country': 'RU', 'sunrise': 1733204316, 'sunset': 1733230838}, 'timezone': 10800, 'id': 524901, 'name': 'Москва', 'cod': 200}

"""

import requests
from plyer import notification
# Просто сделаем запрос без функций

CITY = 'Химки'
APPI_KEY = '23496c2a58b99648af590ee8a29c5348'
UNITS = 'metric'
LANGUAGE = 'ru'


url = fr'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={APPI_KEY}&units={UNITS}&lang={LANGUAGE}'

response = requests.get(url) # Сделали запрос и получили объект ответа
print(response.status_code) # Получили статус ответа
print(response.json()) # Получили объект Python из JSON


# Получим описание и температуру, и ощущается как
weather_dict = response.json()

# Temp
temp = weather_dict['main']['temp']
# Ощущается как
feels_like = weather_dict['main']['feels_like']
# Описание погоды
description = weather_dict['weather'][0]['description']

print(f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}')

# Уведомление
notification.notify(
    title='Погода в Химках',
    message=f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}',
    app_name='Weather',
    app_icon=None)

