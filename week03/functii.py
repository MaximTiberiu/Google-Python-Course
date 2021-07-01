# def my_function(a, b, c):
#     # blocul functiei
#     # pass
#     return a + b + c
#
#
# # variabila = my_function(1, 2)
# variabila = my_function(a=1, b=2, c=3)
# variabila2 = my_function(1, 2, c=3)
# print(variabila)
# print(variabila2)
#
# # -- functie cu parametri default --
#
#
# def my_default_function(a, b, c=3):
#     """
#     Documentatie functie ;)
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     """
#     return a + b + c
#
#
# variabila3 = my_default_function(1, 2)
# print(variabila3)
#
#
# def my_int_function(a: int, b: int, c: int = 2) -> (int, int):
#     return a + b + c, a - b - c
#
#
# adunare, scadare = my_int_function(10, 1)
# # adunare, scadare = my_int_function('1', 1) - GRESEALA
# print(adunare, scadare)

my_var = input("Numar intreg: ")
try:
    my_int = int(my_var)
    # print(varvar) # NameError
except ValueError:
    print("Eroare de valoare")
except NameError:
    print("Eroare de denumire variabila")
except Exception as e:
    print("Exceptie generica: ", e)
else:
    print("Daca nu apare exceptia. ", my_int)
finally:
    print("Afiseaza in orice caz")
