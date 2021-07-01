# def adunare(param_1, param_2, *args):
#     # print(args)
#     suma = param_1 + param_2
#     for iter in args:
#         suma += iter
#     return suma
#
#
# def my_function(param_1, param_2, **kwargs):
#     print(kwargs)
#     print(kwargs.values)
#
#     suma = param_1 + param_2
#     for num in kwargs.values():
#         suma += int(num)
#     return suma
#
#
# rezultat = adunare(1, 2, 3, 4)
# print(rezultat)
#
# rezultat = my_function(1, 2, b=3, a=4)
# print(rezultat)


# def suma(*args):
#     # suma_lista = []
#     # for item in args:
#     #     suma_lista.append(item)
#     suma_lista = [item for item in args if item > 2]  # se poate scrie si sub aceasta forma
#     return suma_lista
#
#
# res = suma(1, 2, 3, 4)
# print(res)


# operatorul ternar

# a = 1
# b = 2
# if a < b:
#     minim = a
# else:
#     minim = b
#
# var = a if a < b else b
# print(var)

# lista = [x ** 2 for x in range(10)]
# print(lista)
# lista_duplicat = []
# for x in lista:
#     if x < 36:
#         x += 1
#     else:
#         x = x * 1000
#     lista_duplicat.append(x)
# print(lista_duplicat)
#
# lista_duplicat = [x + 1 if x < 36 else x * 1000 for x in lista]
# print(lista_duplicat)
#
# lista_duplicat = [y if int(y) > 2 else int(y) + 1 for x in lista for y in str(x)]
# print(lista_duplicat)

# def functie_lambda(x, y):
#     return x - y

# functie_lambda = lambda x, y: x - y
# print(functie_lambda(2, 3))

jucatori = [
    {'nume': 'Ion', 'prenume': 'Vasile', 'nivel': 2, 'varsta': 21},
    {'nume': 'Gheorghe', 'prenume': 'Maria', 'nivel': 1, 'varsta': 24},
    {'nume': 'Vladescu', 'prenume': 'Crina', 'nivel': 1, 'varsta': 22}
]

sortati = sorted(jucatori, key=lambda jucator: (jucator['nivel'], jucator['varsta']))
print(sortati)
