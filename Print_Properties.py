rocket = "Saturn V"

#Obtains the length for rocket
print(len(rocket))

#Displays the type of the variable (what it currently is)
print(type(rocket))

#Prints from the 3rd(0, 1, 2) character to the end
print(rocket[2:len(rocket)])
print (rocket[2:])

#Prints all the variable
print(rocket[:])

#Prints until the character number 8
print(rocket[:7])

#Prints in lower letters
print(rocket.lower())

#Prints the first character in capital letters
print(rocket.capitalize())

#Prints all the characters in capital letters
print(rocket.upper())

#Prints rocket's content 5 times
print(rocket*5)

#Concatenate Strings
print("Hello rocket {0}, {1}".format("Saturn V","Falcon 7"))

print(f"Hello {rocket}")

print("Hello "+rocket)

print("Hello %s" % "Falcon 7")

#Challenge: Divide a plain String and count how many words it has

ChallengeString = "Caleb Jingyi Isa Kevin Kenneth"

print(len(ChallengeString.split()))