# (5 points): As a developer, I want to make at least three commits with descriptive messages
# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 




import random


destination = ["Peru", "China", "Ghana", "England"]
resturant = ["Los Amigos", "Wine 30", "Seafood", "Vegan"]
mode_of_transport = ["Foot", "Bicycle", "Car", "Plane"]
entertainment = ["Movie Night", "Clubing/Partying", "Jet Skiing", "Dancing"]


# (5 points): As a user, I want a destination to be randomly selected for my day trip.

def place_to_go():
    print("You will be going to " +random.choice(destination))

user_destination = place_to_go()


#(5 points): As a user, I want a restaurant to be randomly selected for my day trip

def where_to_eat():
    print("Enjoy dining at " +random.choice(resturant))

user_resturant = where_to_eat()




