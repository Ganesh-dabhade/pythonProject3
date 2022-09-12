#palindrome number 12321 12312 rev no is same
l=[]

for num in range(10,101):
    temp=num
    rno = 0
    while(num>0):
        n = num % 10
        rno = rno * 10 + n
        num = num // 10
    if (temp == rno):
        #print(F"{temp}is palindrom number")
        l.append(temp)
print(l)
