#!/usr/bin/env python
# coding: utf-8

# In[1]:
# Parse Call Connect Success
# Parameter | Parameters for GSM | Parameters for TETRA
# Items Sequence
# 1.  EventID = CAC                   [0]
# 2.  Time                            [1]
# 3.  Call Context ID                 [2] = N
# 3a. Call Context ID                 [N]
# 4.  Measured System                 [3+N]
# 5.  Call Type                       [4+N]
# 6.  Call Connection Status          [5+N]
# 7.  Additional Parameters Count     [6+N]
# CASE GSM
# 8.  TSL                             [7+N]
# CASE TETRA
# 8.  TSL                             [7+N]

#This will have a dictionary of all the Call Context IDs
#atm, dictionary is accumulating all the data from Calls
#present

from MeasureSysConverter import MeasureSysConverter
from ParseCallTypes import ParseCallType
from LogDTClass import LogDT
from CallContextId import CallContextID


# In[4]:


def ParseCAC (line, logObj,dictionary):
    try: 
        dataOfCAC = ""
        length = len(line)
        if 2 < length:
            contextID = "UnKnown"
            measureSystem = "UnKnown"
            callType = "UnKnown"
            callDirection = "UnKnown"
            callConnStatus = "Unknown"
            callTimeOut = "UnKnown"
            uniqueID = "UnKnown"
            CACTimeCorrection = "UnKnown"
            timeSetup = 0
            additionalParameter = ""

            logObj.time = line[1]
            NumberOfContextID = int(line[2])
            if (3 < length) and (line[3] != ''):
                contextID = line[3]
            if contextID in dictionary:
                callContextObj = dictionary[contextID]
            else:
                callContextObj = CallContextID()
                dictionary[contextID] = callContextObj
                callContextObj = dictionary[contextID]

            if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
                measureSystem = line[3+NumberOfContextID]
                measureSystem = MeasureSysConverter(int(measureSystem))
            if ((4+NumberOfContextID) < length) and (line[4+NumberOfContextID] != ''):
                callType = line[4+NumberOfContextID]
                callType = ParseCallType(int(callType))
            if ((5+NumberOfContextID) < length) and (line[5+NumberOfContextID] != ''):
                callConnStatus = line[5+NumberOfContextID]
            if ((6+NumberOfContextID) < length) and (line[6+NumberOfContextID] != ''):
                additionalParameter = int(line[6+NumberOfContextID])

                if callConnStatus == '1':
                    callConnectionStatus = 'Traffic Channel Allocated'
                    logObj.direction = callContextObj.Direction 
                    logObj.msgType = 'Alerting'
                    logObj.event = callConnectionStatus

                elif callConnStatus == '2':
                    callConnectionStatus = 'Alerting'
                    if logObj.time != '-10675199.02:48:05.4775808':
                        callContextObj.CallSetup = logObj.time
                        logObj.direction = callContextObj.Direction
                        logObj.msgType = callConnectionStatus
                        timeSetup = logObj.time[-3:]
                    logObj.event = 'Call Setup'

                elif callConnStatus == '3':
                    callConnectionStatus = 'Connected'
                    if logObj.time != '-10675199.02:48:05.4775808':
                        callContextObj.CallEstablished = logObj.time
                        logObj.direction = callContextObj.Direction
                        logObj.msgType = 'Connect'
                    logObj.event = 'Call Established'

                elif callConnStatus == '4':
                    callConnectionStatus = 'Dial-up connection established'
                    if logObj.time != '-10675199.02:48:05.4775808':
                        callContextObj.CallEstablished = logObj.time
                        logObj.direction = callContextObj.Direction
                        logObj.msgType = 'Connect'
                    logObj.event = 'Call Established'


            dataOfCAC = "Context ID:"+contextID+';'+callConnectionStatus+";Call Type:"+callType+";Measure System:"+measureSystem
            if int(timeSetup) > 0:
                dataOfCAC += ";Setup time:"+timeSetup
            if (additionalParameter > 0) and ((7+NumberOfContextID) < length) and (line[7+NumberOfContextID] != ''): 
                if measureSystem == 'GSM' or measureSystem == 'TETRA':
                    dataOfCAC += "Time slot number:"+line[7+NumberOfContextID]
                    
            dataOfCAC += ';Direction:'+logObj.direction
            logObj.eventInfo = dataOfCAC
            logObj.modeSystem = measureSystem
            return 1
        else:
            dataOfCAC = "No of context id not found"
            return 0
    except:
        return 0


