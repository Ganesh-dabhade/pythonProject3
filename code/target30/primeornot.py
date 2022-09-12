# check prime number or not
num=int(input("enter integer num"))
flag=True
for n in range(2,num):
    if(num%n==0):
        flag=False

if(flag == False):
    print(f"{num} given num is not prime number")
else:
    print(f"{num} given number is prime number")