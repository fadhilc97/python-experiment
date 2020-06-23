import datetime

date_string = '2020-06-16'
date_string_casting = datetime.datetime.strptime(date_string, '%Y-%m-%d')

print(type(date_string))
print(date_string_casting.strftime('%d/%m/%Y'))