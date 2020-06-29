#Lists can store every type of data without any problem
list = ["Hi", 5, 13.7, "", None, True]

#Lists the positions from 0 to 9 separated by every two numbers
listrange = range(0,10,2)

#We add an element at the end of the list
list.append("The end")

list += ["Another end \n \n \n*******************************\n \n \n"]

print(list)

print(list[0:3])

if True or False in list:
    print("There is a boolean \n\n") 
else:
    print("There is not a boolean\n\n")


#We delete the "Hi" element on the list
if "Hi" in list:
    list.remove("Hi") 
else:
    print("There is not a greeting")


#We format the print so the items in the list appear separated by a comma on a foreach loop
for item in list:
    print(item, end= ", ")


#Challenge!!! Request an input text from the user and display it word by word separated by a line

UserText=input("Please enter the text you want (HIT ENTER TO FINISH...): ")

UserTextToList = UserText.split()

UserTextToList.sort()

for word in UserTextToList:
    print(word + "\n\n") 

