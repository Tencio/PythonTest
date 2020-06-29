import random

#displays a random number between 1 and 149
random_range = random.randrange(1,150)

#Challenge!!! Create a script that displays how many times a dice number got selected on a random based number 100 times

number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0
number6 = 0


#The continue makes the compiler go back to the loop without evaluating the othe conditions once one o them is true. It is like a break.
for i in range(100):
    Dice = random.randrange(1,7)
    if Dice == 1:
        number1 += 1
        continue
    elif Dice == 2:
        number2 += 1
        continue
    elif Dice == 3:
        number3 += 1
        continue
    elif Dice == 4:
        number4 += 1
        continue
    elif Dice == 5:
        number5 += 1
        continue
    elif Dice == 6:
        number6 += 1
        continue

print("The number 1 was choosen %d times \n" % (number1))       
print("The number 2 was choosen %d times \n" % (number2))
print("The number 3 was choosen %d times \n" % (number3))
print("The number 4 was choosen %d times \n" % (number4))
print("The number 5 was choosen %d times \n" % (number5))
print("The number 6 was choosen %d times \n" % (number6))