# prime number
# count=0
# l=[]
# for n in range(2,100):
#     if count<20:
#         for i in range(2,round(n/2)+1):
#             if(n%i == 0):
#               break;
#
#         else:
#            l.append(n)
#            count+=1
#
# print(l)

# count number of digits in number
# num=int(input("enter number"))
# count=0
# while(num>0):
#     num=num//10;
#     count+=1
#
#
# print(count)

# reverse number
# rnumber=0
# num=1234
# while(num>0):
#     n=num%10
#     rnumber=rnumber*10 + n
#     num=num//10
#
# print(rnumber)
#
# #prime no not
#
# num=41
# flag=True
# for i in range(2,round(num/2)+1):
#     if(num%i==0):
#         flag=False
#
# if (flag==True):
#     print(f"{num} is prime number")
# else:
#     print(f"{num} is not prime number")
#
# # reverse string for loop
# string="sham"
# rstr=""
# for i in string:
#     rstr=i + rstr
#
# print(rstr)

# using slice operator
p="aman"

print(p[::-1])
# revrsed string method
print("".join(reversed(p)))

# convert list to string
list=['h','e','l','l','o']

print("".join(list))
type("".join(list))

print(tuple(list))
type(tuple(list))

print(set(list))
type(set(list))

# fibonacci seris

a=0
b=1
count=0
l=[]
while(count<15):
    l.append(a)
    c=a+b
    a=b
    b=c
    count+=1

print(l )



