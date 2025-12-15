numbers = [1, 2, 3]
n = len(numbers)

if n == 0:
    result = [[], []]
elif n % 2 == 0:
    half = n // 2
    result = [numbers[:half], numbers[half:]]
else:
    half = n // 2 + 1
    result = [numbers[:half], numbers[half:]]

print(result)
