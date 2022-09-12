num=int(input("enter ineger number :" ))
temp=num
re_no=0
while(num>0) :
    r=num%10
    re_no=re_no*10 + r #no=123 logic 0+3 =3,3*10+2=32,32*10+1=321
    num=num//10

print(f"orignal no: {temp} and revrse no is {re_no}")