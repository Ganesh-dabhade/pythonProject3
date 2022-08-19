i = int(input("Enter an integer: "))
# Regular if else
if i % 2 == 0:
    print("even")
else:
    print("odd")

# Ternary Operator
print("even") if i % 2 == 0 else print("odd")

# if_elif_else
if i == 0:
    print(f"i is 0")
elif i % 2 == 0:
    print(f"{i} is even")
else:
    print(f"{i} is odd")
print("even or divisible by 3")
if i % 2 == 0 or i % 3 == 0:
    print(f'Number {i} is even or divisible by 3')


