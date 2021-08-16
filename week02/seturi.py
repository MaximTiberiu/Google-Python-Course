set1 = {}
print(type(set1))

set1 = {"item1", 2, True, True}
print(set1)

a = {4, 0, 2, 3}
b = {1, 2, 3, 4, 5}
print(a | b) # uniune
print(a & b) # intersectie
print(b & a) # intersectie
print(a - b) # diferenta
print(b - a) # diferenta