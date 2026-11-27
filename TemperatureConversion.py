def celisius_to_fahrenheit(c):
    return(c*9/5) + 32
def fahrenheit_to_celsius(f):
    return (f - 32)* 5/9

print("1. Celsius to fahrenheit")
print("2. Fahrenheit to Celsius")

choise = int(input("Enter your choice: "))

if choise ==1 :
    c = float(input("Enter temperature in Celsius: "))
    result = celisius_to_fahrenheit(c)
    print("Temperature in fahrenheit: ",result)
    
elif choise == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(f)
    print("Temperature in celsius: ",result)
    
else:
    print("Invalid choise")
    