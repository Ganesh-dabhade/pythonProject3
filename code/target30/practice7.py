#input=2022/09/01
#output= 2022/08/01, 2022/08/31
import datetime as dt
date=(dt.date.today())
date_stamp=dt.datetime.now()
print(date)
print(date_stamp)
import calendar as cl
def get_month(date):
    date1=date.month
    date1=date1-1
    year=date.year
    if(date1==1):
        date1=12
        year=year-1

    fdate=date.replace(year=year,month=date1,day=1)
    lm=es = cl.monthrange(year, fdate.month)[1]
    ldate=es = date.replace(year=year,month=date1, day=lm)
    return fdate,ldate
pr_month_details=get_month(dt.date.today())
print(list(pr_month_details))

