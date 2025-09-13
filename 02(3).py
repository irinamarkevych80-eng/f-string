product_name = input("Введіть назву товару: ")
quantity = int(input("Введіть кількість: "))
price = float(input("Введіть ціну за одиницю: "))
date = input("Введіть дату: ")

total_cost = quantity * price

product_name2 = input("Введіть назву товару: ")
quantity2 = int(input("Введіть кількість: "))
price2 = float(input("Введіть ціну за одиницю: "))
date2 = input("Введіть дату: ")

total_cost2 = quantity2 * price2

product_name3 = input("Введіть назву товару: ")
quantity3 = int(input("Введіть кількість: "))
price3 = float(input("Введіть ціну за одиницю: "))
date3 = input("Введіть дату: ")

total_cost3 = quantity3 * price3

product_name4 = input("Введіть назву товару: ")
quantity4 = int(input("Введіть кількість: "))
price4 = float(input("Введіть ціну за одиницю: "))
date4 = input("Введіть дату: ")

total_cost4 = quantity4 * price4

product_name5 = input("Введіть назву товару: ")
quantity5 = int(input("Введіть кількість: "))
price5 = float(input("Введіть ціну за одиницю: "))
date5 = input("Введіть дату: ")

total_cost5 = quantity5 * price5

product_name6 = input("Введіть назву товару: ")
quantity6 = int(input("Введіть кількість: "))
price6 = float(input("Введіть ціну за одиницю: "))
date6 = input("Введіть дату: ")

total_cost6 = quantity6 * price6

product_name7 = input("Введіть назву товару: ")
quantity7 = int(input("Введіть кількість: "))
price7 = float(input("Введіть ціну за одиницю: "))
date7 = input("Введіть дату: ")

total_cost7 = quantity7 * price7

cost = (price * quantity) + (price2 * quantity2) + (price3 * quantity3) + (price4 * quantity4) + (price5 * quantity5) + (price6 * quantity6) + (price7 * quantity7)

print(f"Продукт: {product_name}, Кількість: {quantity}, Вартість: {total_cost}, Date: {date}")

print(f"Продукт: {product_name2}, Кількість: {quantity2}, Вартість: {total_cost2}, Date: {date2}")

print(f"Продукт: {product_name3}, Кількість: {quantity3}, Вартість: {total_cost3}, Date: {date3}")

print(f"Продукт: {product_name4}, Кількість: {quantity4}, Вартість: {total_cost4}, Date: {date4}")

print(f"Продукт: {product_name5}, Кількість: {quantity5}, Вартість: {total_cost5}, Date: {date5}")

print(f"Продукт: {product_name6}, Кількість: {quantity6}, Вартість: {total_cost6}, Date: {date6}")

print(f"Продукт: {product_name7}, Кількість: {quantity7}, Вартість: {total_cost7}, Date: {date7}")

print(f"Сума за тиждень: {cost}")