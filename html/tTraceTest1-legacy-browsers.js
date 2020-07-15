/******************** 
 * Ttracetest1 Test *
 ********************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'tTraceTest1';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const trialsLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopLoopBegin, trialsLoopLoopScheduler);
flowScheduler.add(trialsLoopLoopScheduler);
flowScheduler.add(trialsLoopLoopEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var trialClock;
var trialMouse;
var trialTarget;
var trialCursor;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  trialMouse = new core.Mouse({
    win: psychoJS.window,
  });
  trialMouse.mouseClock = new util.Clock();
  trialTarget = new visual.Polygon ({
    win: psychoJS.window, name: 'trialTarget', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  trialCursor = new visual.Polygon ({
    win: psychoJS.window, name: 'trialCursor', 
    edges: 180, size:[0.025, 0.025],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var trialsLoop;
var currentLoop;
function trialsLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trialsLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'tTraceCond1.xlsx',
    seed: undefined, name: 'trialsLoop'
  });
  psychoJS.experiment.addLoop(trialsLoop); // add the loop to the experiment
  currentLoop = trialsLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trialsLoop.forEach(function() {
    const snapshot = trialsLoop.getSnapshot();

    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(trialRoutineBegin(snapshot));
    thisScheduler.add(trialRoutineEachFrame(snapshot));
    thisScheduler.add(trialRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopLoopEnd() {
  psychoJS.experiment.removeLoop(trialsLoop);

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var gotValidClick;
var trialComponents;
function trialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // setup some python lists for storing info about the trialMouse
    // current position of the mouse:
    trialMouse.x = [];
    trialMouse.y = [];
    trialMouse.leftButton = [];
    trialMouse.midButton = [];
    trialMouse.rightButton = [];
    trialMouse.time = [];
    gotValidClick = false; // until a click is received
    trialMouse.mouseClock.reset();
    trialCursor.pos = [1.5, 1.5];
    trialMouse.pos = [1.5, 1.5];
    
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(trialMouse);
    trialComponents.push(trialTarget);
    trialComponents.push(trialCursor);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    
    return Scheduler.Event.NEXT;
  };
}


var prevButtonState;
var CursorTargetDistance;
var continueRoutine;
function trialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // *trialMouse* updates
    if (t >= 0.0 && trialMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialMouse.tStart = t;  // (not accounting for frame time here)
      trialMouse.frameNStart = frameN;  // exact frame index
      
      trialMouse.status = PsychoJS.Status.STARTED;
      prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
    if (trialMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      let buttons = trialMouse.getPressed();
      const xys = trialMouse.getPos();
      trialMouse.x.push(xys[0]);
      trialMouse.y.push(xys[1]);
      trialMouse.leftButton.push(buttons[0]);
      trialMouse.midButton.push(buttons[1]);
      trialMouse.rightButton.push(buttons[2]);
      trialMouse.time.push(trialMouse.mouseClock.getTime());
    }
    
    // *trialTarget* updates
    if (t >= 0.0 && trialTarget.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialTarget.tStart = t;  // (not accounting for frame time here)
      trialTarget.frameNStart = frameN;  // exact frame index
      
      trialTarget.setAutoDraw(true);
    }

    
    if (trialTarget.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialTarget.setPos([pos1, pos2]);
    }
    
    // *trialCursor* updates
    if (t >= 0.0 && trialCursor.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trialCursor.tStart = t;  // (not accounting for frame time here)
      trialCursor.frameNStart = frameN;  // exact frame index
      
      trialCursor.setAutoDraw(true);
    }

    
    if (trialCursor.status === PsychoJS.Status.STARTED){ // only update if being drawn
      trialCursor.setPos([trialMouse.getPos()[0], trialMouse.getPos()[1]]);
    }
    CursorTargetDistance = Math.sqrt((Math.pow((trialCursor.pos[0] - trialTarget.pos[0]), 2) + Math.pow((trialCursor.pos[1] - trialTarget.pos[1]), 2)));
    if ((CursorTargetDistance < 0.025)) {
        console.log(((("Target get" + " (") + globalClock.getTime().toString()) + ")"));
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('trialMouse.x', trialMouse.x);
    psychoJS.experiment.addData('trialMouse.y', trialMouse.y);
    psychoJS.experiment.addData('trialMouse.leftButton', trialMouse.leftButton);
    psychoJS.experiment.addData('trialMouse.midButton', trialMouse.midButton);
    psychoJS.experiment.addData('trialMouse.rightButton', trialMouse.rightButton);
    psychoJS.experiment.addData('trialMouse.time', trialMouse.time);
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
