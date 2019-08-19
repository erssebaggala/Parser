#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter

def ParseTXPC (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        logObj.event = "TX power control"
        logObj.msgType = ' '
        logObj.time = line[1]
        measureSystems=''
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            measureSystems = int(line[3 + NumberOfContextID])
            logObj.modeSystem = MeasureSysConverter(measureSystems)
            
        if logObj.modeSystem == 'GSM':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.TXPower = float(line[4+NumberOfContextID]) #add
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                if int((line[5+NumberOfContextID])) == 0:
                    lobObj.TXPwrCtrlAlgo = "Power control algorithm 0"#add
                else:
                    lobObj.TXPwrCtrlAlgo = "Power control algorithm 1"#add
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.TXPwrCtrlStep = float(line[6+NumberOfContextID]) #add
            if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                if int((line[7+NumberOfContextID])) == 0:
                    lobObj.CompressMode = "No Compressed mode"#add
                else:
                    lobObj.CompressMode = "Compressed mode"#add
            if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                logObj.ULPwrUpsNum = int(line[8+NumberOfContextID]) #add
            if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
                logObj.ULPwrDownsNum = int(line[9+NumberOfContextID]) #add
            if ((10 + NumberOfContextID) < length) and (line[10+NumberOfContextID] != '') :
                logObj.ULPwrUpPercent = float(line[10+NumberOfContextID]) #add
        elif logObj.modeSystem == 'LTE FDD' or logObj.modeSystem == 'LTE TDD':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.PUSCHTXPower = float(line[4+NumberOfContextID]) #add
                
        return 1
    else:
        return 0
#     except:
#         return 0

