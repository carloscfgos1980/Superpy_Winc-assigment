# Comparing dates in Python

# Simple Python program to compare dates

'''importing datetime module'''  # This one is for the example # 1
from datetime import *
# import datetime

# date in yyyy/mm/dd format
# d1 = datetime.datetime(2018, 5, 3)
# d2 = datetime.datetime(2018, 6, 1)

# Comparing the dates will return
# either True or False
# print("d1 is greater than d2 : ", d1 > d2)
# print("d1 is less than d2 : ", d1 < d2)
# print("d1 is not equal to d2 : ", d1 != d2)

'''
# Code #2 : Sorting dates
# importing datetime module

# create empty list
group = []

# add today's date
group.append(date.today())

# create some more dates
d = date(2015, 6, 29)
group.append(d)

d = date(2011, 4, 7)
group.append(d)

# add 25 days to the date
# and add to the list
group.append(d + timedelta(days=25))

# sort the list
group.sort()

# print the dates
for d in group:
    print(d)


# Code #3 : Comparing Dates
# importing datetime module

# Enter birth dates and store
# into date class objects
d1, m1, y1 = [int(x) for x in input("Enter first"
                                    " person's date(DD/MM/YYYY) : ").split('/')]

b1 = date(y1, m1, d1)

# Input for second date
d2, m2, y2 = [int(x) for x in input("Enter second"
                                    " person's date(DD/MM/YYYY) : ").split('/')]

b2 = date(y2, m2, d2)

# Check the dates
if b1 == b2:
    print("Both persons are of equal age")

elif b1 > b2:
    print("The second person is older")

else:
    print("The first person is older")

'''


def comparing_dates(date1, date2):
    d1, m1, y1 = [int(x) for x in date1.split('/')]

    b1 = date(y1, m1, d1)
    print('b1', b1)

# Input for second date
    d2, m2, y2 = [int(x) for x in date2.split('/')]

    b2 = date(y2, m2, d2)
    print('b2', b2)

# Check the dates
    if b1 == b2:
        print("Both persons are of equal age")

    elif b1 > b2:
        print("The second person is older")

    else:
        print("The first person is older")


print(comparing_dates("12/05/2017", "10/11/2015"))

# Date of today

today = date.today()
print("Today date is: ", today)


# Date of yesterday

currentTimeDate = datetime.now() - timedelta(days=1)
yesterday = currentTimeDate.strftime('%Y-%m-%d')

print('yesterday', yesterday)
date1 = '2023-01-05'
y1, m1, d1 = [int(x) for x in date1.split('-')]

b1 = date(y1, m1, d1)
# day = date(2023, 1, 5)
delta = today - b1
print(delta.days)
