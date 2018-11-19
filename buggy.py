#this code had a bug, line 8 had statement if answer instead of int(answer) to make interger to correctly identify error

import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print('What is ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
if int(answer) == number1 + number2:
    print('Correct!')
else:
    print('Nope! The asnwer is ' + str(number1 + number2))
    
