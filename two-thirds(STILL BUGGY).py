# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 15:10:30 2016

@author: Aaron
"""

import numpy as np
from psychopy import visual, event, core
from numpy import random, pi, sin
import random

#Speed of dots
speed = 0.01
velocity = speed
#Generate a random movement direction
deg = random.uniform(-180.00, 180.00)
#Generate a random time where a turn is triggered. (60=1s on 60Hz monitor)
randturn = random.randint(10,120)
#Position of centre of dot patch
pos1 = (-240,0)
#Number of dots
NrOfDots = 50

speed23 = []
speed23SCALED = []
GauSpeed = []
SinSpeed = []
k = []
num = 0
triggercounter = 0


win =visual.Window(fullscr=True, screen = 0, allowGUI=False,
    bitsMode=None, units='pix', winType='pyglet')

dotPatch1 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos1,fieldSize=(350,350),
    dotLife=180, #number of frames for each dot to be drawn
    speed=0, dir=180,
    coherence=1, noiseDots='direction')

'''#Quadratic Curve formula to create movement trajectory
def quad_curve():
    y = a*(x**2) + (b*x) + c'''


#SANDBOX CODES - THESE WON'T MAKE SENSE AT IT'S CURRENT STAGE! IT'S JUST TO TEST OUT THE MACHINE AND SEE HOW IT'D
#ROUGHLY LOOK LIKE.

#Two-thirds power law (k = gradient). 
def twothird():
    global velocity
    velocity = speed*(k**-0.33)

num = 0 

#Generate an arbitary gradient value based on each degree the dots are moving on
def rough_curvature():
    global k
    #At the first half of a randomly chosen degree value (Ie. at 120 degrees, any frame that consist of 60=< degrees) 
    #generate an ascending gradient value. The 0.001 wouldn't make sense; it's an arbitrary value that generates
    #realistic k value, although not perfectly fine tuned.
    if turn_counter <= deg/2:
        k = np.abs(0.001*dotPatch1.dir)
    #At the second half of the chosen degree value, generate descending gradient value    
    elif turn_counter > deg/2:
        k = np.abs(0.001*(deg-dotPatch1.dir))
    #print 'k', k
        

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
            #Each degree of the randomly generate degree of turn = 1 frame. 0.38 is an arbitary value that doesn't
            #make sense, but scales the velocity quite nicely, though not perfectly accurate.
            for x in range(deg):
                #If right turn
                if turn_dir == 1:
                    #Degree of turn +1 
                    rough_curvature()
                    twothird()
                    dotPatch1.dir += 1.
                    turn_counter += 1
                    dotPatch1.speed = velocity*0.38
                    #print 'velocity', dotPatch1.speed
                    #print 'dotPatch1.dir', dotPatch1.dir
                #If left turn
                elif turn_dir == 2:
                    #Degree of turn -1 
                    rough_curvature()
                    twothird()
                    dotPatch1.dir -= 1.
                    turn_counter += 1
                    dotPatch1.speed = velocity*0.38
                    #print 'velocity', dotPatch1.speed
                    #print 'dotPatch1.dir', dotPatch1.dir                    
                dotPatch1.draw()
                win.flip()     
        #Reset turn trigger counter        
        triggercounter = 0
    velocity = speed
    dotPatch1.speed = velocity
    #print 'velocity', dotPatch1.speed
    dotPatch1.draw()
    win.flip()
    num += 1
    triggercounter += 1
    
    if event.getKeys(keyList=['escape']):
        win.close()
        core.quit()

    