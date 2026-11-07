numbers = [10, 50, 30, 40, 20]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second largest:", unique_numbers[-2])
else:
    print("Second largest element does not exist")
