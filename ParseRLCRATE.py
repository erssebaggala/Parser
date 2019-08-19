#!/usr/bin/env python
# coding: utf-8

# In[1]:

import copy
from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
# In[1]:


def ParseRLCRATE (line, listOfLogObj, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
    dataOfRLCRATE = ""
    length = len(line)
    if 2 < length:
        logObj = LogDT()
        logObj.lat = PREVIOUS_LAT
        logObj.longg = PREVIOUS_LONG
        logObj.mcc = PREVIOUS_MCC
        logObj.mnc = PREVIOUS_MNC
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])        
        logObj.time = line[1]  
        if ((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != ''):
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        currentLog = LogDT()
        currentLog = copy.deepcopy(logObj)
        if currentLog.modeSystem == 'GSM':
            if ((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != ''):
                logObj.RLCRateUL = int(line[4 + NumberOfContextID])
            if ((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != ''):
                logObj.RLCRateDL = int(line[5 + NumberOfContextID])
            if ((6 + NumberOfContextID) < length) and (line[6 + NumberOfContextID] != ''):
                logObj.RLCRetransmissionUL = float(line[6 + NumberOfContextID])
                
        if currentLog.modeSystem == 'UMTS FDD' or currentLog.modeSystem == 'UMTS TD-SCDMA':
            if ((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != ''):
                logObj.RLCRateUL = int(line[4 + NumberOfContextID])
            if ((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != ''):
                logObj.RLCRateDL = int(line[5 + NumberOfContextID])
            if ((6 + NumberOfContextID) < length) and (line[6 + NumberOfContextID] != ''):
                logObj.RLCRetransmissionUL = float(line[6 + NumberOfContextID])
            
            numberOfRBs = 0
            if ((7 + NumberOfContextID) < length) and (line[7 + NumberOfContextID] != ''):
                numberOfRBs = int(line[7 + NumberOfContextID])
            numberOfParamsPerRB = 0
            if ((8 + NumberOfContextID) < length) and (line[8 + NumberOfContextID] != ''):
                numberOfParamsPerRB = int(line[8 + NumberOfContextID])

            for c in range(0,numberOfRBs):
                currentLog = LogDT()
                currentLog = copy.deepcopy(logObj)
                listOfLogObj.append(currentLog)
                for p in range(0, numberOfParamsPerRB):
                    paramNumber = 9 + NumberOfContextID + (c * numberOfParamsPerRB) + p
                    if ((paramNumber) < length) and (line[paramNumber] != ''):
                        if p == 0:
                            currentLog.RBID = float(line[paramNumber])
                        elif p == 1:
                            currentLog.RLCRateUL = int(line[paramNumber])
                        elif p == 2:
                            currentLog.RLCRateDL = int(line[paramNumber])
                        elif p == 3:
                            currentLog.RLCRetransmissionUL = float(line[paramNumber])
                listOfLogObj.append(currentLog)

        
        if currentLog.modeSystem == 'LTE FDD' or currentLog.modeSystem == 'LTE TDD':
            headerParams = 0
            if ((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != ''):
                headerParams = int(line[4 + NumberOfContextID])
            if headerParams > 0:
                if ((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != ''):
                    currentLog.RLCRateDL = int(line[5 + NumberOfContextID])
                if headerParams > 1:
                    if ((6 + NumberOfContextID) < length) and (line[6 + NumberOfContextID] != ''):
                        currentLog.RLCDLBlockRate = int(line[6 + NumberOfContextID])
                    if headerParams > 2:
                        if ((7 + NumberOfContextID) < length) and (line[7 + NumberOfContextID] != ''):
                            currentLog.RLCDLBLER = float(line[7 + NumberOfContextID])
            
            numberOfRBs = 0
            if ((5 + NumberOfContextID + headerParams) < length) and (line[5 + NumberOfContextID + headerParams] != ''):
                numberOfRBs = int(line[5 + NumberOfContextID + headerParams])
                
            numberOfParamsPerRB = 0
            if ((6 + NumberOfContextID + headerParams) < length) and (line[6 + NumberOfContextID + headerParams] != ''):
                numberOfParamsPerRB = int(line[6 + NumberOfContextID + headerParams])
                
            for c in range(0,numberOfRBs):
                currentLog = LogDT()
                currentLog = copy.deepcopy(logObj)
                for p in range(0, numberOfParamsPerRB):
                    paramNumber = 7 + NumberOfContextID + (c * numberOfParamsPerRB) + p
                    if ((paramNumber) < length) and (line[paramNumber] != ''):
                        if p == 0:
                            currentLog.RBID = float(line[paramNumber])
                        elif p == 1:
                            currentLog.RLCRateDL = int(line[paramNumber])
                        elif p == 2:
                            currentLog.RLCDLBlockRate = float(line[paramNumber])
                        elif p == 3:
                            currentLog.RLCDLBLER = float(line[paramNumber])   
                
                listOfLogObj.append(currentLog)

        return 1
    else:
        dataOfRLCRATE = "No of context id not found"
        return 0

