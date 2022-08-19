l = [1, 2, 3, 4,3,2]
print(l[2])
print(l[2:4])
print(l[-1])
print(l[-4:])
print(1 in l)
s=sorted(l, reverse=True)
print(s)
print(len(l))
print(type(l))
print(type(s))
# convert set
s1=set(l)
print(type(s1))
l.append(5)
l = l + [7, 8, 9, 10]
l.insert(3, 13)
l.extend([11, 12])

print("update and delete element in list")
l = [1, 2, 3, 4]
l[1] = 11
print(l)
l.remove(4)
print(l)
l.pop(2)
print(l)


