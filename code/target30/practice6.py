num=10
flag=True
for i in range(2,round(num/2)+1):
    if(num%i==0):
        flag=False

if(flag==True):
    print(f"{num } is prime number")
else:
    print(f"{num} is not prime number")


# first 10 prime number

count=0
l=[]
for n in range(2,100):
    if(count<10):
        for i in range(2,round(n/2)+1):
            if(n%i==0):
                break
        else:
            l.append(n)
print(l)

# no of digit
num=12354
cn=0
while(num>0):
    num=num//10
    cn+=1

print(cn)

# revrse no
num=1987
rno=0
while(num>0):
    n=num%10
    rno=rno*10 + n
    num=num//10

print(rno)

#fibonacci seris
a=0
b=1
con=0
ls=[]
while(con<10):
    ls.append(a)
    c=a+b
    a=b
    b=c
    con+=1

print(ls)