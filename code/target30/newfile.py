# prime number -> A  number that can be divided exactly only by itself and 1;
l=[]
count=0;
#flag=False
for i in range(2,100):
    if count<15:
        for n in range(2,i):
            if(i%n==0):
                break

        else:
            l.append(i)
            count+=1
    else:
        break


print(l)



