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
#Generate a random movement direction
deg = random.uniform(-180.00, 180.00)
#Generate a random time where a turn is triggered. (60=1s on 60Hz monitor)
randturn = random.randint(10,120)
#Position of centre of dot patch
pos1 = (-240,0)
#Number of dots
NrOfDots = 10

speed23 = []
speed23SCALED = []
GauSpeed = []
SinSpeed = []
k = []
num = 0
triggercounter1 = 0
triggercounter2 = 0


win =visual.Window(fullscr=True, screen = 0, allowGUI=False,
    bitsMode=None, units='pix', winType='pyglet')

dotPatch1 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos1,fieldSize=(350,350),
    dotLife=180, #number of frames for each dot to be drawn
    speed=0, dir=180,
    coherence=1, signalDots='same', noiseDots='direction')

dotPatch2 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos1,fieldSize=(350,350),
    dotLife=180, #number of frames for each dot to be drawn
    speed=0, dir=180,
    coherence=1, signalDots='same', noiseDots='direction')

dotPatch3 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos1,fieldSize=(350,350),
    dotLife=180, #number of frames for each dot to be drawn
    speed=0, dir=180,
    coherence=1, signalDots='same', noiseDots='direction')

dotPatch4 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos1,fieldSize=(350,350),
    dotLife=180, #number of frames for each dot to be drawn
    speed=0, dir=180,
    coherence=1, signalDots='same', noiseDots='direction')
   

while True:
    #If the turn trigger counter matches the randomly generate turning interval
    if triggercounter1 == randturn:
        #Counter to establish duration of turn
        turn_counter1 = 0
        #Generate a new direction of turn for next turn.
        deg = random.randint(0, 180)
        #Generate random left turn or right turn
        turn_dir = random.randint(1,2)
        #Generate new time to next turn
        randturn = random.randint(10,120)
        #As long as turn counter is lesser than the randomly generate degree of turn
        if turn_counter1 <= deg:  
            #Each degree of the randomly generate degree of turn = 1 frame
            for x in range(deg):
                #If right turn
                if turn_dir == 1:
                    #Degree of turn +1 
                    dotPatch1.dir += 1
                    dotPatch2.dir -= 1
                    dotPatch3.dir += 0.5
                    dotPatch4.dir -= 0.5
                    turn_counter1 += 1
                #If left turn
                elif turn_dir == 2:
                    #Degree of turn -1 
                    dotPatch1.dir -= 1
                    dotPatch2.dir += 1
                    dotPatch3.dir -= 0.5
                    dotPatch4.dir += 0.5                    
                    turn_counter1 += 1
                dotPatch1.draw()
                dotPatch2.draw()
                dotPatch3.draw()
                dotPatch4.draw()
                
                win.flip()     
        #Reset turn trigger counter        
        triggercounter1 = 0
    '''if triggercounter2 == randturn:
        #Counter to establish duration of turn
        turn_counter2 = 0
        #Generate a new direction of turn for next turn.
        deg = random.randint(0, 180)
        #Generate random left turn or right turn
        turn_dir = random.randint(1,2)
        #Generate new time to next turn
        randturn = random.randint(10,120)
        #As long as turn counter is lesser than the randomly generate degree of turn
        if turn_counter2 <= deg:  
            #Each degree of the randomly generate degree of turn = 1 frame
            for x in range(deg):
                #If right turn
                if turn_dir == 1:
                    #Degree of turn +1 
                    dotPatch2.dir += 1
                    turn_counter2 += 1
                    dotPatch2.speed = speed
                #If left turn
                elif turn_dir == 2:
                    #Degree of turn -1 
                    dotPatch2.dir -= 1
                    turn_counter2 += 1
                    dotPatch2.speed = speed
                dotPatch2.draw()
                win.flip()     
        #Reset turn trigger counter        
        triggercounter2 = 0'''
    dotPatch1.speed = speed
    dotPatch2.speed = speed
    dotPatch3.speed = speed
    dotPatch4.speed = speed
    dotPatch1.draw()
    dotPatch2.draw()
    dotPatch3.draw()
    dotPatch4.draw()
    win.flip()
    num += 1
    triggercounter1 += 1
    
    if event.getKeys(keyList=['escape']):
        win.close()
        core.quit()    
    

    


    