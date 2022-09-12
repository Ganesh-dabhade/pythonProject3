#factor of number

num=30;
a=[]
for i in range(1,round(num/2)+1):
    if(num%i==0):
        a.append(i)

print(a)