for i in range(10):
    print(f"Set instructiuni {i}")

for i in range(1, 10):
    print(f"Set instructiuni {i}")

for i in "abecedar":
    print(i)

dict = {1: 3, 4: 5, 6: 7}
for key, value in dict.items():
    print(key, value)


lista = [1, 2, 4]
for i, val in enumerate(lista):
    print(f"lista[{i}] = {val}")

new_list = [(i, v) for i, v in enumerate(lista)]
print(new_list)

