"""
Michael Lillis
CIS256
US State Capitals Quiz
"""

import random

#Functions
def main():
    setupGame()
    playGame()

def setupGame():
    global states, capitals, correct, incorrect, used #declare globals to be used in other parts of program
    correct = 0 #keep track of correct responses
    incorrect = 0 #keep track of incorrect responses
    used = [False] * 50 #keep track of whether we already asked that question
    states = populateStatesList() #fill list using function
    capitals = populateDict() #fill dict using function

def playGame():
    global correct, incorrect, used
    guess = ""
    while guess.lower() != "quit": #gameplay loop ends by typing quit
        index = random.randint(0, len(states) - 1) #random index out of states list
        while used[index]: #while the value inside the list is True
            index = random.randint(0, len(states) - 1) #pick an index for a question we havent asked
        used[index] = True #update list to true before asking question
        allTrue = True
        for i in range(0, 50): 
            if used[i] == False:
                allTrue = False
        if allTrue: #if all questions have been asked, reset the game
            used = [False] * 50
        state = states[index] #grab state using random index
        capital = capitals[state] #grab capital out of dict using matching state
        guess = input("What is the capital of " + state.upper() + "? (enter 'quit' to end): ")
        if guess.lower() == "quit": #check for sentinel
            print("THANKS FOR PLAYING...You got " + str(correct) + " of " + str(correct + incorrect) + " correct.")
            break
        elif guess.lower() == capital.lower(): #correct response
            print("That is CORRECT!" + capital + " is the capital of " + state + ".")
            correct += 1
        else: #incorrect response
            print("SORRY...the capital of " + state + " is " + capital + ".")
            incorrect += 1
        print("YOUR SCORE: You have gotten " + str(correct) + " of " + str(correct + incorrect) + " correct.")
    

#List of states
def populateStatesList():
    return ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut',
            'Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa',
            'Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan',
            'Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada',
            'New Hampshire','New Jersey','New Mexico','New York','North Carolina',
            'North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island',
            'South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia',
            'Washington','West Virginia','Wisconsin','Wyoming']

#dictionary of states:capitals 
def populateDict():
    return {'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix','Arkansas':'Little Rock',
            'California':'Sacramento','Colorado':'Denver','Connecticut':'Hartford',
            'Delaware':'Dover','Florida':'Tallahassee','Georgia':'Atlanta','Hawaii':'Honolulu',
            'Idaho':'Boise','Illinois':'Springfield','Indiana':'Indianapolis','Iowa':'Des Moines',
            'Kansas':'Topeka','Kentucky':'Frankfort','Louisiana':'Baton Rouge','Maine':'Augusta',
            'Maryland':'Annapolis','Massachusetts':'Boston','Michigan':'Lansing',
            'Minnesota':'St. Paul','Mississippi':'Jackson','Missouri':'Jefferson City',
            'Montana':'Helena','Nebraska':'Lincoln','Nevada':'Carson City','New Hampshire':'Concord',
            'New Jersey':'Trenton','New Mexico':'Santa Fe','New York':'Albany',
            'North Carolina':'Raleigh','North Dakota':'Bismarck','Ohio':'Columbus',
            'Oklahoma':'Oklahoma City','Oregon':'Salem','Pennsylvania':'Harrisburg',
            'Rhode Island':'Providence','South Carolina':'Columbia','South Dakota':'Pierre',
            'Tennessee':'Nashville','Texas':'Austin','Utah':'Salt Lake City','Vermont':'Montpelier',
            'Virginia':'Richmond','Washington':'Olympia','West Virginia':'Charleston',
            'Wisconsin':'Madison','Wyoming':'Cheyenne'}

#Run game
main()
