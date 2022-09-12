num=int(input("enter integer number :"))
temp=num
count=0
while(num>0):
    count+=1
    num=num//10

print(f"number of digit in num {temp} is {count}")


# convert list to string
l=['H','e','l','l','o']

string ="".join(l)
print(string)

#list to set
s=set(l)
print(s)

#list to tuple
t=tuple(l)
print(type(t))
print(t)