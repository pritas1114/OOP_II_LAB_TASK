# -*- coding: utf-8 -*-
"""lab_3Task_2.py

Use Colab.

Original file is located at
    https://colab.research.google.com/drive/1rL50iAXKXlMdZMVClkirWHxBCNoR6wee
"""

# lab 03 // task 02
employee = {
    "Name": "A",
    "age": 40,
    "type": {"Developer": ["ios", "android"]},
    "Parameter": True,
    "Salary": 30000,
    100: (1, 2, 3),
    4.5: {5, 6, True, 7 ,1}
}


print(len(employee), type(employee))


a = employee["type"]["Developer"]
print(a)
b = employee[4.5]
print(b)


employee["Parameter"] = False


employee["gender"] = "male"


del employee["age"]


print("Keys:")
for key in employee.keys():
    print(key)


print("\nValues:")
for value in employee.values():
    print(value)


print("\nItems:")
for key, value in employee.items():
    print(f"{key}: {value}")
