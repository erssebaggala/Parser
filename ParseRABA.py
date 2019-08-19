#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
import copy

def ParseRABA (line, listOfLogObj, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2]) 
        dataOfRAA = ''
        numberOfRABRBs = 0
        logObj = LogDT()
        logObj.lat = PREVIOUS_LAT
        logObj.longg = PREVIOUS_LONG
        logObj.mcc = PREVIOUS_MCC
        logObj.mnc = PREVIOUS_MNC
        logObj.event = "RAB Allocation Attempt"
        logObj.msgType = 'Attempt'
        logObj.time = line[1] 
        rabContextID = 0
        rabType = 0
        numberOfHeaderParam = 0
        if (3 < length) and (line[3] != '') :
            rabContextID = int(line[3])
            dataOfRAA = 'Context ID: ' + str(rabContextID)+ ';'
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
            dataOfRAA += ('Measure System: ' + logObj.modeSystem) + ';'
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            numberOfHeaderParam = int(line[4 + NumberOfContextID])
        if numberOfHeaderParam > 0:
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                rabType = int(line[5 + NumberOfContextID])
            if rabType == 1:
                logObj.rabType = 'CS'
                dataOfRAA += 'RAB Type: CS;' 
            if rabType == 2:
                logObj.rabType = 'PS'
                dataOfRAA += 'RAB Type: PS;' 
            if numberOfHeaderParam > 1:
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.RABID = int(line[6+NumberOfContextID])
        if ((5 + NumberOfContextID + numberOfHeaderParam) < length) and (line[5+NumberOfContextID+numberOfHeaderParam] != '') :
            numberOfRABRBs = int(line[5 + NumberOfContextID + numberOfHeaderParam]) 
        logObj.eventInfo = dataOfRAA
        if numberOfRABRBs == 0:
            listOfLogObj.append(logObj)
        for i in range(0,numberOfRABRBs):
            currentObj = LogDT()
            currentObj = copy.deepcopy(logObj)
            if ((6 + NumberOfContextID + numberOfHeaderParam + i) < length) and (line[6 + NumberOfContextID + numberOfHeaderParam + i] != '') :
                currentObj.RABRBID = int(line[6 + NumberOfContextID + numberOfHeaderParam + i])
            listOfLogObj.append(currentObj)
        return 1    
    else:
        return 0
#     except:
#         return 0

