#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
def ParseAMRI (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])        
        logObj.event = "AMR Information"
        logObj.msgType = ''
        logObj.time = line[1]  
        chi = 0
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        if logObj.modeSystem == 'GSM':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.AMRInitMode = line[4 + NumberOfContextID]
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                chi = int(line[5 + NumberOfContextID])
                if chi == 0:
                    logObj.AMRICMI = "Implicit rule"
                elif chi == 1:
                    logObj.AMRICMI = "RATSCCH/L3"
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.AMRTH1 = float(line[6 + NumberOfContextID])
            if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                logObj.AMRHYS1 = float(line[7 + NumberOfContextID])
            if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                logObj.AMRTH2 = float(line[8 + NumberOfContextID])
            if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
                logObj.AMRHYS2 = float(line[9 + NumberOfContextID])
            if ((10 + NumberOfContextID) < length) and (line[10+NumberOfContextID] != '') :
                logObj.AMRTH3 = float(line[10 + NumberOfContextID])
            if ((11 + NumberOfContextID) < length) and (line[11+NumberOfContextID] != '') :
                logObj.AMRHYS3 = float(line[11 + NumberOfContextID])
            if ((12 + NumberOfContextID) < length) and (line[12+NumberOfContextID] != '') :
                logObj.ActiveAMRCodecCount = int(line[12 + NumberOfContextID])
            if ((13 + NumberOfContextID) < length) and (line[13+NumberOfContextID] != '') :
                logObj.AMRCodec = line[13 + NumberOfContextID]
        return 1
    
    else:
        return 0
#     except:
#         return 0

