from calendar_tools import UkrainianCalendar

cal = UkrainianCalendar()

date_input = input("Введіть дату у форматі ДД.ММ.РРРР (наприклад, 24.08.2025): ")

result = cal.is_working_day(date_input)

if result is True:
    print(date_input, "— це робочий день.")
elif result is False:
    print(date_input, "— це святковий або вихідний день.")
else:
    print("Невірний формат дати. Спробуйте ще раз.")

# Для перегляду свят:
try:
    year = int(date_input.split(".")[2])
    print("Основні державні свята України:", cal.get_holiday_list(year))
except:
    pass

# 2 завдання
from math_utils import Calculator

calc = Calculator()

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
op = input("Оберіть операцію (+, -, *, /): ")

if op == "+":
    print("Результат:", calc.add(a, b))
elif op == "-":
    print("Результат:", calc.subtract(a, b))
elif op == "*":
    print("Результат:", calc.multiply(a, b))
elif op == "/":
    print("Результат:", calc.divide(a, b))
else:
    print("Невідома операція.")
#3 завдання
from text_analysis import TextStats

user_text = input("Введіть будь-який текст: ")

stats = TextStats(user_text)

print("Кількість слів:", stats.count_words())
letter, count = stats.most_common_letter()
print(f"Найчастіша літера: '{letter}' ({count} разів)")
