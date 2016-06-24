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
randturn = random.randint(10,90)
#Position of centre of dot patch
pos1 = (-240,0)
#Number of dots
NrOfDots = 40

k = []
num = 0
triggercounter1 = 0

randdir1 = random.uniform(0.00, 360.00)

win =visual.Window(fullscr=True, screen = 0, allowGUI=False,
    bitsMode=None, units='pix', winType='pyglet')

dotPatch1 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos1,fieldSize=(350,350),
    dotLife=180, #number of frames for each dot to be drawn
    speed=0, dir=randdir1,
    coherence=1, signalDots='same', noiseDots='direction')

newArray = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])

dotPatch1._dotsDir = newArray
dirChange = random.uniform(-0.1,0.1)
turncounter = 0
turndeg = random.randint(30,90)

while True:
    dotPatch1.speed = speed
    deg = random.uniform(-180.,180.)
    if turncounter == turndeg:
        dotPatch1._dotsDir += deg
        turndeg = random.randint(30,90)
        turncounter = 0
    dotPatch1.draw()
    win.flip()
    turncounter += 1
    
    if event.getKeys(keyList=['escape']):
        win.close()
        core.quit()
    


    