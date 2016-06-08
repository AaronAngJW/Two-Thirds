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


while True:
    #If the turn trigger counter matches the randomly generate turning interval
    if triggercounter == randturn:
        #Generate a new direction of turn for next turn.
        deg = random.uniform(0.00, 360.00)
        #Generate new time to next turn
        randturn = random.randint(10,120)
        #Direction of dot movements = random generate degree
        dotPatch1.dir = deg
        #Reset turn counter
        triggercounter = 0
        
    dotPatch1.speed = speed
    dotPatch1.draw()
    
    win.flip()
    num += 1 
    triggercounter += 1     
    print dotPatch1.xys
    
    if event.getKeys(keyList=['escape']):
        win.close()
        core.quit()

    