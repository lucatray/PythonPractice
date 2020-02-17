# how to sort names alphabetically
names = ['jack', 'jill', 'eric', 'zack', 'andy']

(names).sort()

print(names)


import random

lottery_numbers = []

another_number = 'yes'

number1 = random.randint(0, 10)
number2 = random.randint(0, 10)
number3 = random.randint(0, 10)
number4 = random.randint(0, 10)
number5 = random.randint(0, 10)
number6 = random.randint(0, 10)
number7 = random.randint(0, 10)

while another_number == 'yes':

    lottery_numbers.append(number1)
    lottery_numbers.append(number2)
    lottery_numbers.append(number3)
    lottery_numbers.append(number4)
    lottery_numbers.append(number5)
    lottery_numbers.append(number6)
    lottery_numbers.append(number7)

    another_number = str(input('Would you like another ticket (yes or no): '))

    print('The lottery numbers are: ', lottery_numbers)



list = []

list += lottery_numbers

print(list)