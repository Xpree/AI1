from asyncio.windows_events import NULL
from email import message
import queue
from unicodedata import name
import pygame
import os
import time
from random import randint, random
import ctypes
from work import *


##==============================================

#State = type("State",(object,),{})

class State(object):
    def __init__(self, FSM):
        self.FSM = FSM
        self.timer = 0
        self.startTime = 0

    def Enter(self, gg):
        if gg == 1:
            self.timer = 0
        else:
            self.timer = randint(0, 5)
        self.startTime = int(time.perf_counter())

    def Execute(self, name):
        pass
    def Exit(self):
        pass




class Message(State):
    def __init__(self, FSM):
        super(Message, self).__init__(FSM)

    def Enter(self):
        gg = 1
        print("Preparing to Message!")
        super(Message, self).Enter(gg)

    def Execute(self, name):
        
        if name.myId == "ROBOT1":
            whoToMess = randint(1,3)
            whenToMeet = randint(1,5)
            if whoToMess == 1:
                r.addToList(whenToMeet, r.messQueue)
                r2.addToList(whenToMeet, r2.messQueue)
                print("TO R2 IN: ", whenToMeet)
                name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
                name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
            if whoToMess == 2:
                r.addToList(whenToMeet, r.messQueue)
                r3.addToList(whenToMeet, r3.messQueue)
                print("TO R3 IN: ", whenToMeet)
                name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
                name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
            if whoToMess == 3:
                r.addToList(whenToMeet, r.messQueue)
                r4.addToList(whenToMeet, r4.messQueue)
                print("TO R4 IN: ", whenToMeet)
                name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
                name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
        if name.myId == "ROBOT2":
            whoToMess = randint(1,3)
            whenToMeet = randint(1,5)
            if whoToMess == 1:
                r2.addToList(whenToMeet, r2.messQueue)
                r.addToList(whenToMeet, r.messQueue)
                print("TO R1 IN: ", whenToMeet)
                name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
                name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
            if whoToMess == 2:
                r2.addToList(whenToMeet, r2.messQueue)
                r3.addToList(whenToMeet, r3.messQueue)
                print("TO R3 IN: ", whenToMeet)
                name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
                name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
            if whoToMess == 3:
                r2.addToList(whenToMeet, r2.messQueue)
                r4.addToList(whenToMeet, r4.messQueue)
                print("TO R4 IN: ", whenToMeet)
                name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
                name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
        if name.myId == "ROBOT3":
            whoToMess = randint(1,3)
            whenToMeet = randint(1,5)
            if whoToMess == 1:
                r3.addToList(whenToMeet, r3.messQueue)
                r.addToList(whenToMeet, r.messQueue)
                print("TO R1 IN: ", whenToMeet)
                name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
                name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
            if whoToMess == 2:
                r3.addToList(whenToMeet, r3.messQueue)
                r2.addToList(whenToMeet, r2.messQueue)
                print("TO R2 IN: ", whenToMeet)
                name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
                name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
            if whoToMess == 3:
                r3.addToList(whenToMeet, r3.messQueue)
                r4.addToList(whenToMeet, r4.messQueue)
                print("TO R4 IN: ", whenToMeet)
                name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
                name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
        if name.myId == "ROBOT4":
            whoToMess = randint(1,3)
            whenToMeet = randint(1,5)
            if whoToMess == 1:
                r4.addToList(whenToMeet, r4.messQueue)
                r.addToList(whenToMeet, r.messQueue)
                print("TO R1 IN: ", whenToMeet)
                name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
                name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
            if whoToMess == 2:
                r4.addToList(whenToMeet, r4.messQueue)
                r2.addToList(whenToMeet, r2.messQueue)
                print("TO R2 IN: ", whenToMeet)
                name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
                name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
            if whoToMess == 3:
                r4.addToList(whenToMeet, r4.messQueue)
                r3.addToList(whenToMeet, r3.messQueue)
                print("TO R3 IN: ", whenToMeet)
                name.stats(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food, name.myId, name.messQueue)
                name.choice(name.hunger, name.thirst, name.gear, name.happy, name.energy, name.money, name.food)
        
        
        

##=================================================

class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print("Transitioning")

##=================================================


class FSM(object):
    def __init__(self, Char):
        self.Char = Char
        self.states = {}
        self.transition = {}
        self.curState = None
        self.prevState = None #ska göra så man inte loopar och gör samma 2 gånger i rad
        self.trans = None

    def AddTransition(self, transName, transition):
        self.transition[transName] = transition
    
    def AddState(self, stateName, state):
        self.states[stateName] = state

    def SetState(self, stateName):
        self.prevState = self.curState
        self.curState = self.states[stateName]

    def ToTransition (self, toTrans):
        self.trans = self.transition[toTrans]


    def Execute(self, name):
        if (self.trans):
            self.curState.Exit()
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.curState.Enter()
            self.trans = None
        self.curState.Execute(name)
       


##=================================================

Char = type("Char",(object,), {})

class littleMan(Char):
    def __init__(self):
        self.messQueue = []
        self.FSM = FSM(self)

        #states
        self.FSM.AddState("Work", Work(self.FSM))
        self.FSM.AddState("Buy", Buy(self.FSM))
        self.FSM.AddState("Drink", Drink(self.FSM))
        self.FSM.AddState("Eat", Eat(self.FSM))
        self.FSM.AddState("Sleep", Sleep(self.FSM))
        self.FSM.AddState("HangWFriends", HangWFriends(self.FSM))
        self.FSM.AddState("Message", Message(self.FSM))
        self.FSM.AddState("Death", Death(self.FSM))
        

        #Transitions
        self.FSM.AddTransition("toWork", Transition("Work"))
        self.FSM.AddTransition("toBuy", Transition("Buy"))
        self.FSM.AddTransition("toDrink", Transition("Drink"))
        self.FSM.AddTransition("toEat", Transition("Eat"))
        self.FSM.AddTransition("toSleep", Transition("Sleep"))
        self.FSM.AddTransition("toHangWFriends", Transition("HangWFriends"))
        self.FSM.AddTransition("toMessage", Transition("Message"))
        self.FSM.AddTransition("toDeath", Transition("Death"))

        self.FSM.SetState("Sleep")
         

    def Execute(self, name):
        self.FSM.Execute(name)

    hunger = 100
    thirst = 100
    gear = 100
    happy = 100
    energy = 100
    money = 100
    food = 100

    myId = ""



    #stats
    def stats(self, hunger, thirst, gear, happy, energy, money, food, myId, messQueue):
        print(messQueue)
        print("Mitt namn är: ", myId)
        print("             Hunger: ", hunger, " Thirst: ", thirst, " Gear: ", gear, " Happy: ", happy, " Energy :", energy, " Money: ", money, " Food: ", food)
        print("\n")
    
    def choice(self, hunger, thirst, gear, happy, energy, money, food):
        rand = randint(1,6)
        
        if hunger <= 0 or thirst <= 0 or energy <= 0:
            self.FSM.ToTransition("toDeath")
        elif hunger < 30 and food > 20:
            self.FSM.ToTransition("toEat")
        
        elif food < 30 or gear < 30:
            self.FSM.ToTransition("toBuy")
        elif thirst < 30:
            self.FSM.ToTransition("toDrink")
        elif energy < 30:
            self.FSM.ToTransition("toSleep")
        elif happy < 30:
            self.FSM.ToTransition("toHangWFriends")
        elif money < 30:
            self.FSM.ToTransition("toWork")
        
        else:

            if rand == 1:
                self.FSM.ToTransition("toBuy")
            elif rand == 2:
                self.FSM.ToTransition("toWork")
            elif rand == 3:
                self.FSM.ToTransition("toEat")
            elif rand == 4:
                self.FSM.ToTransition("toSleep")
            elif rand == 5:
                self.FSM.ToTransition("toMessage")
            elif rand == 6:
                self.FSM.ToTransition("toDrink")
            # elif rand == 100:
            #     self.FSM.ToTransition("toHangWFriends") # avstängd just nu


        

    def addToList(self, whenToMeet, messQueue):
        messQueue.insert(0, whenToMeet)
        

    def messCount(self, name):
        
        i = 0
        while i < len(name.messQueue):
            name.messQueue[i] -= 1
            if name.messQueue[i] == 0:
                name.messQueue.remove(0)
                i -= 1
                if name.food < 30 or name.thirst < 30:
                        print("i cannot come")
                        break
                elif name.hunger < 30 and name.food > 20:
                    print("i cannot come")
                    break
                elif name.food < 30 or name.gear < 30:
                    print("i cannot come")
                    break
                elif name.thirst < 30:
                    print("i cannot come")
                    break
                elif name.energy < 30:
                    print("i cannot come")
                elif name.happy < 30:
                    print("i cannot come")
                    break
                elif name.money < 30:
                    print("i cannot come")
                    break           


                else:
                    name.FSM.ToTransition("toHangWFriends")
                    break
            i += 1

       



##=================================================

if __name__ == '__main__':
    r = littleMan()
    r.myId = "ROBOT1"
    r2 = littleMan()
    r2.myId = "ROBOT2"
    r3 = littleMan()
    r3.myId = "ROBOT3"
    r4 = littleMan()
    r4.myId = "ROBOT4"
    print("====================================")
    for i in range(1000):
        startTime = time.perf_counter()
        timeInterval = 0.2
        while(startTime + timeInterval > time.perf_counter()):
            pass
                    
        r.messCount(r)
        r2.messCount(r2)
        r3.messCount(r3)
        r4.messCount(r4)

        r.Execute(r)
        r2.Execute(r2)
        r3.Execute(r3)
        r4.Execute(r4)
        print("====================================")

