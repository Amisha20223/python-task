numbers = [float(x) for x in input("Enter a list of numbers separated by spaces: ").split()]

max_value = max(numbers)
min_value = min(numbers)
average = sum(numbers) / len(numbers)

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print(f"Average value: {average}")
