# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 15:10:30 2016

@author: Aaron
"""

import numpy as np
from psychopy import visual, event, core
from numpy import random, pi, sin
import random

<<<<<<< HEAD
#Speed of dots
speed = 0.01
#Generate a random movement direction
deg = random.uniform(-180.00, 180.00)
#Generate a random time where a turn is triggered. (60=1s on 60Hz monitor)
randturn = random.randint(10,120)
#Position of centre of dot patch
pos1 = (-240,0)
#Number of dots
NrOfDots = 50
=======
speed = 0.01
deg = random.uniform(-180.00, 180.00)
#xchange = random.uniform(-1.00,1.00)
#ychange = random.uniform(-1.00,1.00)
randturn = random.randint(10,120)
k = []
pos1 = (-240,0)
>>>>>>> origin/master

speed23 = []
speed23SCALED = []
GauSpeed = []
SinSpeed = []
<<<<<<< HEAD
k = []
num = 0
triggercounter = 0

=======

turn = False
num = 0
NrOfDots = 50
turn_trigger = 40
>>>>>>> origin/master

win =visual.Window(fullscr=True, screen = 0, allowGUI=False,
    bitsMode=None, units='pix', winType='pyglet')

dotPatch1 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos1,fieldSize=(350,350),
    dotLife=180, #number of frames for each dot to be drawn
    speed=0, dir=180,
    coherence=1, noiseDots='direction')

'''
#SANDBOX CODES - UNSTABLE
#for jerky condition
for x in range(20):
    k.append(1)
for x in range(10):
    k.append(5)
for x in range(5):
    k.append(10)    
for x in range(10):
    k.append(5)
for x in range(20):
    k.append(1)
    
def twothird():
    global num, speed23
    for this in range(len(k)):
        velocity = (np.power(x*k[num], -0.33))
        speed23.append(velocity)
        num +=1 
    
twothird()

#for smooth condition
def twothird():
    global num, speed23
    for this in range(len(k)):
        velocity = (np.power(x*k[num], -0.33))
        speed23.append(velocity)
        num +=1 

num = 0 

def rough_curvature():
    global k
    
    if dotPatch1.dir <= 180:
        k = 0.05*dotPatch1.dir
    elif dotPatch1.dir > 180:
        k = 0.05*(360-dotPatch1.dir)
    if dotPatch1.dir <= 45:
        k = 5.
    elif dotPatch1.dir <= 90 and dotPatch1.dir < 180:
        k = 10.
    elif dotPatch1.dir <= 180 and dotPatch1.dir < 270:
        k = 20.
    elif dotPatch1.dir <= 270 and dotPatch1.dir > 315:
        k = 10.
    elif dotPatch1.dir <= 315 and dotPatch1.dir >= 360:
        k = 5.
  
print speed23
print randturn

for x in range(len(speed23)):
    scale = speed23[num]/100
    speed23SCALED.append(scale)
    num += 1'''
    
<<<<<<< HEAD

while True:
    #If the turn trigger counter matches the randomly generate turning interval
    if triggercounter == randturn:
        #Generate a new direction of turn for next turn.
        deg = random.randint(0, 180)
        #Generate random left turn or right turn
        turn_dir = random.randint(1,2)
        #Counter to establish duration of turn
        turn_counter = 0
        #Generate new time to next turn
        randturn = random.randint(10,120)
        #As long as turn counter is lesser than the randomly generate degree of turn
        if turn_counter <= deg:  
            #Each degree of the randomly generate degree of turn = 1 frame
            for x in range(deg):
                #If right turn
                if turn_dir == 1:
                    #Degree of turn +1 
                    dotPatch1.dir += 1
                    turn_counter += 1
                    dotPatch1.speed = speed
                #If left turn
                elif turn_dir == 2:
                    #Degree of turn -1 
=======
num = 0
trigger = randturn
triggercounter = 0


while True:

    if triggercounter == randturn:
        deg = random.randint(0, 180)
        turn_dir = random.randint(1,2)
        turn_counter = 0
        randturn = random.randint(10,120)
        if turn_counter <= deg:  
            for x in range(deg):
                if turn_dir == 1:
                    dotPatch1.dir += 1
                    turn_counter += 1
                    dotPatch1.speed = speed
                elif turn_dir == 2:
>>>>>>> origin/master
                    dotPatch1.dir -= 1
                    turn_counter += 1
                    dotPatch1.speed = speed
                dotPatch1.draw()
<<<<<<< HEAD
                win.flip()     
        #Reset turn trigger counter        
        triggercounter = 0
=======
                win.flip()            
        triggercounter = 0
    #dotPatch1.speed = speed23SCALED[num]
>>>>>>> origin/master
    dotPatch1.speed = speed
    dotPatch1.draw()
    win.flip()
    num += 1
    triggercounter += 1
    
    if event.getKeys(keyList=['escape']):
        win.close()
        core.quit()

    