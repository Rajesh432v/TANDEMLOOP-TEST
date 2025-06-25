user_input = input("Enter a list of numbers separated by commas: ")
numbers = list(map(int, user_input.split(',')))
multiples_count = {i: 0 for i in range(1, 10)}
for i in range(1, 10):
    for num in numbers:
        if num % i == 0:
            multiples_count[i] += 1
print("Output:")
print(multiples_count)
