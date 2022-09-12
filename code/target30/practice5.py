#primary no

count=0
l=[]
for n in range(2,100):
    if(count<15):
        for i in range(2,round(n/2)+1):
            if(n%i==0):
                break

        else:
            l.append(n)
            count+=1
print(l)

# no of digit
num =12345
cnt=0
while(num>0):
    num=num/10
    cnt=+1

print(cnt)

#revrse no
num=123546
rno=0
while(num>0):
    n=num%10
    rno=rno*10 + n
    num=num//10

print(rno)

num=31
flag=True
for i in range(2,round(num/2)+1):
    if(num%i==0):
        flag=False

if(flag==True):
    print(f"{num } is prime number")
else:
    print(f"{num} is not prime number")

st="paras"
r=""
for i in st:
    r=i + r

print(r)

print(st[::-1])
print("".join(reversed(st)))

