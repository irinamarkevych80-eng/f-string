def weather_report1(city1, temperature1, date1, humidity1, weather_description1):
  return f"Погода в місті {city1}:\nТемпература: {temperature1}°C\nВологість: {humidity1}%\nДата: {date1}\n{weather_description1}"

city1 = input("Введіть назву міста: ")
date1 = input("Введіть дату: ")
temperature1 = float(input("Введіть температуру: "))
humidity1 = int(input("Введіть вологість: "))
weather_description1 = input("Введіть опис погоди: ")

print(weather_report1(city1, temperature1, date1, humidity1, weather_description1))

def weather_report2(city2, temperature2, date2, humidity2, weather_description2):
  return f"Погода в місті {city2}:\nТемпература: {temperature2}°C\nВологість: {humidity2}%\nДата: {date2}\n{weather_description2}"

city2 = input("Введіть назву міста: ")
date2 = input("Введіть дату: ")
temperature2 = float(input("Введіть температуру: "))
humidity2 = int(input("Введіть вологість: "))
weather_description2 = input("Введіть опис погоди: ")

print(weather_report2(city2, temperature2, date2, humidity2, weather_description2))

def weather_report3(city3, temperature3, date3, humidity3, weather_description3):
  return f"Погода в місті {city3}:\nТемпература: {temperature3}°C\nВологість: {humidity3}%\nДата: {date3}\n{weather_description3}"

city3 = input("Введіть назву міста: ")
date3 = input("Введіть дату: ")
temperature3 = float(input("Введіть температуру: "))
humidity3 = int(input("Введіть вологість: "))
weather_description3 = input("Введіть опис погоди: ")

print(weather_report3(city3, temperature3, date3, humidity3, weather_description3))