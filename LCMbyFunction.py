def calculate_lcm(a, b):
    x = a
    y = b

    while b != 0:
        a, b = b, a % b

    gcd = a

    lcm = abs(x * y) // gcd

    return lcm


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = calculate_lcm(num1, num2)

print("LCM =", result)
