#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter

def ParseSEI (line, logObj):
    dataOfSEI = ""
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        SEIType = 0
        mmCause = 0
        logObj.event = "Service Information"
        logObj.msgType = ''
        logObj.time = line[1]  
                   
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            SEIType = int(line[4+NumberOfContextID]) #add
            if SEIType == 1:
                dataOfSEI = 'Service received'
            elif SEIType == 2:
                dataOfSEI = 'Service dropped'
        if logObj.modeSystem == 'GSM' or logObj.modeSystem == 'UMTS FDD' or logObj.modeSystem == 'UMTS TD-SCDMA' or logObj.modeSystem == 'LTE FDD' or logObj.modeSystem == 'LTE TDD':
            
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                logObj.LAC = int(line[5+NumberOfContextID]) #add
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.mcc = line[6+NumberOfContextID] #add  
            if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                logObj.mnc = int(line[7+NumberOfContextID]) #add
            if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                logObj.TMSI = line[8+NumberOfContextID] #add
               
        logObj.eventInfo = dataOfSEI 
        return 1
    
    else:
        dataOfSEI = "No of context id not found"
        return 0
#     except:
#         return 0

