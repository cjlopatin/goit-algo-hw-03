# Лопатін Євген домашка модулю 3
# завдання 4 
# створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати з Днем народження.

from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.08"},
    {"name": "Jane Smith", "birthday": "1990.05.27"},
    {"name": "Jack Vorobey", "birthday": "1960.03.10"},
    {"name": "James Potter", "birthday": "1997.03.12"}
]
 
  
def prepare_users(users: list):
    prepared_users =[]
    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
            prepared_users.append({"name": user['name'], "birthday": birthday})
        except ValueError:
            print(f"Некоректна дата народження для користувача {user["name"]}")
    return prepared_users   


def get_upcoming_birthdays(prepared_users: list, days=7):
    def find_next_weekday(d, weekday: int):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return d + timedelta(days = days_ahead)

    today = datetime.today().date()  # Поточна дата
    upcoming_birthdays = []
    for user in prepared_users:  # Ітерація по підготовленим користувачам
        birthday_this_year = user["birthday"].replace(year=today.year)  # Заміна року на поточний для дня народження цього року

        if birthday_this_year < today:  # Якщо дата народження вже пройшла цього року
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)  # Переносимо наступний рік

        if 0 <= (birthday_this_year - today).days <= days:  # Якщо день народження в межах вказаного періоду
            if birthday_this_year.weekday() >= 5:  # Якщо день народження випадає на суботу або неділю
                birthday_this_year = find_next_weekday(birthday_this_year, 0)  # Знаходимо наступний понеділок

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')  # Форматуємо дату у рядок
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })
    #return upcoming_birthdays
    upcoming_birthdays = get_upcoming_birthdays(prepared_users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)