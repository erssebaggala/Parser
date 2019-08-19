#!/usr/bin/env python
# coding: utf-8

# In[11]:

# Parse Call Attempt
# Items Sequence
# 1.  EventID = CAA            [0]
# 2.  Time                     [1]
# 3.  Call Context ID Count    [2] = N
# 3a. Call Context ID          [N]
# 4.  Measured System          [3+N]
# 5.  Call Type                [4+N]
# 6.  Call Direction           [5+N]
# 7.  Phone Number             [6+N]
# 8.  Own Phone Number         [7+N]
# 9.  Call Timeout             [8+N]
# 10. Unique ID                [9+N]
# 11. CAA Timeout              [10+N]

#This will have a dictionary of all the Call Context IDs
#atm, dictionary is accumulating all the data from Calls
#present

from MeasureSysConverter import MeasureSysConverter
from ParseCallTypes import ParseCallType
from LogDTClass import LogDT
from CallContextId import CallContextID


# In[12]:



def ParseCAA (line, logObj,dictionary):
    try:  
        dataOfCAA = ""
        length = len(line)
        if 2 < length:

            contextID = "UnKnown"
            measureSystem = "UnKnown"
            callType = "UnKnown"
            callDirection = "UnKnown"
            phoneNumber = "UnKnown"
            ownPhoneNumber = "UnKnown"
            callTimeOut = "UnKnown"
            uniqueID = "UnKnown"
            CAATimeCorrection = "UnKnown"

            NumberOfContextID = int(line[2])
            if (3 < length) and (line[3] != ''):
                #context ID will be unique for every call setup
                contextID = line[3]
            if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
                measureSystem = line[3+NumberOfContextID]
                measureSystem = MeasureSysConverter(int(measureSystem))
            if ((4+NumberOfContextID) < length) and (line[4+NumberOfContextID] != ''):
                callType = line[4+NumberOfContextID]
                callType = ParseCallType(int(callType))
            if ((5+NumberOfContextID) < length) and (line[5+NumberOfContextID] != ''):
                callDirection = line[5+NumberOfContextID]
                if callDirection == '1':
                    callDirection = 'Originated Call To'
                else:
                    callDirection = 'Terminated Call From'

            if ((6+NumberOfContextID) < length) and (line[6+NumberOfContextID] != ''):
                phoneNumber = line[6+NumberOfContextID]
            if ((7+NumberOfContextID) < length) and (line[7+NumberOfContextID] != ''):
                ownPhoneNumber = line[7+NumberOfContextID]
            if ((8+NumberOfContextID) < length) and (line[8+NumberOfContextID] != ''):
                callTimeOut = line[8+NumberOfContextID]
            if ((9+NumberOfContextID) < length) and (line[9+NumberOfContextID] != ''):
                uniqueID = line[9+NumberOfContextID]
            if (10+NumberOfContextID) < length:
                CAATimeCorrection = line[10+NumberOfContextID]


            dataOfCAA = "Context ID:"+contextID+";Measure System:"+measureSystem+";Call Type:"+callType+";Call Direction:" +callDirection+";Phone Number:"+phoneNumber+";Own Phone No:"+ownPhoneNumber+";Call Time Out:"+callTimeOut+";Unique ID:"+uniqueID+";CAA Time Correction:"+CAATimeCorrection

            logObj.eventInfo = dataOfCAA
            logObj.event = 'Call Attempt'
            logObj.msgType = 'Setup'
            logObj.modeSystem = measureSystem
            logObj.time = line[1]

            if callDirection == 'Originated Call To':
                logObj.direction = "UL"
            elif callDirection == 'Terminated Call From':
                logObj.direction = 'DL'
            else:
                logObj.direction = "Unknown call direction"
                
            if contextID in dictionary:
                callContextObj = dictionary[contextID]
                callContextObj.CallAttempt = line[1]
                callContextObj.Direction = logObj.direction
            else:
                callContextObj = CallContextID()
                callContextObj.CallAttempt = line[1]
                callContextObj.Direction = logObj.direction
                dictionary.update({contextID : callContextObj})
            return 1

        else:
            dataOfCAA = "No of context id not found"
            return 0
    except:
        return 0



# In[ ]:




