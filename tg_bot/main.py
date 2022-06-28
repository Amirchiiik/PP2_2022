import requests
import datetime
#from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):
	code_to_smile = {
		'Clear': 'Ясно \U00002600',
		'Clouds': 'Облачно \U00002601',
		'Rain': 'Дождь \U00002614',
		'Drizzle': 'Дождь \U00002614',
		'Thunderstorm': 'Гроза \U000026A1',
		'Snow': 'Снег \U0001F328',
		'Mist': 'Туман \U0001F32B'
	}

	try:
		r = requests.get(
			f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
		)
		data = r.json()
		description = data['weather'][0]['main']
		if description in code_to_smile:
			wd = code_to_smile[description]
		else:
			wd = 'Друг сам посмотри, не пойму, что там происходит!'
		city = data['name']
		temp = data['main']['temp'] 
		print(f"Время сейчас: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\nПогода в городе: {city}\nТемпература: {temp} C\nОписание: {wd}")

	except Exception as ex:
		print(ex)
		print("Проверьте названия города")

def main():
	city = input("Напишите пожалуйста ваш город 🌆: ")
	get_weather(city, open_weather_token)

if __name__== "__main__":
	main()