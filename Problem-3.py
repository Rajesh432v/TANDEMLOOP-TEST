a = int(input("Enter a number: "))
count = a if a % 2 != 0 else a - 1
odd_numbers = [str(2 * i + 1) for i in range(count)]
print(", ".join(odd_numbers))
