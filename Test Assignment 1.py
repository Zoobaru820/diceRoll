import random

username = input("Enter Your Name:")                                       #flavor text
print ("Welcome:" + username)

numberSides= input (username + ", how many sides do you want on your die?")#Defining # of sides
print (numberSides + " sided die, okay.")

numberRolls= input ("And how many times do you want to roll your die?")    #Defining # of rolls
print (numberRolls + " times, okay.")

for rolls in range (int(numberRolls)):                                     #Taking the users input and printing
    randomDice=random.randrange(int(numberSides))+1
    print (randomDice)

    if randomDice==int(numberSides):
        print ("Critical Hit!")                                           #Defining Critical Hit

    elif randomDice==1:
        print ("Criticl Fail!")                                           #Defining Critical Fail

print ("Hope you enjoyed your rolls. Bye bye!")

#Sources:
#https://stackoverflow.com/questions/44008489/dice-rolling-simulator-in-python
#https://www.w3schools.com/python/ref_func_input.asp
#https://www.w3schools.com/python/python_user_input.asp




