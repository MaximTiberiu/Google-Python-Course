my_list = [8, 2, -3, 6.2, 20, "s", 2, True]

print(my_list[2])
print(my_list[-1])

print(len(my_list))

my_list.append("element adaugat")
print(my_list)

my_list.insert(2, False)
print(my_list)

print(my_list[3:])
print(my_list[0:5])
print(my_list[:-3])
print(my_list[3:8:2])

list = [8, 2, 2, 2, 2, [3, 2, 4], [True, [1, True, '3']]]
print(list[-1][-1][-1])

list.append('4')
print(list)

print(list[3][1][2])

list.remove(2)
print(list)

list.pop()
print(list)

list.pop(3)
print(list)

list.clear()
print(list)

list1 = [0, 1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9]
list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)

list1 = [8, 2, 2, 4, 5]
print(set(list1))
