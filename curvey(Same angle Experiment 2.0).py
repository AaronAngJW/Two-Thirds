# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 15:10:30 2016

@author: Aaron
"""

import numpy as np
from psychopy import visual, event, core, data, gui
from numpy import random
import random, copy
from random import shuffle
from datetime import datetime
from csv import DictWriter

#Speed of dots
speed = 0.01
#Generate a random movement direction
deg = random.uniform(-180.00, 180.00)
#Generate a random time where a turn is triggered. (60=1s on 60Hz monitor)
randturn = random.randint(10,90)
#Position of centre of dot patch
pos1 = (-220,0)
pos2 = (220,0)
#Number of dots
NrOfDots = 20 #Only in multiples of 4

trialnum = 0
numreps = 10
TrialType = ['J1', 'JN2', 'N3', 'NS4', 'S5']
DisplayType = ['0', '1'] #0 = Left, 1 = Right
TrialList = []
n = 150 #300 #Duration of trial display (100hz (CRT refresh rate) = 1s)
restinterval = 20 #Allow participants to rest at every n trial
intertrial_interval = 0.2
adaptduration = 1800 #100Hz (for CRT) x number of seconds. This is for the first trial for every block. Subsequent trials have an adaptduration of adaptaduration/6.

bounce_trigger = 30
trigger_counter = 0
randdir1 = random.uniform(0.00, 360.00)
dirChange = random.uniform(-0.1,0.1)
deg1 = -0.1
deg2 = 0.1
CurveTurnRate = 0.1 #The higher the value the higher the turn frequency

outputs = {}
rested = False
adaptSJ = True
adaptJS = False
trigger_rest = True
outputTRIAL = 1

#Set experimental name as 'Dotty'
outputs['Exp Name'] = 'Plausible FULL'
#Set experimental date and time
outputs['Exp Date'] = datetime.now().strftime('%Y%m%d_%H%M')
#Set participant ID textbox
outputs['ParticipantID'] = ''
#GUI display set to unchangable Exp Name, Exp Date, whilst allowing user to key in participant ID
dlg = gui.DlgFromDict(outputs, title='Input data', fixed=['Exp Name', 'Exp Date'], order=['Exp Name', 'Exp Date', 'ParticipantID'])

#If user presses cancel, abort experiment
if not dlg.OK:
    print('User cancelled the experiment')
    core.quit()     

win =visual.Window(fullscr=True, screen = 0, allowGUI=False,
    bitsMode=None, units='pix', winType='pyglet')

dotPatch1 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos1,fieldSize=(350,350),
    dotLife=90, #number of frames for each dot to be drawn
    speed=0, 
    coherence=1, noiseDots='direction')  
dotPatch2 = visual.DotStim(win, units='pix', 
    color=(1.0,1.0,1.0), nDots=NrOfDots, dotSize = 5,
    fieldShape='circle', fieldPos=pos2,fieldSize=(350,350),
    dotLife=90, #number of frames for each dot to be drawn
    speed=0, 
    coherence=1, noiseDots='direction')
       
    
#Set file name for output data file which includes participant ID and the experiment time and date
filename = 'PartID_%s_%s.csv' % (outputs['ParticipantID'], outputs['Exp Date'])

#Generate trial list
for type in TrialType:
    for display in DisplayType: 
        for rep in range(numreps):
            TrialList.append([display, type])
            
shuffle(TrialList)
print TrialList

newArray40 = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])

dotPatch1._dotsDir = copy.deepcopy(newArray40)
dotPatch2._dotsDir = copy.deepcopy(newArray40)

print dotPatch1._dotsDir

fixation = visual.TextStim(win, text = '+', bold = 'True', pos=[0,0], rgb=1)


def adaptation_SJ():
    global dotPatch1, dotPatch2, dotPatch3, dotPatch4, rested, trigger_counter, dirChange
    if trialnum == 0:
        adapttime = adaptduration
    elif rested == True:
        adapttime = adaptduration
    else:
        adapttime = adaptduration/5

    for adaptation in range(adapttime): 
        if event.getKeys(keyList=['escape']):
            win.close()
            core.quit()
        dotPatch1.speed = speed
        dotPatch2.speed = speed
        deg = random.uniform(-deg2,deg2)
        if np.abs(dirChange) > CurveTurnRate and np.sign(deg) == np.sign(dirChange):
            dirChange -= deg
        else:
            dirChange += deg
        if trigger_counter == bounce_trigger:
            #newArray = copy.deepcopy(dotPatch1._dotsDir)
            dotPatch2._dotsDir = copy.deepcopy(dotPatch1._dotsDir)
            trigger_counter = 0
        dotPatch1._dotsDir += dirChange
        dotPatch1.draw()
        dotPatch2.draw()
        fixation.draw()
        win.flip()
        trigger_counter += 1
        rested = False 
        
        
def adaptation_JS():
    global dotPatch1, dotPatch2, dotPatch3, dotPatch4, rested, trigger_counter, dirChange
    if trialnum == 0:
        adapttime = adaptduration
    elif rested == True:
        adapttime = adaptduration
    else:
        adapttime = adaptduration/5
    for adaptation in range(adapttime): 
        if event.getKeys(keyList=['escape']):
            print dotPatch1._dotsDir
            win.close()
            core.quit()
        dotPatch1.speed = speed
        dotPatch2.speed = speed
        deg = random.uniform(-deg2,deg2)
        if np.abs(dirChange) > CurveTurnRate and np.sign(deg) == np.sign(dirChange):
            dirChange -= deg
        else:
            dirChange += deg
        if trigger_counter == bounce_trigger:
            #newArray = copy.deepcopy(dotPatch1._dotsDir)
            dotPatch1._dotsDir = copy.deepcopy(dotPatch2._dotsDir)
            trigger_counter = 0
        dotPatch2._dotsDir += dirChange
        dotPatch1.draw()
        dotPatch2.draw()
        fixation.draw()
        win.flip()
        trigger_counter += 1
        rested = False 

        
#Create a csv file in write format to allow input of data later on. 
createfile = open(filename, 'wb')
#Setup header for file
writer = DictWriter(createfile, fieldnames=['trialnum', 'stimulus', 'stimulus_location', 'response', 'more_smooth_like', 'smooth_adapt'])
#Write header
writer.writeheader()

startstim = visual.TextStim(win, text = 'Press SPACE to begin experiment or press ESCAPE to abort.', pos=(0,0))
startstim.draw()
win.flip()
promptstim = visual.TextStim(win, text = 'Which patch (left or right) looked SMOOTHER? Hit the LEFT arrow for the left patch or RIGHT arrow for the right patch.', pos=(0,0))
fixation = visual.TextStim(win, text = '+', bold = 'True', pos=[0,0], rgb=1)


for key in event.waitKeys():
    if key in ['escape']:
        win.close()
        core.quit()
    elif key in ['space']:
        trigger_counter = 0

        for experiment in range(len(TrialList)*2):        
            if TrialList[trialnum][1] == 'J1' and TrialList[trialnum][0] == '0':
                print '-------'
                print 'trialnum:', trialnum+outputTRIAL
                print 'J1 Left'
                fixation.draw()                
                win.flip()
                core.wait(1.0)                
                if adaptSJ == True:                
                    adaptation_SJ()
                    adaptS = 1
                if adaptJS == True:
                    adaptation_JS()
                    adaptS = 0
                fixation.draw()                
                win.flip()
                core.wait(1.0)
                for triallength in range(n): 
                    if event.getKeys(keyList=['escape']):
                        win.close()
                        core.quit()
                    if triallength == 1:
                        #Generate independent direction for each dot
                        newArray40 = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])
                        
                        dotPatch1._dotsDir = copy.deepcopy(newArray40)
                        dotPatch2._dotsDir = copy.deepcopy(newArray40)

                    dotPatch1.speed = speed
                    dotPatch2.speed = speed
                    #Generate a random degree (pixel) of movement per frame for curvy movement
                    deg = random.uniform(-deg2,deg2)
                    #To prevent curvy motion from getting stuck in an abyss inward movement
                    if np.abs(dirChange) > CurveTurnRate and np.sign(deg) == np.sign(dirChange):
                        dirChange -= deg
                    else:
                        dirChange += deg
                    #Bounce for Jerky      
                    if trigger_counter == bounce_trigger:
                        dotPatch1._dotsDir = copy.deepcopy(dotPatch2._dotsDir)
                        dotPatch2._dotsDir[NrOfDots/2:NrOfDots] = copy.deepcopy(dotPatch1._dotsDir[NrOfDots/2:NrOfDots])
                        trigger_counter = 0
                    #Live update of curvy motion    
                    dotPatch2._dotsDir[0:NrOfDots/2] += dirChange
                    fixation.draw()
                    dotPatch1.draw()
                    dotPatch2.draw()
                    win.flip()
                    trigger_counter += 1
                trigger_counter = 0    
                win.flip()    
                core.wait(intertrial_interval)
                promptstim.draw()
                win.flip() 
                for key in event.waitKeys(keyList = ['left', 'right', 'escape']):
                    if key in ['left']:
                        print 'left hit'
                        userkey = '0'
                    elif key in ['right']:
                        print 'right hit'
                        userkey = '1'
                    elif key in ['escape']:
                        print 'aborted'
                        userkey = 'aborted'
                        win.close()
                        core.quit()
                win.flip()
                if userkey == TrialList[trialnum][0]:
                    sin_like = '1'
                else:
                    sin_like = '0'                
                #Print data for the current trial into a line of text
                outputs = {'trialnum': trialnum+outputTRIAL, 'stimulus': TrialList[trialnum][1] , 'stimulus_location': TrialList[trialnum][0], 'response': userkey, 'more_smooth_like': sin_like, 'smooth_adapt': adaptS }
                trialnum += 1
                #Print the above line of text into the next line in the csv file    
                writer.writerow(outputs)
#---------------------------------------------------------------------------------------------------                
            if TrialList[trialnum][1] == 'JN2' and TrialList[trialnum][0] == '0':
                print '-------'
                print 'trialnum:', trialnum+outputTRIAL
                print 'JN2 Left'
                fixation.draw()                
                win.flip()
                core.wait(1.0)                
                if adaptSJ == True:                
                    adaptation_SJ()
                    adaptS = 1
                if adaptJS == True:
                    adaptation_JS()
                    adaptS = 0
                fixation.draw()                
                win.flip()
                core.wait(1.0)
                for triallength in range(n): 
                    if event.getKeys(keyList=['escape']):
                        win.close()
                        core.quit()
                    if triallength == 1:
                        newArray40 = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])
                        
                        dotPatch1._dotsDir = copy.deepcopy(newArray40)
                        dotPatch2._dotsDir = copy.deepcopy(newArray40)

                    dotPatch1.speed = speed
                    dotPatch2.speed = speed
                    deg = random.uniform(-deg2,deg2)
                    if np.abs(dirChange) > CurveTurnRate and np.sign(deg) == np.sign(dirChange):
                        dirChange -= deg
                    else:
                        dirChange += deg
                    #Bounce for Jerky    
                    if trigger_counter == bounce_trigger:
                        dotPatch1._dotsDir[NrOfDots/4:NrOfDots] = copy.deepcopy(dotPatch2._dotsDir[NrOfDots/4:NrOfDots])
                        dotPatch2._dotsDir[NrOfDots/2:NrOfDots] = copy.deepcopy(dotPatch1._dotsDir[NrOfDots/2:NrOfDots])
                        trigger_counter = 0
                    dotPatch1._dotsDir[0:NrOfDots/4] += dirChange    
                    dotPatch2._dotsDir[0:NrOfDots/2] += dirChange
                    fixation.draw()
                    dotPatch1.draw()
                    dotPatch2.draw()
                    win.flip()
                    trigger_counter += 1
                trigger_counter = 0 
                win.flip()    
                core.wait(intertrial_interval)
                promptstim.draw()
                win.flip() 
                for key in event.waitKeys(keyList = ['left', 'right', 'escape']):
                    if key in ['left']:
                        print 'left hit'
                        userkey = '0'
                    elif key in ['right']:
                        print 'right hit'
                        userkey = '1'
                    elif key in ['escape']:
                        print 'aborted'
                        userkey = 'aborted'
                        win.close()
                        core.quit()
                win.flip()
                if userkey == TrialList[trialnum][0]:
                    sin_like = '1'
                else:
                    sin_like = '0'                
                #Print data for the current trial into a line of text
                outputs = {'trialnum': trialnum+outputTRIAL, 'stimulus': TrialList[trialnum][1] , 'stimulus_location': TrialList[trialnum][0], 'response': userkey, 'more_smooth_like': sin_like, 'smooth_adapt': adaptS }
                trialnum += 1
                #Print the above line of text into the next line in the csv file    
                writer.writerow(outputs)
#---------------------------------------------------------------------------------------------------                
            if TrialList[trialnum][1] == 'N3' and TrialList[trialnum][0] == '0':
                print '-------'
                print 'trialnum:', trialnum+outputTRIAL
                print 'N3 Left'
                fixation.draw()                
                win.flip()
                core.wait(1.0)                
                if adaptSJ == True:                
                    adaptation_SJ()
                    adaptS = 1
                if adaptJS == True:
                    adaptation_JS()
                    adaptS = 0
                fixation.draw()                
                win.flip()
                core.wait(1.0)
                for triallength in range(n): 
                    if event.getKeys(keyList=['escape']):
                        win.close()
                        core.quit()
                    if triallength == 1:
                        newArray40 = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])
                        
                        dotPatch1._dotsDir = copy.deepcopy(newArray40)
                        dotPatch2._dotsDir = copy.deepcopy(newArray40)

                    dotPatch1.speed = speed
                    dotPatch2.speed = speed
                    deg = random.uniform(-deg2,deg2)
                    if np.abs(dirChange) > CurveTurnRate and np.sign(deg) == np.sign(dirChange):
                        dirChange -= deg
                    else:
                        dirChange += deg
                    #Bounce for Jerky    
                    if trigger_counter == bounce_trigger:
                        dotPatch1._dotsDir[0:NrOfDots/2] = copy.deepcopy(dotPatch2._dotsDir[0:NrOfDots/2])
                        dotPatch2._dotsDir[NrOfDots/2:NrOfDots] = copy.deepcopy(dotPatch1._dotsDir[NrOfDots/2:NrOfDots])
                        trigger_counter = 0
                    dotPatch1._dotsDir[NrOfDots/2:NrOfDots] += dirChange    
                    dotPatch2._dotsDir[0:NrOfDots/2] += dirChange
                    fixation.draw()
                    dotPatch1.draw()
                    dotPatch2.draw()
                    win.flip()
                    trigger_counter += 1
                trigger_counter = 0 
                win.flip()    
                core.wait(intertrial_interval)
                promptstim.draw()
                win.flip() 
                for key in event.waitKeys(keyList = ['left', 'right', 'escape']):
                    if key in ['left']:
                        print 'left hit'
                        userkey = '0'
                    elif key in ['right']:
                        print 'right hit'
                        userkey = '1'
                    elif key in ['escape']:
                        print 'aborted'
                        userkey = 'aborted'
                        win.close()
                        core.quit()
                win.flip()
                if userkey == TrialList[trialnum][0]:
                    sin_like = '1'
                else:
                    sin_like = '0'                
                #Print data for the current trial into a line of text
                outputs = {'trialnum': trialnum+outputTRIAL, 'stimulus': TrialList[trialnum][1] , 'stimulus_location': TrialList[trialnum][0], 'response': userkey, 'more_smooth_like': sin_like, 'smooth_adapt': adaptS }
                trialnum += 1
                #Print the above line of text into the next line in the csv file    
                writer.writerow(outputs)
#---------------------------------------------------------------------------------------------------                
            if TrialList[trialnum][1] == 'NS4' and TrialList[trialnum][0] == '0':
                print '-------'
                print 'trialnum:', trialnum+outputTRIAL
                print 'NS4 Left'
                fixation.draw()                
                win.flip()
                core.wait(1.0)                
                if adaptSJ == True:                
                    adaptation_SJ()
                    adaptS = 1
                if adaptJS == True:
                    adaptation_JS()
                    adaptS = 0
                fixation.draw()                
                win.flip()
                core.wait(1.0)
                for triallength in range(n): 
                    if event.getKeys(keyList=['escape']):
                        win.close()
                        core.quit()
                    if triallength == 1:
                        newArray40 = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])
                        
                        dotPatch1._dotsDir = copy.deepcopy(newArray40)
                        dotPatch2._dotsDir = copy.deepcopy(newArray40)

                    dotPatch1.speed = speed
                    dotPatch2.speed = speed
                    deg = random.uniform(-deg2,deg2)
                    if np.abs(dirChange) > CurveTurnRate and np.sign(deg) == np.sign(dirChange):
                        dirChange -= deg
                    else:
                        dirChange += deg
                    #Bounce for Jerky    
                    if trigger_counter == bounce_trigger:
                        dotPatch1._dotsDir[0:NrOfDots/4*3] = copy.deepcopy(dotPatch2._dotsDir[0:NrOfDots/4*3])
                        dotPatch2._dotsDir[NrOfDots/2:NrOfDots] = copy.deepcopy(dotPatch1._dotsDir[NrOfDots/2:NrOfDots])
                        trigger_counter = 0
                    dotPatch1._dotsDir[NrOfDots/4*3:NrOfDots] += dirChange    
                    dotPatch2._dotsDir[0:NrOfDots/2] += dirChange
                    fixation.draw()
                    dotPatch1.draw()
                    dotPatch2.draw()
                    win.flip()
                    trigger_counter += 1
                trigger_counter = 0 
                win.flip()    
                core.wait(intertrial_interval)
                promptstim.draw()
                win.flip() 
                for key in event.waitKeys(keyList = ['left', 'right', 'escape']):
                    if key in ['left']:
                        print 'left hit'
                        userkey = '0'
                    elif key in ['right']:
                        print 'right hit'
                        userkey = '1'
                    elif key in ['escape']:
                        print 'aborted'
                        userkey = 'aborted'
                        win.close()
                        core.quit()
                win.flip()
                if userkey == TrialList[trialnum][0]:
                    sin_like = '1'
                else:
                    sin_like = '0'                
                #Print data for the current trial into a line of text
                outputs = {'trialnum': trialnum+outputTRIAL, 'stimulus': TrialList[trialnum][1] , 'stimulus_location': TrialList[trialnum][0], 'response': userkey, 'more_smooth_like': sin_like, 'smooth_adapt': adaptS }
                trialnum += 1
                #Print the above line of text into the next line in the csv file    
                writer.writerow(outputs)                
#---------------------------------------------------------------------------------------------------                
            if TrialList[trialnum][1] == 'S5' and TrialList[trialnum][0] == '0':
                print '-------'
                print 'trialnum:', trialnum+outputTRIAL
                print 'S5 Left'
                fixation.draw()                
                win.flip()
                core.wait(1.0)                
                if adaptSJ == True:                
                    adaptation_SJ()
                    adaptS = 1
                if adaptJS == True:
                    adaptation_JS()
                    adaptS = 0
                fixation.draw()                
                win.flip()
                core.wait(1.0)
                for triallength in range(n): 
                    if event.getKeys(keyList=['escape']):
                        win.close()
                        core.quit()
                    if triallength == 1:
                        newArray40 = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])
                        
                        dotPatch1._dotsDir = copy.deepcopy(newArray40)
                        dotPatch2._dotsDir = copy.deepcopy(newArray40)

                    dotPatch1.speed = speed
                    dotPatch2.speed = speed
                    deg = random.uniform(-deg2,deg2)
                    if np.abs(dirChange) > CurveTurnRate and np.sign(deg) == np.sign(dirChange):
                        dirChange -= deg
                    else:
                        dirChange += deg
                    #Bounce for Jerky    
                    if trigger_counter == bounce_trigger:
                        dotPatch2._dotsDir[NrOfDots/2:NrOfDots] = copy.deepcopy(dotPatch1._dotsDir[NrOfDots/2:NrOfDots])
                        trigger_counter = 0
                    dotPatch1._dotsDir += dirChange    
                    dotPatch2._dotsDir[0:NrOfDots/2] += dirChange
                    fixation.draw()
                    dotPatch1.draw()
                    dotPatch2.draw()
                    win.flip()
                    trigger_counter += 1
                trigger_counter = 0 
                win.flip()    
                core.wait(intertrial_interval)
                promptstim.draw()
                win.flip() 
                for key in event.waitKeys(keyList = ['left', 'right', 'escape']):
                    if key in ['left']:
                        print 'left hit'
                        userkey = '0'
                    elif key in ['right']:
                        print 'right hit'
                        userkey = '1'
                    elif key in ['escape']:
                        print 'aborted'
                        userkey = 'aborted'
                        win.close()
                        core.quit()
                win.flip()
                if userkey == TrialList[trialnum][0]:
                    sin_like = '1'
                else:
                    sin_like = '0'                
                #Print data for the current trial into a line of text
                outputs = {'trialnum': trialnum+outputTRIAL, 'stimulus': TrialList[trialnum][1] , 'stimulus_location': TrialList[trialnum][0], 'response': userkey, 'more_smooth_like': sin_like, 'smooth_adapt': adaptS }
                trialnum += 1
                #Print the above line of text into the next line in the csv file    
                writer.writerow(outputs)                
#-----------------------------------------------SWAP HERE--------------------------------------------                
            if TrialList[trialnum][1] == 'J1' and TrialList[trialnum][0] == '1':
                print '-------'
                print 'trialnum:', trialnum+outputTRIAL
                print 'J1 Right'
                fixation.draw()                
                win.flip()
                core.wait(1.0)                
                if adaptSJ == True:                
                    adaptation_SJ()
                    adaptS = 1
                if adaptJS == True:
                    adaptation_JS()
                    adaptS = 0
                fixation.draw()                
                win.flip()
                core.wait(1.0)
                for triallength in range(n): 
                    if event.getKeys(keyList=['escape']):
                        win.close()
                        core.quit()
                    if triallength == 1:
                        newArray40 = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])
                        
                        dotPatch1._dotsDir = copy.deepcopy(newArray40)
                        dotPatch2._dotsDir = copy.deepcopy(newArray40)

                    dotPatch1.speed = speed
                    dotPatch2.speed = speed
                    deg = random.uniform(-deg2,deg2)
                    if np.abs(dirChange) > CurveTurnRate and np.sign(deg) == np.sign(dirChange):
                        dirChange -= deg
                    else:
                        dirChange += deg
                    #Bounce for Jerky    
                    if trigger_counter == bounce_trigger:
                        dotPatch1._dotsDir[NrOfDots/2:NrOfDots] = copy.deepcopy(dotPatch2._dotsDir[NrOfDots/2:NrOfDots])
                        dotPatch2._dotsDir = copy.deepcopy(dotPatch1._dotsDir)
                        trigger_counter = 0
                    dotPatch1._dotsDir[0:NrOfDots/2] += dirChange    
                    fixation.draw()
                    dotPatch1.draw()
                    dotPatch2.draw()
                    win.flip()
                    trigger_counter += 1
                trigger_counter = 0 
                win.flip()    
                core.wait(intertrial_interval)
                promptstim.draw()
                win.flip() 
                for key in event.waitKeys(keyList = ['left', 'right', 'escape']):
                    if key in ['left']:
                        print 'left hit'
                        userkey = '0'
                    elif key in ['right']:
                        print 'right hit'
                        userkey = '1'
                    elif key in ['escape']:
                        print 'aborted'
                        userkey = 'aborted'
                        win.close()
                        core.quit()
                win.flip()
                if userkey == TrialList[trialnum][0]:
                    sin_like = '1'
                else:
                    sin_like = '0'                
                #Print data for the current trial into a line of text
                outputs = {'trialnum': trialnum+outputTRIAL, 'stimulus': TrialList[trialnum][1] , 'stimulus_location': TrialList[trialnum][0], 'response': userkey, 'more_smooth_like': sin_like, 'smooth_adapt': adaptS }
                trialnum += 1
                #Print the above line of text into the next line in the csv file    
                writer.writerow(outputs)  
#---------------------------------------------------------------------------------------------------                
            if TrialList[trialnum][1] == 'JN2' and TrialList[trialnum][0] == '1':
                print '-------'
                print 'trialnum:', trialnum+outputTRIAL
                print 'JN2 Right'
                fixation.draw()                
                win.flip()
                core.wait(1.0)                
                if adaptSJ == True:                
                    adaptation_SJ()
                    adaptS = 1
                if adaptJS == True:
                    adaptation_JS()
                    adaptS = 0
                fixation.draw()                
                win.flip()
                core.wait(1.0)
                for triallength in range(n): 
                    if event.getKeys(keyList=['escape']):
                        win.close()
                        core.quit()
                    if triallength == 1:
                        newArray40 = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])
                        
                        dotPatch1._dotsDir = copy.deepcopy(newArray40)
                        dotPatch2._dotsDir = copy.deepcopy(newArray40)

                    dotPatch1.speed = speed
                    dotPatch2.speed = speed
                    deg = random.uniform(-deg2,deg2)
                    if np.abs(dirChange) > CurveTurnRate and np.sign(deg) == np.sign(dirChange):
                        dirChange -= deg
                    else:
                        dirChange += deg
                    #Bounce for Jerky    
                    if trigger_counter == bounce_trigger:
                        dotPatch1._dotsDir[NrOfDots/2:NrOfDots] = copy.deepcopy(dotPatch2._dotsDir[NrOfDots/2:NrOfDots])
                        dotPatch2._dotsDir[NrOfDots/4:NrOfDots] = copy.deepcopy(dotPatch1._dotsDir[NrOfDots/4:NrOfDots])
                        trigger_counter = 0
                    dotPatch1._dotsDir[0:NrOfDots/2] += dirChange 
                    dotPatch2._dotsDir[0:NrOfDots/4] += dirChange
                    fixation.draw()
                    dotPatch1.draw()
                    dotPatch2.draw()
                    win.flip()
                    trigger_counter += 1
                trigger_counter = 0 
                win.flip()    
                core.wait(intertrial_interval)
                promptstim.draw()
                win.flip() 
                for key in event.waitKeys(keyList = ['left', 'right', 'escape']):
                    if key in ['left']:
                        print 'left hit'
                        userkey = '0'
                    elif key in ['right']:
                        print 'right hit'
                        userkey = '1'
                    elif key in ['escape']:
                        print 'aborted'
                        userkey = 'aborted'
                        win.close()
                        core.quit()
                win.flip()
                if userkey == TrialList[trialnum][0]:
                    sin_like = '1'
                else:
                    sin_like = '0'                
                #Print data for the current trial into a line of text
                outputs = {'trialnum': trialnum+outputTRIAL, 'stimulus': TrialList[trialnum][1] , 'stimulus_location': TrialList[trialnum][0], 'response': userkey, 'more_smooth_like': sin_like, 'smooth_adapt': adaptS }
                trialnum += 1
                #Print the above line of text into the next line in the csv file    
                writer.writerow(outputs) 
#---------------------------------------------------------------------------------------------------                
            if TrialList[trialnum][1] == 'N3' and TrialList[trialnum][0] == '1':
                print '-------'
                print 'trialnum:', trialnum+outputTRIAL
                print 'N3 Right'
                fixation.draw()                
                win.flip()
                core.wait(1.0)                
                if adaptSJ == True:                
                    adaptation_SJ()
                    adaptS = 1
                if adaptJS == True:
                    adaptation_JS()
                    adaptS = 0
                fixation.draw()                
                win.flip()
                core.wait(1.0)
                for triallength in range(n): 
                    if event.getKeys(keyList=['escape']):
                        win.close()
                        core.quit()
                    if triallength == 1:
                        newArray40 = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])
                        
                        dotPatch1._dotsDir = copy.deepcopy(newArray40)
                        dotPatch2._dotsDir = copy.deepcopy(newArray40)

                    dotPatch1.speed = speed
                    dotPatch2.speed = speed
                    deg = random.uniform(-deg2,deg2)
                    if np.abs(dirChange) > CurveTurnRate and np.sign(deg) == np.sign(dirChange):
                        dirChange -= deg
                    else:
                        dirChange += deg
                    #Bounce for Jerky    
                    if trigger_counter == bounce_trigger:
                        dotPatch1._dotsDir[NrOfDots/2:NrOfDots] = copy.deepcopy(dotPatch2._dotsDir[NrOfDots/2:NrOfDots])
                        dotPatch2._dotsDir[NrOfDots/2:NrOfDots] = copy.deepcopy(dotPatch1._dotsDir[NrOfDots/2:NrOfDots])
                        trigger_counter = 0
                    dotPatch1._dotsDir[0:NrOfDots/2] += dirChange 
                    dotPatch2._dotsDir[0:NrOfDots/2] += dirChange  
                    fixation.draw()
                    dotPatch1.draw()
                    dotPatch2.draw()
                    win.flip()
                    trigger_counter += 1
                trigger_counter = 0 
                win.flip()    
                core.wait(intertrial_interval)
                promptstim.draw()
                win.flip() 
                for key in event.waitKeys(keyList = ['left', 'right', 'escape']):
                    if key in ['left']:
                        print 'left hit'
                        userkey = '0'
                    elif key in ['right']:
                        print 'right hit'
                        userkey = '1'
                    elif key in ['escape']:
                        print 'aborted'
                        userkey = 'aborted'
                        win.close()
                        core.quit()
                win.flip()
                if userkey == TrialList[trialnum][0]:
                    sin_like = '1'
                else:
                    sin_like = '0'                
                #Print data for the current trial into a line of text
                outputs = {'trialnum': trialnum+outputTRIAL, 'stimulus': TrialList[trialnum][1] , 'stimulus_location': TrialList[trialnum][0], 'response': userkey, 'more_smooth_like': sin_like, 'smooth_adapt': adaptS }
                trialnum += 1
                #Print the above line of text into the next line in the csv file    
                writer.writerow(outputs)  
#---------------------------------------------------------------------------------------------------                
            if TrialList[trialnum][1] == 'NS4' and TrialList[trialnum][0] == '1':
                print '-------'
                print 'trialnum:', trialnum+outputTRIAL
                print 'NS4 Right'
                fixation.draw()                
                win.flip()
                core.wait(1.0)                
                if adaptSJ == True:                
                    adaptation_SJ()
                    adaptS = 1
                if adaptJS == True:
                    adaptation_JS()
                    adaptS = 0
                fixation.draw()                
                win.flip()
                core.wait(1.0)
                for triallength in range(n): 
                    if event.getKeys(keyList=['escape']):
                        win.close()
                        core.quit()
                    if triallength == 1:
                        newArray40 = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])
                        
                        dotPatch1._dotsDir = copy.deepcopy(newArray40)
                        dotPatch2._dotsDir = copy.deepcopy(newArray40)

                    dotPatch1.speed = speed
                    dotPatch2.speed = speed
                    deg = random.uniform(-deg2,deg2)
                    if np.abs(dirChange) > CurveTurnRate and np.sign(deg) == np.sign(dirChange):
                        dirChange -= deg
                    else:
                        dirChange += deg
                    #Bounce for Jerky    
                    if trigger_counter == bounce_trigger:
                        dotPatch1._dotsDir[NrOfDots/2:NrOfDots] = copy.deepcopy(dotPatch2._dotsDir[NrOfDots/2:NrOfDots])
                        dotPatch2._dotsDir[NrOfDots/4*3:NrOfDots] = copy.deepcopy(dotPatch1._dotsDir[NrOfDots/4*3:NrOfDots])
                        trigger_counter = 0
                    dotPatch1._dotsDir[0:NrOfDots/2] += dirChange 
                    dotPatch2._dotsDir[0:NrOfDots/4*3] += dirChange
                    fixation.draw()
                    dotPatch1.draw()
                    dotPatch2.draw()
                    win.flip()
                    trigger_counter += 1
                trigger_counter = 0 
                win.flip()    
                core.wait(intertrial_interval)
                promptstim.draw()
                win.flip() 
                for key in event.waitKeys(keyList = ['left', 'right', 'escape']):
                    if key in ['left']:
                        print 'left hit'
                        userkey = '0'
                    elif key in ['right']:
                        print 'right hit'
                        userkey = '1'
                    elif key in ['escape']:
                        print 'aborted'
                        userkey = 'aborted'
                        win.close()
                        core.quit()
                win.flip()
                if userkey == TrialList[trialnum][0]:
                    sin_like = '1'
                else:
                    sin_like = '0'                
                #Print data for the current trial into a line of text
                outputs = {'trialnum': trialnum+outputTRIAL, 'stimulus': TrialList[trialnum][1] , 'stimulus_location': TrialList[trialnum][0], 'response': userkey, 'more_smooth_like': sin_like, 'smooth_adapt': adaptS }
                trialnum += 1
                #Print the above line of text into the next line in the csv file    
                writer.writerow(outputs)  
#---------------------------------------------------------------------------------------------------                
            if TrialList[trialnum][1] == 'S5' and TrialList[trialnum][0] == '1':
                print '-------'
                print 'trialnum:', trialnum+outputTRIAL
                print 'S5 Right'
                fixation.draw()                
                win.flip()
                core.wait(1.0)                
                if adaptSJ == True:                
                    adaptation_SJ()
                    adaptS = 1
                if adaptJS == True:
                    adaptation_JS()
                    adaptS = 0
                fixation.draw()                
                win.flip()
                core.wait(1.0)
                for triallength in range(n): 
                    if event.getKeys(keyList=['escape']):
                        win.close()
                        core.quit()
                    if triallength == 1:
                        newArray40 = np.array([random.uniform(0.,360.) for r in xrange(NrOfDots)])
                        
                        dotPatch1._dotsDir = copy.deepcopy(newArray40)
                        dotPatch2._dotsDir = copy.deepcopy(newArray40)

                    dotPatch1.speed = speed
                    dotPatch2.speed = speed
                    deg = random.uniform(-deg2,deg2)
                    if np.abs(dirChange) > CurveTurnRate and np.sign(deg) == np.sign(dirChange):
                        dirChange -= deg
                    else:
                        dirChange += deg
                    #Bounce for Jerky    
                    if trigger_counter == bounce_trigger:
                        dotPatch1._dotsDir[NrOfDots/2:NrOfDots] = copy.deepcopy(dotPatch2._dotsDir[NrOfDots/2:NrOfDots])
                        trigger_counter = 0
                    dotPatch1._dotsDir[0:NrOfDots/2] += dirChange 
                    dotPatch2._dotsDir += dirChange 
                    fixation.draw()
                    dotPatch1.draw()
                    dotPatch2.draw()
                    win.flip()
                    trigger_counter += 1
                trigger_counter = 0 
                win.flip()    
                core.wait(intertrial_interval)
                promptstim.draw()
                win.flip() 
                for key in event.waitKeys(keyList = ['left', 'right', 'escape']):
                    if key in ['left']:
                        print 'left hit'
                        userkey = '0'
                    elif key in ['right']:
                        print 'right hit'
                        userkey = '1'
                    elif key in ['escape']:
                        print 'aborted'
                        userkey = 'aborted'
                        win.close()
                        core.quit()
                win.flip()
                if userkey == TrialList[trialnum][0]:
                    sin_like = '1'
                else:
                    sin_like = '0'                
                #Print data for the current trial into a line of text
                outputs = {'trialnum': trialnum+outputTRIAL, 'stimulus': TrialList[trialnum][1] , 'stimulus_location': TrialList[trialnum][0], 'response': userkey, 'more_smooth_like': sin_like, 'smooth_adapt': adaptS }
                trialnum += 1
                #Print the above line of text into the next line in the csv file    
                writer.writerow(outputs)  
        
            if (trialnum % restinterval) == 0 and trialnum != 0 and trialnum != numreps*len(TrialType)*len(DisplayType):
                #Alternate between Sin-Cons, Cons-Sin adaptors after every rest period.                
                if adaptSJ == True:
                    adaptSJ = False
                    adaptJS = True
                elif adaptJS == True:
                    adaptJS = False
                    adaptSJ = True
                rested = True
                reststim = visual.TextStim(win, text = 'Take a break. Press SPACE to start when you are ready to continue.', pos=(0,0))
                reststim.draw()
                win.flip()
                if event.waitKeys(keyList=['space']):
                    win.flip()
            #If trial number hits 100,       
            if trialnum == numreps*len(TrialType)*len(DisplayType): 
                #Reset trial number to 0 to use the stimuli list for a second time.                 
                trialnum = 0
                #Set .csv output for trialnum to start from 101.
                outputTRIAL = numreps*len(TrialType)*len(DisplayType)+1
                #Alternate between Sin-Cons, Cons-Sin adaptors after every rest period.
                if adaptSJ == True:
                    adaptSJ = False
                    adaptJS = True
                elif adaptJS == True:
                    adaptJS = False
                    adaptSJ = True
                if trigger_rest == True: #Trigger rest when the entire stimuli list has completed for one turn 
                    reststim = visual.TextStim(win, text = 'Take a break. Press SPACE to start when you are ready to continue.', pos=(0,0))
                    reststim.draw()
                    win.flip()
                    if event.waitKeys(keyList=['space']):
                        win.flip()
                        trigger_rest = False #End the experiment and not run this function when the stimuli list is completed for the second time.
                    
                                             
                    
print '----------------------------------------------------------'
print 'The experiment has ended. Thank you for your participation.'
print '----------------------------------------------------------'




    


    