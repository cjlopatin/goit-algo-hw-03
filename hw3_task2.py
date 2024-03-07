# Лопатін Євген домашка модулю 3
# завдання 2
# Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

import random  # імопртуємо модуль random

def get_numbers_ticket(min, max, qty): # створюємо функцію, яка приймає параметри
    if not isinstance(min, int) or not isinstance(max, int) or not isinstance(qty, int): # перевіряємо чи умови є цілим числом
        print(f"Ви ввели не ціле число. Введіть дані цілим числом!")
        return []
    try: # робимо перевірку коректності умов данних
        if min > 1 or max < 100 or qty >= min or qty < (max - min + 1):
            numbers_list = list(range(min, max)) # створюємо список з заданим діапазоном
            lottery_mix_choice = random.sample(numbers_list, qty) # вибираємо унікальни цифри за вказаною кількістю
            lottery_sorted_choice = lottery_mix_choice.sort() # сортуємо отриманий список по зростанню
            print("Ваші лотерейні числа:", lottery_mix_choice) # виводимо результат в терміналі
    except ValueError: # виключаємо помилку 
        print(f"Перше число не може бути меншим за 1, а друге більшим за 100. Кількість вибору не може бути більшим другого числа -1. Введіть нові дані цілим числом!")
        return []
        
print("----------------------------------------") 
print("Приклади коректної функції:")    
get_numbers_ticket(1, 50, 5) # приклад коректної функції
get_numbers_ticket(2, 100, 10) # приклад коректної функції
print("----------------------------------------") 
print("Приклади некоректної функції:")  
get_numbers_ticket(0, 102, 103) # приклад некоректної функції
get_numbers_ticket(1j, 50, 5.5) # приклад некоректної функції
get_numbers_ticket("один", 50, 5) # приклад некоректної функції