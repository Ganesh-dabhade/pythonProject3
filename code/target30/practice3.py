# prime number
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

# fibonaci seris

a=0
b=1
ls=[]
cnt=0
while(cnt<10):
    ls.append(a)
    c=a+b
    a=b
    b=c
    cnt+=1

print(ls)

# count no of digit
num=1234
ct=0
while(num>0):
    num=num//10
    ct+=1
print(ct)

# reverse no
num=1234
rno=0
while(num>0):
    n=num%10
    rno=rno*10 + n
    num=num//10

print(rno)

# revrse String

st="avinash"
print(st[::-1])
rst=""
for i in st:
    rst= i + rst

print(rst)

print(''.join(reversed(st)))