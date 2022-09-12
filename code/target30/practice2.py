l=[]
count=0
for n in range(2,100):
    if(count<15):
        for i in range(2,round(n/2)+1):
            if(n%i==0):
                break

        else:
            l.append(n)
            count+=1

print(l)

num=12
flag=True
for i in range(2,round(num/2)+1):
    if (num%i==0):
        flag=False

if(flag== True):
    print(f"{num } is prime number")
else:
    print(f"{num} is not prime number")

# revrse number
num=1234
rno=0
while(num>0):
    n=num%10
    rno=rno*10 +n
    num=num//10

print(rno)

# no of digit

n=1234
cou=0
while(n>0):
    n=n//10
    cou+=1

print(cou)

#fibonacci series
a=0
b=1
cont=0
ls=[]
while(cont<10):
    ls.append(a)
    c=a+b
    a=b
    b=c
    cont+=1

print(ls)

#reverse string

st="pavsn"
rst=""

for i in st:
    rst=i +rst

print(rst)

print(st[::-1])

print("".join(reversed(st)))


