#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter

def ParseRABC (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2]) 
        dataOfRABC = ''
        numberOfRABRBs = 0
        logObj.event = "RAB Allocation Success"
        logObj.msgType = 'Setup'
        logObj.time = line[1] 
        rabContextID = 0
        rabType = 0
        numberOfHeaderParam = 0
        if (3 < length) and (line[3] != '') :
            rabContextID = int(line[3])
            dataOfRABC = 'Context ID: ' + str(rabContextID)+ ';'
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
            dataOfRABC += ('Measure System: ' + logObj.modeSystem) + ';'
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            numberOfHeaderParam = int(line[4 + NumberOfContextID])
        if numberOfHeaderParam > 0:
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                rabType = int(line[5 + NumberOfContextID])
            if rabType == 1:
                logObj.rabType = 'CS'
                dataOfRABC += 'RAB Type: CS;' 
            if rabType == 2:
                logObj.rabType = 'PS'
                dataOfRABC += 'RAB Type: PS;' 
            if numberOfHeaderParam > 1:
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.RABID = int(line[6+NumberOfContextID])
        logObj.eventInfo = dataOfRABC        
        return 1    
    else:
        return 0
#     except:
#         return 0

