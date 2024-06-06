import os
import pprint


clear = lambda: os.system("cls")
clear()


#SECTION :      Dictionary

my_dict = {
    "langauge": "Python",
    "error": "TypeError",
    "year": 1992,
    "version": 3.12,
    1: "one",
    2.1: "two",
    #! [1, 2, 3]: "numbers"
    (1, 2, 3): "numbers",
    #! {"a": "A", "b": "B"}: "letters"
}

print(my_dict)

#NOTE:      access items
print(my_dict["langauge"])
print(my_dict["year"])
print(my_dict["version"])

print()

#NOTE:      add new item
my_dict["city"] = "Bangalore"
print(my_dict)

print()

#NOTE:      change item value

my_dict["city"] = "Delhi"
print(my_dict)

print()

#NOTE:      loop dict

#       only key will print
for i in my_dict:
    print(i)

print()

#       print both key and value
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

print()

#       key() method
for key in my_dict.keys():
    print(key)

print()

#       value() method
for value in my_dict.values():
    print(value)

print()

#       items() method - key and value
for key, value in my_dict.items():
    print(f"{key}: {value}")


print()


#SECTION :      Empty Dictionary
items = {}

print(items)
items["a"] = "A"
items["b"] = "B"
items[1] = "One"
items[(1, 2, "a")] = "Tuple Items"
print(items)


print()


#SECTION:           Nesting Dictionary

items = {
    "cities": ["Delhi", "Bangalore", "Patna"],
    "visited_country": {
        "India": ["Delhi", "Patna", "Mumbai", "Bangalore"],
        "Nepal": ["Pokhra", "Himalaya"],
        "total_visited_country": 2
    },
    
}

pprint.pp(items["visited_country"])

print()

items = [
    {"cities": ["Delhi", "Bangalore", "Patna"]},
    {"visited_country": {
        "India": ["Delhi", "Patna", "Mumbai", "Bangalore"],
        "Nepal": ["Pokhra", "Himalaya"],
        "total_visited_country": 2
    }},
]
print(items)