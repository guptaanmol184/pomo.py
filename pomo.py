#!/usr/bin/env python3

import gtts
import os
import time

# set default values
workTime = 25           # value in minutes
breakTime = 5           # value in minutes

# COnvert to seconds for usage with time.time()
workTimeSec = workTime * 60
breakTimeSec = breakTime * 60

# alert text
workTimerStartAlertText = 'Work time started. Work timer has been set for ' + str(workTime) + ' minutes. Work hard.'
breakTimerStartAlertText = 'Work time over. Break timer has been set for ' + str(breakTime) + ' minutes. Have fun.'

# work timer start alert
workTimerStartAlert =  gtts.gTTS(text = workTimerStartAlertText, lang = 'en')
workTimerStartAlert.save('/var/tmp/workTimerStartAlert.mp3')
os.system('mpg123 /var/tmp/workTimerStartAlert.mp3')

# run the  work clock
startTime = time.time()    # store the starting time
while time.time() != startTime + workTimeSec:
    pass

# break timer start alert
breakTimerStartAlert = gtts.gTTS(text = breakTimerStartAlertText, lang = 'en')
breakTimerStartAlert.save('/var/tmp/breakTimerStartAlert.mp3')
os.system('mpg123 /var/tmp/breakTimerStartAlert.mp3')

# run the break clock
startTime = time.time()    # store the starting time
while time.time() != startTime + breakTimeSec:
    pass