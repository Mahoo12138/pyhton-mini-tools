# 对指定日期段内符合要求的日期提取，并以 YYYY-MM-DD 格式显示

from datetime import *

start_date = date(2020, 3, 2)
end_date = date(2020, 5, 19)
delta = timedelta(days=1)
while start_date <= end_date:
    # print (start_date.strftime("%Y-%m-%d"))
    # print (start_date.weekday())
    if (start_date.weekday()==0 or start_date.weekday() == 2 or start_date.weekday() == 4):
        print (start_date.strftime("%Y-%m-%d"))
    start_date += delta