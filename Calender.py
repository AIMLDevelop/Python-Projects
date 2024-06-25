import calendar

year = int(input("Enter the year :" ))

month = int(input("Enter the month : "))

mycal = calendar.month(year,month)

print(mycal)