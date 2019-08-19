#!/usr/bin/env python
# coding: utf-8

# In[1]:

import copy
from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter

# In[3]:


def ParseTRCHI (line, listOfLogObj, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
    dataOfTRCHI = ""
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
            
        headerParams = 0
        if ((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != ''):
            headerParams = int(line[4 + NumberOfContextID])
        numberOfParamsPerTrCh = 0
        if ((5 + NumberOfContextID + headerParams) < length) and (line[5 + NumberOfContextID + headerParams] != ''):
            numberOfParamsPerTrCh = int(line[5 + NumberOfContextID + headerParams])
        numberOfTrChs = 0
        if ((6 + NumberOfContextID + headerParams) < length) and (line[6 + NumberOfContextID + headerParams] != ''):
            numberOfTrChs = int(line[6 + NumberOfContextID + headerParams])

        for c in range (0, numberOfTrChs):
            currentLog = LogDT()
            currentLog = copy.deepcopy(logObj)
                
            for p in range(0,numberOfParamsPerTrCh):
                paramNumber = 6 + NumberOfContextID + (c * numberOfParamsPerTrCh) + p
                if ((paramNumber) < length) and (line[paramNumber] != '') :
                    if p == 0:#TrCh ID
                        if currentLog.modeSystem == 'UMTS FDD':
                            currentLog.TrChID = int(line[paramNumber]) 
                    elif p == 2:#Direction
                        if currentLog.modeSystem == 'UMTS FDD':
                            if int(line[paramNumber]) == 0:
                                currentLog.direction = 'Uplink'
                            elif int(line[paramNumber]) == 1:
                                currentLog.direction = 'Downlink'
                            elif int(line[paramNumber]) == 2:
                                currentLog.direction = 'Relay-link'
                    elif p == 3:#TrCh Type
                        if currentLog.modeSystem == 'UMTS FDD':
                            if int(line[paramNumber]) == 0:
                                currentLog.TrChType = 'BCH'
                            elif int(line[paramNumber]) == 1:
                                currentLog.TrChType = 'CPCH'
                            elif int(line[paramNumber]) == 2:
                                currentLog.TrChType = 'DCH'
                            elif int(line[paramNumber]) == 3:
                                currentLog.TrChType = 'HS-DSCH'
                            elif int(line[paramNumber]) == 4:
                                currentLog.TrChType = 'PCH'
                            elif int(line[paramNumber]) == 5:
                                currentLog.TrChType = 'FACH'
                            elif int(line[paramNumber]) == 6:
                                currentLog.TrChType = 'RACH'
                            elif int(line[paramNumber]) == 7:
                                currentLog.TrChType = 'E-DCH'
                    elif p == 4:#TrCh Coding
                        if currentLog.modeSystem == 'UMTS FDD':
                            if int(line[paramNumber]) == 0:
                                currentLog.TrChCoding = '1/2 and convolutional'
                            elif int(line[paramNumber]) == 1:
                                currentLog.TrChCoding = '1/3 and convolutional'
                            elif int(line[paramNumber]) == 2:
                                currentLog.TrChCoding = '1/3 and turbo'
                            elif int(line[paramNumber]) == 3:
                                currentLog.TrChCoding = 'No coding'
                    elif p == 6:#TTI
                        if currentLog.modeSystem == 'UMTS FDD':
                            currentLog.TTI = int(line[paramNumber]) 
                                
            listOfLogObj.append(currentLog)

        return 1
    else:
        dataOfTRCHI = "No of context id not found"
        return 0


# In[ ]:




