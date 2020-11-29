# Author: Joshua T Smith
# Date: 4-15-2020 

import random

# This is the main menu.
def menu():
    print(35 * '-')
    print('1. Survival Mode')
    print('2. Information About Survival Mode')
    print(35 * '-')

# This will initiate the beginning game prompt and menu. User will select game mode, or select more info.
def main():
    print('------------------------------------------------------------------------------')
    print('Welcome to The Story. The game where you decide where you go, and what you do.')
    print('')
    print('Remember. Your actions could have consiquences.')
    print('------------------------------------------------------------------------------')
    loop = True
    while loop == True:
        menu()
        select = int(input('Please select a number from the Menu: '))
        if select == 1:
            survivalPrompt()
            loop = False
        elif select == 2:
            print(60*'-')
            print('Survival Info:')
            print('The survival game mode is set in a remote forest. Your plane has crashed and now you must survive.')
            print('You must find resources such as food, water, and wood if you are to survive the woods.')
            print('You will be given prompts to search the woods for resources, or to continue through the forest.')
            print(60*'-')
        else:
            print()
            print()
            print()
            print(40*'-')
            print('Invalid selection. Please try again')
            print(40*'-')
            print()
            print()
            print()
            loop = True

# If user selects survival mode, they will be brought to the Survival Game Mode Prompt. From here they can decide if they want to
# continue, or return to the main menu to select a different game mode.
def survivalPrompt():
    # Below are values that will be used later on.
    fire = 0
    fireSet = False
    shelterSet = False
    shelter = 0
    cloth = 0
    glass = 0
    selector = 0
    wood = 0
    stamina = 5
    hunger = 100
    thirst = 100
    health = 100
    loop = True
    while loop == True: # Below is the beginning survival prompt. It will explain the game to the player.
        print(15 * '-')
        print('Survival')
        print(15 * '-')
        print('')
        print(60 * '-')
        print('Welcome to The Story, survival mode.')
        print('')
        print('You survived a plane crash, but you are now on your own in the middle of the woods.')
        print('')
        print('You wander the woods in search of food, water, or rescue.')
        print('')
        print('When looking for supplies, you will have a random chance of recieving items, not recieving items, or getting hurt.')
        print('')
        print('You will gain stamina as you progress through the story.')
        print('Use stamina to look for food, water, or wood for shelters and fires.')
        print('')
        choice = int(input('Press 1 to continue  |  Press 2 to return to main menu:  ')) # Player can choose to continue or go to the main menu
        if choice == 1:
            loop = False
            survival(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
        if choice == 2:
            loop = False
            main()
        else:
            print('Not a valid response. Please try again.')
# The info bar will tell the user what their stats are currently at, as they will continue to change throughout the game.
def infoBar(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector):
    print(80 * '-')
    print('Wood: ',wood,' |  Hunger: ',hunger,' |  Thirst: ',thirst,' |  Health: ',health,' |  Stamina: ',stamina)
    print(80 * '-')

def craftingMenu(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector):
    # This is the menu the player will go to when crafting survival items.
    print('')
    infoBar(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
    print('')
    print('------------------------CRAFTING MENU-----------------------')
    print('')
    print('1. Fire (3 wood)  |  2.  Shelter (8 wood) |  3. Back to menu')
    print('')
    print('------------------------------------------------------------')

def survival(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector): # The beginning of the main survival story
    print('')
    print('')
    infoBar(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
    loop = True
    while loop == True:
        print('')
        print('Would you like to search for resources, craft, or continue through the woods?')
        option = int(input('1. Search for resources  |  2. Craft  |  3. Continue through the woods:  '))
        if option == 1: # Search for resources
            if stamina >= 1: # If their stamina is 1 or above, they can access the resource menu
                userChoice(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
                loop = False
            if stamina < 0: # If stamina is 0, they will not be able to access the resources menu
                print('You do not have enough stamina points to do this. Please choose again.')
                stamina = 0
                survival(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
        elif option == 2: # Craft Menu
            craftingMenu(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            choice = int(input('Enter your choice:  '))
            if choice == 1: # to craft a fire
                if wood >= 3:
                    fire = 1
                    print('')
                    print('You made a fire!')
                    print('')
                if wood < 3:
                    print('Im sorry. You dont have enough wood for this')
            if choice == 2: # to craft a shelter
                if wood >= 8:
                    shelter = 1
                    print('')
                    print('You made a shelter!')
                    print('')
                if wood < 8:
                    print('Im sorry, you dont have enough wood for this')
            if choice == 3: # to go back to menu
                loop = True
        elif option == 3: # Brings Character to their designated stories
            loop = False
            if selector == 0: # This will bring the Character to the first story, about the Skeleton.
                survivalStory1(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            if selector == 1: # This will bring the Character to the second story, about finding something shiny.
                survivalStory2(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            if selector == 2:# This will bring the Character to the third story, about finding a deer.
                survivalStory3(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            if selector == 3: # This will bring the Character to the four story, giving them they option to follow the deer.
                survivalStory4(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            if selector == 60:# This will bring the Character to the alternate story, finding the lake.
                altSurvivalStory1(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            if selector == 61: # This will bring the Character to the alternate story, of ending the day.
                altSurvivalStory2(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)

        else:
            print('Not a valid response. Try again.')

def userChoice(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector):
    while  stamina > 0:
        print('')
        infoBar(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
        print(70 * '-')
        option = int(input('1 to find wood  |  2 to find food  |  3 to find water  |  4 to continue walking:  '))
        print('')
        print('Please select an option.')
        gamble = random.randint(1,3)
        if option == 1:
            stamina = stamina - 1
            print('There is a random probability that you will find wood.')
            print('')
            if gamble == 1:
                print('You found a fallen tree and recieved 3 wood')
                wood = wood + 3
            elif gamble == 2:
                print('You could not find any wood')
            elif gamble == 3:
                print('You could not find any wood, and you injured yourself in the process. You lost 10 health.')
                health = health - 10
        if option == 2:
            stamina = stamina - 1
            print('You search for food in nearby bushes')
            if gamble == 1:
                print('You found some berrys in a bush nearby. You gained 10 hunger points.')
                hunger = hunger + 10
                thirst = thirst - 5
                health = health + 5
            elif gamble == 2:
                print('You could not find any food.')
            elif gamble == 3:
                print('You could not find any food, and you injured yourself in the process. You lost 10 health.')
        if option == 3:
            stamina = stamina - 1
            print('You search for some water.')
            if gamble == 1:
                print('You found some water in a nearby creek. You gained 10 thirst points.')
            elif gamble == 2:
                print('You could not find any water.')
            elif gamble == 3:
                print('You could not find any water, and injured yourself in the process. You lost 10 health.')
        if option == 4:
            survival(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
        if stamina == 0:
            print('You are out of stamina. Please try again when you gain more stamina.')
            if selector == 0: # This will bring the Character to the first story, about the Skeleton.
                survivalStory1(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            if selector == 1: # This will bring the Character to the second story, about finding something shiny.
                survivalStory2(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            if selector == 2:# This will bring the Character to the third story, about finding a deer.
                survivalStory3(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            if selector == 3:
                survivalStory4(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            if selector == 60:# This will bring the Character to the alternate story, finding the lake.
                altSurvivalStory1(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            if selector == 61: # This will bring the Character to the alternate story, of ending the day.
                altSurvivalStory2(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
        
def survivalStory1(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector):
    print('')
    print('')
    print('You continue trekking through the woods, hoping to find a road or some other sign of civilization.')
    print('')
    print('You find a skeleton, still fully clothed. You wonder what happened to this traveler. Were they stranded like you are?')
    print('')
    loop = True
    while loop == True:
        choice = int(input('1. Take the clothes from the corpse.   |    2. Leave the corps alone.    :   '))
        if choice == 1:
            loop = False
            print('It was a trap! You narrowly missed a bear trap. The bear trap closes fast and fiercely behind you.')
            print('')
            print('It nicked your leg and hurt you. You lost some health(-10 health) but you got some cloth')
            print('')
            health = health - 10
            cloth = cloth + 1
            selector = selector + 1
            survival(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            hunger = hunger - 6
        if choice == 2:
            loop = False
            print('You ignore the deceased explorer.')
            print('')
            stamina = stamina + 1
            selector = selector + 1
            survival(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
        else:
            print('Please select a valid option.')
            print('')


def survivalStory2(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector):
    print('As you leave the corpse behind, you see a nice stump to take a break at.')
    choice = int(input('1. Take a break(gain stamina)   | 2. Keep walking  : '))
    if choice == 1:
        stamina = stamina + 1
    if choice == 2:
        print('You continue walking.')
        print('')
    print('You notice something shiny in the distance.')
    choice = int(input('1. Go to shiny object    | 2. Keep walking  :  '))
    hunger = hunger - 3
    if choice == 1:
        print('')
        print('You get closer to the object and discover its a broken piece of glass.')
        print('')
        print('You realize its sharp and could be used to cut things')
        print('')
        choice = int(input('1. Take the sharp glass    |2. Leave it alone  :  '))
        if choice == 1:
            if cloth == 1:
                print('')
                print('You take the piece of cloth you found earlier to wrap the glass as to not get hurt.')
                print('Earn 1 stamina')
                print('')
                stamina = stamina + 1
                glass = 1
                selector = selector + 1
                hunger = hunger - 5
                survival(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
            if cloth == 0:
                print('')
                print('You pick up the glass and cut yourself. Ouch! You lost some health.')
                print('')
                health = health - 10
                selector = selector + 1
                survival(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
                hunger = hunger - 5
def survivalStory3(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector):
    print('')
    print('You hear a noise in the distance. You wonder what that could be.')
    choice = int(input('1. Go torwards the sound  | 2. Continue through the woods  :  '))
    if choice == 1:
        print('')
        print('')
        print('You follow the noise and you come across a deer stuck in a trap.')
        print('A trap... You realize that these were set up by somebody. They could be nearby')
        print('As you realize this, the deer yelps in pain. You have to make a choice.')
        print('')
        choice = int(input('1. Free the deer   |2. Leave it alone, and continue through the woods   : '))
        if choice == 1:
            print('You look at the deer and you wonder how to set it free. Its held down by a weighted net with cinder blocks on all corners.')
            print('')
            print('You remember the sharp piece of glass you have. You take it out of your pocket and you begin to cut the ropes.')
            print('')
            print('You cut the last rope and the deer runs away.')
            print('')
            print('') 
            selector = 60
            survival(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
        if choice == 2:
            print('')
            print('You look back at the deer in pain, and continue through the woods.')
            print('')
            selector = 3
            stamina = stamina + 1
def altSurvivalStory1(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector):
    print('')
    print('You notice the deer left behind a trail of blood.')
    print('')
    print('You wonder where the deer could be headed...')
    print('')
    loop = True
    while loop == True:
        choice = int(input('1. Follow the trail  2. Continue through the woods :  '))
        if choice == 1:
            loop = False
            selector = 61
            hunger = hunger - 35
            print('')
            print('You follow the trail of blood.')
            print('')
            print('You trek through rough terrain, misquitos and thick brush.')
            print('')
            print('You arrive at a clearing in the woods, and you see a lake!')
            print('')
            print('')
            print('You get down to the lake, the trail ends there.')
            print('')
            print('It took you almost the whole day to track the deer. You find yourself getting tired')
            print(' as you watch the sun starting to set.')
            print('')
            print('You sit down and admire the sunset. This gives you some stamina')
            stamina = stamina + 5
            print('You better make a shelter and a fire if you havent already.')
            survival(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
        if choice == 2:
            selector = 61
            loop = False
            selector = 3
            survival(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
def altSurvivalStory2(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector):
    print('')
    print('You are ready to end the day and get some rest.')
    print('')
    loop = True
    while loop == True:
        choice = int(input("1. Set up fire  2. Set up shelter  3. Back to Menu   4.  Done   :  "))
        if choice == 1:
            if fire >= 1:
                print('')
                print('You set up your fire on the shores of the lake.')
                print('')
                fireSet = True
                fire = fire - 1
                
            if fire < 1 and fireSet == False:
                print('')
                print('You do not have a fire to set up.')
                print('')
        if choice == 2:
            if shelter >= 1:
                print('')
                print('You set up your shelter on the shores of the lake.')
                print('')
                shelterSet = True
                shelter = shelter - 1
                
            if shelter < 1 and shelterSet == False:
                print('')
                print('You do not have a shelter to set up.')
                print('')
        if choice == 3:
            loop = False
            survival(fire, fireSet, shelter, shelterSet, cloth, glass, wood, hunger, thirst, health, stamina, selector)
        if choice == 4:
            break          
    if fireSet == False and shelterSet == True:
        print('You did not set up a fire, but you did set up a shelter. You will be a little cold')
        print('but you will get a decent nights sleep.')
        stamina = stamina + 9
        health = health + 20
    if shelterSet == False and fireSet == True:
        print('You did not set up a shelter, but you did set up a fire. You will be warm')
        print('but you will have nothing to protect you from the elements.')
        stamina = stamina + 9
        health = health + 20
    if shelterSet == False and fireSet == False:
        print('You did not set up a fire or a shelter. You will be very cold tonight and')
        print('will lose some health, and you will not gain back much stamina.')
        stamina = stamina + 5
        health = health + 5
    if shelterSet == True and fireSet == True:
        print('You have both a fire and a shelter. You will be nice and warm tonight, which')
        print('will give you more stamina for tomorrow.')
        stamina = stamina + 15
        health = health + 50

main()
