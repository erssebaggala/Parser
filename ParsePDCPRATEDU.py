#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
import copy

# In[1]:


def ParsePDCPRATEDU (line, listOfLogObj, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
    dataOfPDCPRATED = ""
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
            logObj.modeSystem = int(line[3 + NumberOfContextID])
        currentLog = LogDT()
        currentLog = copy.deepcopy(logObj)
        
        if currentLog.modeSystem == 'LTE TDD' or currentLog.modeSystem == 'LTE FDD':
            headerParams = 0
            if ((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != ''):
                headerParams = int(line[4 + NumberOfContextID])
            if headerParams > 0:
                if ((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != ''):
                    currentLog.PDCPULBitRate = int(line[5 + NumberOfContextID])
                if headerParams > 1:
                    if ((6 + NumberOfContextID) < length) and (line[6 + NumberOfContextID] != ''):
                        currentLog.PDCPULBlockRate = int(line[6 + NumberOfContextID])
                        
            numberOfRBs = 0
            if ((5 + NumberOfContextID + headerParams) < length) and (line[5 + NumberOfContextID + headerParams] != ''):
                numberOfRBs = int(line[5 + NumberOfContextID + headerParams])
            numberOfParamsPerRB = 0
            if ((6 + NumberOfContextID) < length + headerParams) and (line[6 + NumberOfContextID + headerParams] != ''):
                numberOfParamsPerRB = int(line[6 + NumberOfContextID + headerParams])
            for c in range(0,numberOfRBs):
                currentLog = LogDT()
                currentLog = copy.deepcopy(logObj)
                for p in range(0, numberOfParamsPerRB):
                    paramNumber = 7 + NumberOfContextID + (c * numberOfParamsPerRB) + p
                    if ((paramNumber) < length) and (line[paramNumber] != ''):
                        if p == 0:
                            currentLog.RBID = int(line[paramNumber])
                        elif p == 1:
                            currentLog.PDCPULBitRate = int(line[paramNumber])
                        elif p == 2:
                            currentLog.PDCPULBlockRate = int(line[paramNumber])
                listOfLogObj.append(currentLog)

        return 1
    else:
        dataOfPDCPRATED = "No of context id not found"
        return 0

