﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on July 15, 2020, at 16:05
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'tTraceTest1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andrew\\Documents\\Work\\Projects\\tTraceTest1\\tTraceTest1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialMouse = event.Mouse(win=win)
x, y = [None, None]
trialMouse.mouseClock = core.Clock()
trialTarget = visual.Polygon(
    win=win, name='trialTarget',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
trialCursor = visual.Polygon(
    win=win, name='trialCursor',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trialsLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('tTraceCond1.xlsx'),
    seed=None, name='trialsLoop')
thisExp.addLoop(trialsLoop)  # add the loop to the experiment
thisTrialsLoop = trialsLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop.rgb)
if thisTrialsLoop != None:
    for paramName in thisTrialsLoop:
        exec('{} = thisTrialsLoop[paramName]'.format(paramName))

for thisTrialsLoop in trialsLoop:
    currentLoop = trialsLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop.rgb)
    if thisTrialsLoop != None:
        for paramName in thisTrialsLoop:
            exec('{} = thisTrialsLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the trialMouse
    trialMouse.x = []
    trialMouse.y = []
    trialMouse.leftButton = []
    trialMouse.midButton = []
    trialMouse.rightButton = []
    trialMouse.time = []
    gotValidClick = False  # until a click is received
    trialMouse.mouseClock.reset()
    trialCursor.pos = (1.5,1.5)
    trialMouse.pos = (1.5,1.5)
    # keep track of which components have finished
    trialComponents = [trialMouse, trialTarget, trialCursor]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *trialMouse* updates
        if trialMouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialMouse.frameNStart = frameN  # exact frame index
            trialMouse.tStart = t  # local t and not account for scr refresh
            trialMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialMouse, 'tStartRefresh')  # time at next scr refresh
            trialMouse.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if trialMouse.status == STARTED:  # only update if started and not finished!
            x, y = trialMouse.getPos()
            trialMouse.x.append(x)
            trialMouse.y.append(y)
            buttons = trialMouse.getPressed()
            trialMouse.leftButton.append(buttons[0])
            trialMouse.midButton.append(buttons[1])
            trialMouse.rightButton.append(buttons[2])
            trialMouse.time.append(trialMouse.mouseClock.getTime())
        
        # *trialTarget* updates
        if trialTarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialTarget.frameNStart = frameN  # exact frame index
            trialTarget.tStart = t  # local t and not account for scr refresh
            trialTarget.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialTarget, 'tStartRefresh')  # time at next scr refresh
            trialTarget.setAutoDraw(True)
        if trialTarget.status == STARTED:  # only update if drawing
            trialTarget.setPos((pos1, pos2), log=False)
        
        # *trialCursor* updates
        if trialCursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trialCursor.frameNStart = frameN  # exact frame index
            trialCursor.tStart = t  # local t and not account for scr refresh
            trialCursor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trialCursor, 'tStartRefresh')  # time at next scr refresh
            trialCursor.setAutoDraw(True)
        if trialCursor.status == STARTED:  # only update if drawing
            trialCursor.setPos((trialMouse.getPos()[0], trialMouse.getPos()[1]), log=False)
        CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTarget.pos[0])**2 + (trialCursor.pos[1]-trialTarget.pos[1])**2)
        
        if (CursorTargetDistance < .05):
                print('Target get'+' ('+str(globalClock.getTime())+')')
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trialsLoop (TrialHandler)
    trialsLoop.addData('trialMouse.x', trialMouse.x)
    trialsLoop.addData('trialMouse.y', trialMouse.y)
    trialsLoop.addData('trialMouse.leftButton', trialMouse.leftButton)
    trialsLoop.addData('trialMouse.midButton', trialMouse.midButton)
    trialsLoop.addData('trialMouse.rightButton', trialMouse.rightButton)
    trialsLoop.addData('trialMouse.time', trialMouse.time)
    trialsLoop.addData('trialMouse.started', trialMouse.tStartRefresh)
    trialsLoop.addData('trialMouse.stopped', trialMouse.tStopRefresh)
    trialsLoop.addData('trialTarget.started', trialTarget.tStartRefresh)
    trialsLoop.addData('trialTarget.stopped', trialTarget.tStopRefresh)
    trialsLoop.addData('trialCursor.started', trialCursor.tStartRefresh)
    trialsLoop.addData('trialCursor.stopped', trialCursor.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trialsLoop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
