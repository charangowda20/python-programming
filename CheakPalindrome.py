def check_palindrome(value):
    if value == value[::-1]:
        return True
    else:
        return False


text = input("Enter a word or number: ")

if check_palindrome(text):
    print(text, "is a Palindrome")
else:
    print(text, "is Not a Palindrome")
