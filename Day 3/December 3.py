import numpy as np

with open('inputDec3.txt', 'r') as f:
    lines = f.readlines()
    numbers = []
    for number in lines:
        numbers.append(number.strip('"\n"'))


def countValues(numbers):
    oneCount = np.zeros(12)
    zeroCount = np.zeros(12)
    for binary in numbers:
        for i, digit in enumerate(binary):
            if int(digit) == 0:
                zeroCount[i] += 1
            else:
                oneCount[i] += 1
    return zeroCount, oneCount

zeroCount, oneCount = countValues(numbers)
gamma = '000010110001'
epsilon = '111101001110'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma*epsilon)



# Part 2
# Keep only the binary number that has a majority of digits
numbersBad = numbers.copy()


def countPopDigit(numbers, zeroCount, oneCount, index):
    legalNumbers = []
    for number in numbers:
        if zeroCount[index] > oneCount[index]:
            if int(number[index]) == 0:
                legalNumbers.append(number)
        elif zeroCount[index] < oneCount[index]:
            if int(number[index]) == 1:
                legalNumbers.append(number)
        else:
            if int(number[index]) == 1:
                legalNumbers.append(number)
    return legalNumbers


def countNotPopDigit(numbers, zeroCount, oneCount, index):
    legalNumbers = []
    for number in numbers:
        if zeroCount[index] < oneCount[index]:
            if int(number[index]) == 0:
                legalNumbers.append(number)
        elif zeroCount[index] > oneCount[index]:
            if int(number[index]) == 1:
                legalNumbers.append(number)
        else:
            if int(number[index]) == 0:
                legalNumbers.append(number)
    return legalNumbers


for i in range(len(numbers[0])):
    zeroCount, oneCount = countValues(numbers)
    numbersCheck = countPopDigit(numbers, zeroCount, oneCount, i)
    if not numbersCheck:
        break
    elif numbersCheck:
        numbers = numbersCheck

for i in range(len(numbersBad[0])):
    zeroCount, oneCount = countValues(numbersBad)
    numbersBadCheck = countNotPopDigit(numbersBad, zeroCount, oneCount, i)
    if not numbersBadCheck:
        break
    elif numbersBadCheck:
        numbersBad = numbersBadCheck

print(int(numbers[0], 2)*int(numbersBad[0], 2))