#I am assigning to a key (1, 2, 3, 4, 5, 6, 7, 8)
dic = {1:'mercury', 2: 'venus', 3:'earth', 4: 'mars', 5: 'jupiter', 6:'saturn', 7:'uranus', 8:'neptune'}

#Assigning a int to a string key
dic2 = {'monday':1, 'tuesday':2, 'wednesday':3}

dic[9] = 'pluto'

#Prints earth
print(dic[3])

#prints the int value assigned to the 'Tuesday' key
print(dic2['tuesday'])

#Challenge!!! How many times a word appears on a phrase?

challenge_variable = "Si el caracol tuviera cara como tiene el caracol fuera cara fuera col fuera caracol con cara"
dic_challenge={}

challenge_variable = challenge_variable.lower()

for i in challenge_variable.split():
    if i in dic_challenge:
        dic_challenge[i] += 1
    else:
        dic_challenge[i] = 1
    
print(dic_challenge)