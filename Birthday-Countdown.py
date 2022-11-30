import time

today = date.today()

birthday = date(2009, 8, 11)

this_years_birthday = date(today.year, birthday.month, birthday.day)
days_until_birthday = (this_years_birthday-today).days
days_alive = (today-birthday).days

print('You are ' + str(days_alive) + ' days old!')

if days_until_birthday > 0:
  print('You have ' + days_until_birthday + 'until your birthday.'
elif days_until_birthday == 0:
  print("Happy Birthday!!")
else:
  print("Wait until next year for your birthday..")
        
