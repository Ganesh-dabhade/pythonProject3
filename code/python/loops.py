import  calendar
print(type(range(5,10)))

print(list(range(5, 11, 2)))

for i in range(2, 20, 2): print(i)
import  math
# print month
for month in list(calendar.month_name)[1:]:
    print(month)

# check no. is even or devisible by 3
ns = [1, 6, 2, 7, 9, 11, 3, 4]
for n in ns:
    if n % 2 == 0 and n % 3 == 0:
        print(f'Number {n} is even or divisible by 3')
    elif n % 3 == 0:
        print(f'Number {n} is divisible by 3 but not even')
    elif n % 2 == 0:
        print(f'Number {n} is even but not divisible by 3')

str= "ajay"
print("".join(reversed(str)))