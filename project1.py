# (5 points): As a developer, I want to make at least three commits with descriptive messages
# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 




from __future__ import print_function
from ast import FloorDiv
from multiprocessing.connection import answer_challenge
from pickle import TRUE
import random
from tkinter.messagebox import YES


destination = ["Peru", "China", "Ghana", "England"]
resturant = ["Los Amigos", "Wine 30", "Ruth Chris", "PF Changs"]
mode_of_transport = ["by Foot", " by Public Transportation", "by Car", " by Plane"]
entertainment = ["a Movie Night", "Clubing/Partying", "Jet Skiing", "Dancing"]
answer = "Yes"
can_continue = True

# # (5 points): As a user, I want a destination to be randomly selected for my day trip.



def place_to_go():
    
    while can_continue is True:
        location = random.choice(destination)
        print(location)

        user_input = input("Do you like this choice? Please answer 'Yes' or 'No'")
        if user_input == answer:
            print("Great")
            print("Let's see where you'll be dining.")
            return location
        else:
            print("Okay! Let's try this again")




user_destination = place_to_go()


# # # #(5 points): As a user, I want a restaurant to be randomly selected for my day trip

def where_to_eat():

    while can_continue is True:
        Food = random.choice(resturant)
        print("Enjoy dining at " +random.choice(resturant)+"!")
        user_input = input("Do you like this choice? Please answer 'Yes' or 'No'")
        if user_input == answer:
             print("Great")
             print("Enjoy")
             return Food
        else:
             print("No worries. Let's try this again")
             


user_resturant = where_to_eat()


# # # # (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 

def how_to_get_there():

    while can_continue is True:
        transport = random.choice(mode_of_transport)
        print("Your primary mode of transportation,while on this trip, will be "+ random.choice(mode_of_transport))
        user_input = input("Is this an acceptable option?")
        if user_input == answer:
            print("Awesome")
            print("Travel Safe")
            return transport
        else:
            print("Okay. Let's find another option.")

user_means_of_transport = how_to_get_there()


# # # # (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.


def what_to_do():
    while can_continue is True:
        fun = random.choice(entertainment)
        print("If you ever get bored, try "+ random.choice(entertainment)+" with friends")
        user_input = input("Is this cool?")
        if user_input == answer:
            print("Cool")
            print("Have fun")
            return fun
        else:
            print("No problem. Let's find somethig else to do")


user_activity = what_to_do()

# # (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.
# # The functions above have been modified to fit this prompt.

# # (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

def all_together():
    print("You will be to " + user_destination)
    print("You will be dining at "+ user_resturant)
    print("Your primary road of transportation will be "+ user_means_of_transport)
    print("If you ever get bored, try "+ user_activity)

final_step = all_together()
print("Complete")
    

    

# def where_to_go(something):
#     loca =  print("Are you hapy with this choice?")
