#Write a Python program to determine whether a given year is a leap year.
import datetime as dt
import calendar as cl
date_str = '19-09-2022'

date_object = dt.datetime.strptime(date_str, '%d-%m-%Y')
print(date_object)
print(date_object.day)
print(date_object.year)
print(date_object.month)
print(date_object.replace(year=date_object.year-1,month=date_object.month+1,day=date_object.day+4))


