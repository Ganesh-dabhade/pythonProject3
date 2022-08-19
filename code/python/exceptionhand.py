a=10;
b=0;

try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("We cannot divide by zero")
    