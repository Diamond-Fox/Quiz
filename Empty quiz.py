#-----------------
# Little quiz
# This is little Quiz, made in 2023 by Alexis.D AKA Aldbg74
#
# French enthousiast dev
#
# This is a Quiz python program (Oh what a suprise, i guess you didn't know it isn't it ?)
# You have serval questions made by me (i'm a men of culture as well)
# You need to answer to all of it to have your final score
# A good answer give you a point a wrong answer give you nothing (yeah i know it's so difficult to understand you need long studies for it guess sorry not sorry ?)
#
# You can modify the files to make your own questions.
# Not gonna explain you how to do it's easy as least you can read (So if you reading me it's ok u can do it, i belive in you)
#
#Alexis.D
#2023
#-----------------

#-----------------

def new_game():

    guesses =[]
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("--------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)
            
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
        
        
    display_score(correct_guesses, guess)
    
#-----------------

def check_answer(answer, guess):
    
    if answer == guess:
        print(" CORRECT ! ")
        return 1
    else:
        print("WRONG")
        return 0
    
#-----------------

def display_score(correct_guesses, guesses):
    print("--------------------")
    print(" RESULTS ")
    print("--------------------")
    
    print("Answers: ", end = "")
    for i in questions:
        print(questions.get(i), end="")
    print()
    
    print("guesses: ", end = "")
    for i in guesses:
        print(i, end="")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print("You have a score of :"+str(score)+"%")
    
#-----------------

def play_again():
    reponse = input("Do you want to play or play again ? (y or n) :")
    
    if reponse == "y":
        return True
    else:
        return False
        
#-----------------

questions = {
# "question" : "A/B/C",

 }

#-----------------

options = [["A. ", "B. ", "C."],
["A. ", "B.", "C. A"]]

#-----------------

new_game

while play_again():
    new_game()
    
print ("Bye")

#-----------------

#The end

#Play the gitar like young satana

# TO BE ADDED (Maybe)

# random.randint for the questions
# More questions
# MORE questions
