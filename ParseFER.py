#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
def ParseFER (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        logObj.event = "Frame Error Rate"
        logObj.msgType = ' '
        logObj.time = line[1]
        measureSystems=''
        
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            measureSystems = int(line[3 + NumberOfContextID])
            logObj.modeSystem = MeasureSysConverter(measureSystems)
            
        if logObj.modeSystem == 'GSM':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.FERFull = float(line[4+NumberOfContextID]) #add
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                logObj.FERSub = float(line[5+NumberOfContextID]) #add
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.FERTCH = float(line[6+NumberOfContextID]) #add
            if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                logObj.DTXDL = int(line[7+NumberOfContextID]) #add
        elif logObj.modeSystem == 'UMTS FDD':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.FER = float(line[4+NumberOfContextID]) #add

        return 1
    else:
        return 0
#     except:
#         return 0

