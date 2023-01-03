import calendar

weekday = input("Specify a weekday:\n1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\6.Saturday\n7.Sunday")
year = input("Provide a specific year: ")

cal = calendar.monthcalendar(2022, 1)
for i in cal:
    realweekday = int(weekday) - 1
    if i[int(realweekday)] != 0:
        print("Weekday count")