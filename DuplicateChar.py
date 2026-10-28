text = input("Enter a string: ")

for char in set(text):
    if text.count(char) > 1:
        print(char, "appears", text.count(char), "times")
