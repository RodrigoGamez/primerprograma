
import datetime

year = int(input("Dime un año: "))
month = int(input("Dime un mes: "))
day = int(input("Dime un dia: "))

user_date = datetime.datetime(year=year, month=month, day=day)

time_remainig = user_date - datetime.datetime.now()

print("Quedan {} dias, {} horas".format(time_remainig.days, int(time_remainig.seconds / 3600)))