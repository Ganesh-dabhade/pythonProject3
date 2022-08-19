# passing function as argument;

def my_sum(lb, ub, f):
    total = 0
    for e in range(lb, ub + 1):
        total += f(e)
    return total


def sqr(n): return n * n

def cube(n): return n * n * n

print(my_sum(5, 10, sqr))
print(my_sum(5, 10, cube))