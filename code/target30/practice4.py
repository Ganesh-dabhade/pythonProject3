
l=[]
count=0

for n in range(2,100):
    if(count<15):
        for i in range(2,round(n/2)+1):
            if(n%i==0):
                break

        else:
            l.append(n)

print(l)

num=1234
cn=0
while(num>0):
    num=num//10
    cn+=1

print(cn)

# revrse number

num=3214
rno=0
while(num>0):
    n=num%10
    rno=rno*10 + n
    num=num//10

print(rno)

#fibonacci series
a=0
b=1
ct=0
p=[]
while(ct<15):
    p.append(a)
    c=a+b
    a=b
    b=c

print(p)