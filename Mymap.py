def myMap(c, f):
    c_t = []
    for e in c:
        c_t.append(f(e))
    return c_t

l = list(range(1, 10))
print(myMap(l, lambda e: e * e))
