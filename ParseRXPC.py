#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
def ParseRXPC (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        logObj.event = "RX power control"
        logObj.msgType = ' '
        logObj.time = line[1]
        measureSystems=''
        bsDivState = 0
        dpcMode = 0
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            measureSystems = int(line[3 + NumberOfContextID])
            logObj.modeSystem = MeasureSysConverter(measureSystems)
            
        if logObj.modeSystem == 'UMTS FDD':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.SIRTarget = float(line[4+NumberOfContextID]) #add
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                logObj.SIR = float(line[5+NumberOfContextID]) #add
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                bsDivState = int(line[6+NumberOfContextID]) #add
                if bsDivState == 0:
                    lobObj.BSDivState = "Not active"#add
                elif bsDivState == 1:
                    lobObj.BSDivState = "Closed loop mode 1"#add
                elif bsDivState == 2:
                    lobObj.BSDivState = "Closed loop mode 2"#add
            if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                logObj.DLPwrUpsNum = int(line[7+NumberOfContextID]) #add
            if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                logObj.DLPwrDownsNum = int(line[8+NumberOfContextID]) #add
            if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
                logObj.DLPwrUpPercent = float(line[9+NumberOfContextID]) #add
            if ((10 + NumberOfContextID) < length) and (line[10+NumberOfContextID] != '') :
                dpcMode = int(line[10+NumberOfContextID]) #add
                if dpcMode == 0:
                    lobObj.DpcMode = "Unique TPC command in each slot"#add
                else:
                    lobObj.DpcMode = "Same TPC command repeated over three slots"#add
                
        return 1
    else:
        return 0
#     except:
#         return 0

