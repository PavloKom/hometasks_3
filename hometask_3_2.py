numbers = [1, 2, 3]
if len(numbers) >= 1:
    numbers = [numbers[-1]] + numbers[:-1]
print(numbers)