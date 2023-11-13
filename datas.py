import datetime

# Variables

Today = datetime.date.today()

print(Today.year)
print(Today.month)
print(Today.day)

print(datetime.datetime.now())

print(datetime.datetime.now().strftime("%H:%M:%S"))

date1 = "2000-01-01"
date2 = "2000-02-01"

date1_obj = datetime.datetime.strptime(date1, "%Y-%m-%d")
date2_obj = datetime.datetime.strptime(date2, "%Y-%m-%d")

diferenca = date2_obj - date1_obj

print(diferenca.days)