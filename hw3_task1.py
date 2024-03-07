# Лопатін Євген домашка модулю 3
# завдання 1
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

from datetime import datetime, timedelta

def get_days_from_today(): # створюємо функцію
    date = input(f"Введіть дату в форматі чисел РРРР-ММ-ДД: ") # створюємо поле для вводу дати
    try: # інтегруємо блок перевірки на коректність вводу данних
        date_corrected = datetime.strptime(date, "%Y-%m-%d")
    except ValueError: # виключаємо помилку некоректного вводу данних
        print(f"Ви ввели неправильний формат дати! Введіть дату в числовому форматі РРРР-ММ-ДД") # виводимо текст помилки
        return get_days_from_today() #повертаємо функцію

    now_date = datetime.today() # створюємо змінну поточної дати
    delta_days = date_corrected - now_date # розраховуємо дельту між введеною датою та поточною датою
    if delta_days.days > 0: # інтегруємо умови виводу меседжу 
        print(f"Різниця між заданою майбутньою датою та поточною датою {delta_days.days} днів")
    elif delta_days.days == 0:
        print(f"Ви задали сьогоднішню дату")
    else:
        print(f"Різниця між заданою датою в минулому та поточною датою {delta_days.days} днів")
            
get_days_from_today()