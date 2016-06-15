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
triggercounter = 0

randdir1 = random.uniform(0.00, 360.00)
randdir2 = random.uniform(0.00, 360.00)
randdir3 = random.uniform(0.00, 360.00)
randdir4 = random.uniform(0.00, 360.00)

win =visual.Window(fullscr=True, screen = 0, allowGUI=False,
    bitsMode=None, units='pix', winType='pyglet')

dotPatch1 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos1,fieldSize=(350,350),
    dotLife=180, #number of frames for each dot to be drawn
    speed=0, dir=randdir1,
    coherence=1, signalDots='same', noiseDots='direction')

dotPatch2 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos1,fieldSize=(350,350),
    dotLife=180, #number of frames for each dot to be drawn
    speed=0, dir=randdir2,
    coherence=1, signalDots='same', noiseDots='direction')

dotPatch3 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos1,fieldSize=(350,350),
    dotLife=180, #number of frames for each dot to be drawn
    speed=0, dir=randdir3,
    coherence=1, signalDots='same', noiseDots='direction')

dotPatch4 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos1,fieldSize=(350,350),
    dotLife=180, #number of frames for each dot to be drawn
    speed=0, dir=randdir4,
    coherence=1, signalDots='same', noiseDots='direction')



while True:
    #If the turn trigger counter matches the randomly generate turning interval
    if triggercounter == randturn:
        #Generate a new direction of turn for next turn.
        deg = random.uniform(0.00, 360.00)
        #Generate new time to next turn
        randturn = random.randint(10,90)
        #Direction of dot movements = random generate degree
        dotPatch1.dir = deg
        dotPatch2.dir = deg/2
        dotPatch3.dir = deg/3
        dotPatch4.dir = deg/4
        #Reset turn counter
        triggercounter = 0
        
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
    triggercounter += 1     
    #print dotPatch1.xys
    
    if event.getKeys(keyList=['escape']):
        win.close()
        core.quit()

    