from main import State
from unicodedata import name
import pygame
import os
import time
from random import randint
import ctypes



class Work(State):
    def __init__(self, FSM):
        super(Work, self).__init__(FSM)

    def Enter(self):
        gg = 0
        print("Preparing to work")
        super(Work, self).Enter(gg)
    
    def Execute(self, name):
        print("I'm Working")
        name.energy -= 1
        name.hunger -= 1
        name.thirst -= 1
        name.happy -= 1
        name.money += 1
        name.gear -= 1
        name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
        if(self.startTime + self.timer <= time.perf_counter()):
            name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)

    def Exit(self):
        print("Finished Working")

class Buy(State):
    def __init__(self, FSM):
        super(Buy, self).__init__(FSM)

    def Enter(self):
        gg = 0
        print("Preparing to Buy")
        super(Buy, self).Enter(gg)
    
    def Execute(self, name):
        print("I'm buying stuff")
        name.money -= 1
        name.gear += 1
        name.food += 1
        name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
        if(self.startTime + self.timer <= time.perf_counter()):
            name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
    
    def Exit(self):
        print("Finished Buying")



class Drink(State):
    def __init__(self, FSM):
        super(Drink, self).__init__(FSM)

    def Enter(self):
        gg = 0
        print("Preparing to Drink")
        super(Drink, self).Enter(gg)
    
    def Execute(self, name):
        print("I'm Drinking")
        name.thirst += 1
        name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
        if(self.startTime + self.timer <= time.perf_counter()):
            name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
            
    def Exit(self):
        print("Finished Drinking")



class Eat(State):
    def __init__(self, FSM):
        super(Eat, self).__init__(FSM)

    def Enter(self):
        gg = 0
        print("Preparing to Eat")
        super(Eat, self).Enter(gg)
    
    def Execute(self, name):
        print("I'm Eating")
        name.hunger += 1
        name.food -= 1
        name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
        if(self.startTime + self.timer <= time.perf_counter()):
            name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
    
    def Exit(self):
        print("Finished Eating")



class Sleep(State):
    def __init__(self, FSM):
        super(Sleep, self).__init__(FSM)

    def Enter(self):
        gg = 0
        print("Preparing to Sleep")
        super(Sleep, self).Enter(gg)
    
    def Execute(self, name):
        print("zzzzZZZZzzz sleeping")
        name.energy += 1
        name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
        if(self.startTime + self.timer <= time.perf_counter()):
            name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
    
    def Exit(self):
        print("Finished Sleeping")




class HangWFriends(State):
    def __init__(self, FSM):
        super(HangWFriends, self).__init__(FSM)

    def Enter(self):
        gg = 0
        print("Preparing to Hang with friends!")
        super(HangWFriends, self).Enter(gg)
    
    def Execute(self, name):
        print("Hanging with friends :D")
        
        name.energy -= 1
        name.happy += 1
        
        name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
        if(self.startTime + self.timer <= time.perf_counter()):
            name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
    
    def Exit(self):
        print("Finished Hanging with Friends")


class Death(State):
    def __init__(self, FSM):
        super(Death, self).__init__(FSM)

    def Enter(self):
        gg = 0
        print("I'M DYING")
        super(Death, self).Enter(gg)
    
    def Execute(self, name):
        print("dead")
        
    
    def Exit(self):
        pass

