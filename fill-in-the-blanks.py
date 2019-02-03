# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

#sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
#adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
#don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
#tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?


#################################################################################################


import time
from time import sleep

blanks = ["__1__","__2__","__3__", "__4__"] #these are the blanks in the paragraphs for which answers must be provided.


questions_easy = '''I am happy to __1__ with you today in what will go down in __2__ as the greatest __3__ for freedom in the history of our __4__.\n\n'''



questions_medium = '''This will be the day, this will be the day when all of Gods __1__ (Yes, Yeah) will be able to sing with new meaning: My __2__, tis of thee (Yeah, Yes), sweet land of liberty, of thee I sing. (Oh yes) Land where my __3__ died, land of the pilgrims pride (Yeah), from every __4__, let freedom ring! (Yeah)\n\n'''



questions_hard = '''And when this happens [applause] (Let it ring, Let it ring), and when we allow __1__ ring (Let it ring), when we let it ring from every __2__ and every hamlet, from every state and every city (Yes Lord), we will be able to speed up that day when all of Gods children (Yeah), black men (Yeah) and white men (Yeah), Jews and Gentiles, Protestants and Catholics (Yes), will be able to join hands and sing in the words of the old Negro spiritual: __3__ at last! (Yes) Free at last! Thank God Almighty, we are free at __4__!\n\n'''

answers_list_easy = ["join", "history", "demonstration", "nation"]
answers_list_medium = ["children", "country", "fathers", "mountainside"]
answers_list_hard = ["freedom", "village", "Free", "last"]


game_data = {#based on the user input, this will return feedback to the user after making difficulty level.
   'easy': {
        'quiz': questions_easy,
        'answers': answers_list_easy,
        'message': "\nYou chose easy.\n"
    },
   'medium': {
        'quiz': questions_medium,
        'answers': answers_list_medium,
        'message': "\nYou chose medium.\n"
    },
   'hard': {
        'quiz': questions_hard,
        'answers': answers_list_hard,
        'message': "\nYou chose hard.\n"
    }
}


def get_level(): #this function will ask the user to select a difficulty level and will provide feedback base onthe selection.
    pick_level = raw_input("Please select a difficulty level.\n\nPossible choices include easy, medium or hard.\n\n")
    while pick_level not in ["easy", "medium", "hard"]:
        pick_level = raw_input("\nInvalid input, please try again. Choose from easy, medium or hard\n\n")
    print game_data[pick_level]['message']
    return pick_level


def check_answer(user_answer, answers_list, answers_index):#this will check if the answer provided by user is correct or incorrect and provide feedback.
    if user_answer == answers_list[answers_index]:
        return "right_answer"
    return "Wrong"
    pass

def you_lost():
    print "\n\nYou've lost :(\n\nTry again. Good Bye."
    time.sleep (3)
def you_win():
    print "You win!! \n\n\nThank you for playing. Good Bye.\n\n\n\n"
    time.sleep (3)



def play_game():
    level = get_level()
    quiz = game_data[level]['quiz']
    print quiz
    answers_list =  game_data[level]['answers']
    blanks_index = 0
    answers_index = 0
    guesses = 3

    while blanks_index < len(blanks):
        user_answer = raw_input("Please type the answer to the question " + blanks[blanks_index] + ": ")
        if check_answer(user_answer,answers_list,answers_index) == "right_answer":
            print "\n  Great, that is the right answer!\n"
            quiz = quiz.replace(blanks[blanks_index], user_answer.upper())
            blanks_index += 1
            answers_index += 1
            guesses = 3
            print quiz
            if blanks_index == len(blanks):
                return you_win()

        else:
            guesses -= 1
            if guesses == 0:
                return you_lost()
                break
            print "\n\nWrong!! Please try again. you have " + str (guesses) + " guesses left!\n\n"




play_game()
