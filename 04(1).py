import random

def generate_ticket ():
  ticket_number = random.randint(100000, 999999)
  return f"Квиток №{ticket_number}"

def generate_valute_in_ticket ():
  valute = random.randint(1, 100)
  return f"Ціна: {valute}"

def generate_set_in_transport (last_name, date, destination, departure_time):
  set_transport = random.randint(1, 50)
  return f"Місце №{set_transport}\nПрізвище: {last_name}\nПункт призначення: {destination}\nЧас відправлення: {departure_time}"

last_name = input("Введіть ваше прізвище: ")
date = input("Введіть дату: ")
destination = input("Введіть пункт призначення: ")
departure_time = input("Введіть час відправлення: ")

print(generate_ticket())
print(generate_valute_in_ticket())
print(generate_set_in_transport(last_name, destination, departure_time))