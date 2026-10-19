text = input("Enter a string: ")

reverse = text[::-1]

if text == reverse:
    print("It is a palindrome string")
else:
    print("It is not a palindrome string")
