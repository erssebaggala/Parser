#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from ParseAQType import ParseAQType
def ParseAQUL (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])        
        logObj.event = "Parse Audio quality uplink"
        logObj.msgType = ''
        logObj.time = line[1]  
        logObj.direction = 'UL'
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.AQMOSType = ParseAQType(int(line[3 + NumberOfContextID])) #add
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            logObj.AQMOS = float(line[4 + NumberOfContextID]) #add
        if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
            logObj.AQTimestamp = line[7 + NumberOfContextID] #add
        if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
            logObj.AQSampleDurationUL = float(line[9 + NumberOfContextID]) #add
        if ((13 + NumberOfContextID) < length) and (line[13+NumberOfContextID] != '') :
            logObj.AQStdevDelay = float(line[13 + NumberOfContextID]) #add
        return 1
    
    else:
        return 0
#     except:
#         return 0

