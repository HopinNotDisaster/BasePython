# import time
#
# # time.time整数部分是从1970 - 1 - 1
# # 0
# # 时到现在的秒数
# print(time.time())
# time.sleep(5)
# print(time.time())
# time.sleep(5)
# print(time.time())


# 日历
import  calendar

print(calendar)
# 年历
print(calendar.calendar(2024))
# 月历
print(calendar.month(2024, 1))
# 周几
print(calendar.weekday(2024, 1, 11))
# 是否为闰年
print(calendar.isleap(2001))
