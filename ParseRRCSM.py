#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from RadioResourceInfo import RadioResourceInfo
from MeasureSysConverter import MeasureSysConverter


# In[3]:


def ParseRRCSM (line, logObj):
    length = len(line)
    if 2 < length:
        dataOfRRCSM = ''
        RRCSMContextID = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') :
                    RRCSMContextID = int(line[3])
        logObj.direction = 'NA'
        
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') : 
            measureSystem = MeasureSysConverter (int(line[3 + NumberOfContextID]))          

        if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
            cause = line[4 + NumberOfContextID]
            if cause == '1':
                logObj.direction = 'UL'
            elif cause == '2':
                logObj.direction = 'DL'
        if((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') : 
                logObj.RRCMessage = line[5 + NumberOfContextID]
        if((6 + NumberOfContextID) < length) and (line[6 + NumberOfContextID] != '') : 
                logObj.SubChannel = line[6 + NumberOfContextID]
        if((9 + NumberOfContextID) < length) and (line[9 + NumberOfContextID] != '') : 
                logObj.RRCData = line[9 + NumberOfContextID]
        if logObj.event != '':
            logObj.event = logObj.RRCMessage
        
        if measureSystem == 'UMTS FDD' or measureSystem == 'UMTS TD-SCDMA':
            if((7 + NumberOfContextID) < length) and (line[7 + NumberOfContextID] != '') : 
                logObj.UARFCN = line[7 + NumberOfContextID]
            if((8 + NumberOfContextID) < length) and (line[8 + NumberOfContextID] != '') : 
                logObj.SC = line[8 + NumberOfContextID]
    
        if measureSystem == 'LTE FDD' or measureSystem == 'LTE TDD':
            if((7 + NumberOfContextID) < length) and (line[7 + NumberOfContextID] != '') : 
                logObj.EARFCN = line[7 + NumberOfContextID]
            if((8 + NumberOfContextID) < length) and (line[8 + NumberOfContextID] != '') : 
                logObj.PCI = line[8 + NumberOfContextID]
        logObj.modeSystem = measureSystem
                                                 
        return 1

