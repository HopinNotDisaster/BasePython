from datetime import date, time, datetime, timedelta

# date0 = date.today()
# date0 = date.today()
# date0 = date.today()
# date0 = date.today()
# print(type(date0))
# print(date0.strftime("%Y--%m--%d"))
# print(date0.strftime("%Y--%m--%d"))
# print(date0.year)
# print(date0.year)
# print(date0.year)
#
# datetime0 = datetime.now()
# print(datetime0.strftime("%Y-%m-%d %H:%M:%S"))
# print(datetime0.strftime("%Y-%m-%d %H:%M:%S"))


# # 使用数字构造日期
# date0 = date(year=2001, month=1, day=10)
# 获取今天日期
# date0 = date.today()
# date0 = date.today()
#
# print(type(date0))
# #  取得日期中每一个部分
# print(date0.year, date0.month, date0.day, date0.weekday())
# # %y 两位年  %Y 四位年份  %m 两位月  %d两位日
# print(date0.strftime("%Y-%m-%d"))

# # 使用数字构造时间
# time0 = time(hour=17, minute=1, second=30)
# print(type(time0))
# print(time0.hour, time0.minute, time0.second)
# print(time0.hour, time0.minute, time0.second)
# print(time0.hour, time0.minute, time0.second)
# print(time0.hour, time0.minute, time0.second)
# print(time0.utctime("%H:%M:%S"))

#
# # datetime0 = datetime(year=2001, month=5, day=25, hour=5, minute=29, second=11)
# datetime0 = datetime.now()
# print(type(datetime0))
# print(datetime0.year, datetime0.month, datetime0.day, datetime0.hour, datetime0.minute, datetime0.second)
# print(datetime0.strftime("%Y-%m-%d %H:%M:%S"))
# print(datetime0.strftime("%Y-%m-%d %H:%M:%S"))
# print(datetime0.strftime("%Y-%m-%d %H:%M:%S"))
# print(datetime0.strftime("%Y-%m-%d %H:%M:%S"))
# print(datetime0.strftime("%Y-%m-%d %H:%M:%S"))
# print(datetime0.strftime("%Y-%m-%d %H:%M:%S"))


now = datetime.now()
print(now.strftime("%Y/%m/%d %H:%M:%S"))

timedelta0 = timedelta(weeks=1, days=1, hours=2, seconds=30)
print(timedelta0.days, timedelta0.seconds)

future = now + timedelta(weeks=2, hours=2)
print(type(future), future.strftime("%Y/%m/%d %H:%M:%S"))

future = now - timedelta(hours=8)
print(type(future), future.strftime("%Y/%m/%d %H:%M:%S"))
