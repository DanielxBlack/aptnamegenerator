#!/usr/bin/env python3

import random


def createAPTname():
    adjective = open("adjectivelist.txt").read().splitlines()
    theAdjective = random.choice(adjective).capitalize()
    animal = open("animallist.txt").read().splitlines()
    theAnimal = random.choice(animal)
    aptName = f"{theAdjective} {theAnimal}"
    print(f'Your APT name is "{aptName}." Congratulations! You\'re in the big leagues now!')


createAPTname()
