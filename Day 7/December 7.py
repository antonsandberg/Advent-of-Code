import numpy as np

# A
with open('inputDec7.txt', 'r') as f:
    numbers_list = f.read().strip().split(',')
    numbers = [int(number) for number in numbers_list]

test_numbers = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
numbers = np.array(numbers)
test_numbers = np.array(test_numbers)
least_fuel = float('inf')

best_number = 0
for number in range(max(numbers)+1):
    fuel = 0
    dist_numbers = np.abs(numbers - number)
    fuel = np.sum(dist_numbers)
    if fuel < least_fuel:
        best_number = number
        least_fuel = fuel

print(best_number, least_fuel)

# B
least_fuel = float('inf')
best_number = 0
for number in range(max(numbers)+1):
    fuel = 0
    fuel = np.sum(np.abs(numbers - number)*(np.abs(numbers - number)+1)/2)
    if fuel < least_fuel:
        best_number = number
        least_fuel = fuel
print(best_number, least_fuel)
