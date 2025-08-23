import datetime
import bday_messages

today = datetime.date.today()
next_birthday_input = input("When is your next birthday? Enter as YYYY M D: ")
year, month, day = map(int, next_birthday_input.split())
next_birthday = datetime.date(year, month, day)

days_away = next_birthday - today

if today == next_birthday:
    print(random_message)
else:
    print(f"My next birthday is {days_away.days} days away!")
