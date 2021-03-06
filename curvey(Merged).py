# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 15:10:30 2016

@author: Aaron
"""

import numpy as np
from psychopy import visual, event, core
from numpy import random, pi, sin
import random, copy

#Speed of dots
speed = 0.008
#Generate a random movement direction
deg = random.uniform(-180.00, 180.00)
#Generate a random time where a turn is triggered. (60=1s on 60Hz monitor)
randturn = random.randint(10,90)
#Position of centre of dot patch
pos1 = (-240,0)
pos2 = (240,0)
#Number of dots
NrOfDots = 40

bounce_trigger = 60
trigger_counter = 0

randdir1 = random.uniform(0.00, 360.00)

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
    fieldShape='circle', fieldPos=pos2,fieldSize=(350,350),
    dotLife=180, #number of frames for each dot to be drawn
    speed=0, dir=randdir1,
    coherence=1, signalDots='same', noiseDots='direction')

newArray = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])

dotPatch1._dotsDir = newArray
dotPatch2._dotsDir = copy.deepcopy(newArray)
dirChange = random.uniform(-0.1,0.1)

while True:
    dotPatch1.speed = speed
    dotPatch2.speed = speed
    deg = random.uniform(-0.05,0.05)
    if np.abs(dirChange) > 0.1 and np.sign(deg) == np.sign(dirChange):
        dirChange -= deg
    else:
        dirChange += deg
    if trigger_counter == bounce_trigger:
        newArray = copy.deepcopy(dotPatch1._dotsDir)
        dotPatch2._dotsDir = newArray
        trigger_counter = 0
    dotPatch1._dotsDir += dirChange
    dotPatch1.draw()
    dotPatch2.draw()
    win.flip()
    trigger_counter += 1
    
    if event.getKeys(keyList=['escape']):
        win.close()
        core.quit()

    