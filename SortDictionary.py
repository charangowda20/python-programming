my_dict = {
    "Apple": 50,
    "Banana": 20,
    "Mango": 40,
    "Orange": 30
}

sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))

print("Sorted dictionary:", sorted_dict)
