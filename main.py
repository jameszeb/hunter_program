# This is a sample Python script.
import os
import random
from inspect import stack

import openai
from openai import OpenAI

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Hunter:
    def __init__(self, name):
        self.hunter_name = name
        self.strength = random.randint(1, 10)
        self.intelligence = random.randint(1, 10)
        self.wisdom = random.randint(1, 10)
        self.speed = random.randint(1, 10)

class Species:
    def __init__(self, name):
        self.species = name
        self.strength = random.randint(1, 10)
        self.intelligence = random.randint(1, 10)
        self.wisdom = random.randint(1, 10)
        self.speed = random.randint(1, 10)


def create_hunter(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, hunter {name}')
    print('Your stats are equal to 4-40 points. '
          'You don\'t know what they are.')# Press Ctrl+F8 to toggle the breakpoint.na
    hunter_1 = Hunter(name)
    return hunter_1

def create_animals():
    return(Species('Werewolf'),Species('Mammoth'),Species('Tiger'),Species('Atlasaurus Rex'),Species('Eggasaurus'))

def compare_skills(primal_character_animal,primal_character_hunter):
    pc_animal = 0
    pc_hunter = 0
    tie = 0
    result = None
    if primal_character_animal.strength > primal_character_hunter.strength:
        pc_animal += 1
    elif primal_character_animal.strength < primal_character_hunter.strength:
        pc_hunter += 1
    else:
        tie += 1

    if primal_character_animal.intelligence > primal_character_hunter.intelligence:
        pc_animal += 1
    elif primal_character_animal.intelligence > primal_character_hunter.intelligence:
        pc_hunter += 1
    else:
        tie += 1

    if primal_character_animal.wisdom > primal_character_hunter.wisdom:
        pc_animal += 1
    elif primal_character_animal.wisdom < primal_character_hunter.wisdom:
        pc_hunter += 1
    else :
        tie += 1

    if primal_character_animal.speed > primal_character_hunter.speed:
        pc_animal += 1
    elif primal_character_animal.speed < primal_character_hunter.speed:
        pc_hunter += 1
    else:
        tie += 1

    if pc_animal > pc_hunter and pc_animal>tie:
        result = primal_character_animal
        return result
    if pc_animal < pc_hunter and pc_hunter>tie:
        result = primal_character_hunter
        return result
    return result

def get_total_skills(x):
    return x.wisdom + x.intelligence + x.strength + x.speed

def increase_stats(hunter):
    hunter.intelligence += random.randint(1, 10)
    hunter.wisdom += random.randint(1, 10)
    hunter.strength += random.randint(1, 10)
    hunter.speed += random.randint(1, 10)
    return (hunter.intelligence + hunter.wisdom + hunter.strength + hunter.speed)
def get_list_of_stats(animal):
    return {'Intelligence' : animal.intelligence,
            'Wisdom' : animal.wisdom,
            'Strength' : animal.strength,
            'Speed' : animal.speed}

def battle(animal,hunter):
    winner = compare_skills(animal,hunter)
    if winner == hunter:

        print(f'Your hunter\'s stats increased by {increase_stats(hunter_1)}')
        return (f'The {animal.species} is less powerful than you. '
                f'Describe a pg-13 battle in which you the {hunter} wins in 3 sentences. '
                f'State that the hunter has won at the end in addition to the first request.')
    elif winner == animal:
        return (f'The {animal.species} is less powerful than you. '
                f'Describe a pg-13 battle in which you the {hunter} loses in 3 sentences.'
                f'State that the hunter has lost at the end in addition to the first request.')
    else:
        return (f'The {animal.species} is equally matched with you. '
                f'Describe a pg-13 battle in which you the {animal.species} ties with you in 3 sentences.'
                f'State that the hunter has tied at the end in addition to the first request.')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    hunter_1 = create_hunter('Hero Hunter')
    list_of_animals = create_animals()

    for animal in list_of_animals:

        battle_animals_stats =print(f'\nYou approach a {animal.species}' f' It\'s stats are: ' + str(get_total_skills(animal))+ ' out of 40.')

        characteristics_prompt = input(f'Would you like to know more about the {animal.species}\'s skills?: ')

        if characteristics_prompt.lower() == 'yes':
            if characteristics_prompt.lower() == 'y' or characteristics_prompt.lower() == 'yes':
                print('\n')
                try:
                    print('Please wait ...')
                    client = OpenAI()
                    response = client.responses.create(model='gpt-6.2-astra'
                                                       , input=f'Explain briefly the animals stats. {get_list_of_stats(animal)}, The scale is 1-10. List them vertically with descriptions.')
                    print(response.output_text.strip())
                except openai.APIError as e:
                    print(repr(e.__cause__))
            else:
                print('moving on...')

        battle_question = input(f'\nKnowing what you know now, Would you like to fight or flee from the {animal.species}?: ')

        if battle_question.lower() == 'fight' or battle_question.lower() == 'yes':
            print('\n')
            try:
                print('Please wait ...')
                client = OpenAI()
                response = client.responses.create(model='gpt-6.2-astra'
                                                   , input=battle(animal, hunter_1))
                print(response.output_text.strip())
            except openai.APIError as e:
                print(repr(e.__cause__))
        else:
            print('You fled from it.')








