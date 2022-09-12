Sum = 0
Times = 0

num =int(input("enter number :"))
Temp = num
while Temp > 0:
    Times = Times + 1
    Temp = Temp // 10

Temp = num
while Temp > 0:
    Reminder = Temp % 10
    Sum = Sum + (Reminder ** Times)
    Temp //= 10

if num == Sum:
           print(f"{num} is Armstrong number")
else:
           print(f"{num} is not Armstrong number")