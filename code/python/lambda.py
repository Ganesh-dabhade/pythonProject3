# lambda functions

def my_sum(lb, ub, f):
    total = 0
    for i in range(lb, ub + 1):
        total += f(i)
    return total

print(my_sum(5, 10, lambda n: n * n))

print(my_sum(5, 10, lambda n: n * n * n))

print(my_sum(5, 10, lambda n: n if n % 2 == 0 else 0))

# l=["hello world", 'jay ganesh']
# filter(l, lambda a:a.split(" ")[1])

