import datetime

timeStamp = 1640916076
dateArray = datetime.datetime.utcfromtimestamp(timeStamp) + datetime.timedelta(hours=8)
# timedelta(hours=8)
# print(dateArray)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)
print(type(otherStyleTime))

now = datetime.datetime.now()
dc = now.strftime("%H:%M:%S")
tzshj = dc
print("github通知时间是：" + tzshj)
d1 = now.strftime('%Y-%m-%d %H:%M:%S')
print("github时间d1是：" + d1)
d3 = datetime.datetime.strptime(d1, '%Y-%m-%d %H:%M:%S')
print(d3)

d2 = datetime.datetime.strptime(otherStyleTime, "%Y-%m-%d %H:%M:%S")
print(d2)

timedelay = d3 - d2

timedelay = str(timedelay)
print(timedelay)
