dict = {}
print(type(dict))

set = set()
print(type(set))

dict = {"key1": 12, "key2": True, "key3": [1, 2, 3], ("key3", 7): [1.2], -8: 3}
print(type(dict))

print(dict)
print(dict.keys())
print(dict.values())

print(dict[-8])
print(dict.get("key1"))

print("key3" in dict)

print(dict.items())

dict.pop("key2")
print(dict)

dict.popitem()
print(dict)

dict["key2"] = False
dict["key4"] = True
dict.update({3:'a', -1.4:123})
print(dict)

dict.clear()