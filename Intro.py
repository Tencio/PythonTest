#Python executes all the things under the file we are importing, hen the class were we are
import First_methods

#VARIABLE DEFINITIONS
#Correct
my_variable = 8

#Incorrect
myVariable = 7

#Constants are defined 
CONSTANT = 55

#None is the NULL for Python
velocity = None

#If velocity has something
if velocity:
    print("I am fast")
else:
    print("I am not fast")

#We need to call the method using the name of the file
First_methods.salute(input("What is your name? \n \n"))
First_methods.print5() 
