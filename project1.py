# (5 points): As a developer, I want to make at least three commits with descriptive messages
# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 




import random


destination = ["Peru", "China", "Ghana", "England"]
resturant = ["Los Amigos", "Wine 30", "Ruth Chris", "PF Changs"]
mode_of_transport = ["by Foot", " by Public Transportation", "by Car", " by Plane"]
entertainment = ["a Movie Night", "Clubing/Partying", "Jet Skiing", "Dancing"]


# (5 points): As a user, I want a destination to be randomly selected for my day trip.

def place_to_go():
    print("You will be going to " +random.choice(destination)+"!!")

user_destination = place_to_go()


#(5 points): As a user, I want a restaurant to be randomly selected for my day trip

def where_to_eat():
    print("Enjoy dining at " +random.choice(resturant)+"!")

user_resturant = where_to_eat()


# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 

def how_to_get_there():
    print("Your primary mode of transportation,while on this trip, will be "+ random.choice(mode_of_transport))

user_means_of_transport = how_to_get_there()


# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.


def what_to_do():
    print("If you ever get bored, try "+ random.choice(entertainment)+" with friends")

user_activity = what_to_do()



