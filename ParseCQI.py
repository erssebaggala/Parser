#!/usr/bin/env python
# coding: utf-8

# In[2]:


from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter


# In[26]:


def ParseCQI (line, listOfLogObj, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        logObj = LogDT()
        logObj.lat = PREVIOUS_LAT
        logObj.longg = PREVIOUS_LONG
        logObj.mcc = PREVIOUS_MCC
        logObj.mnc = PREVIOUS_MNC
        logObj.event = "Channel quality indicator"
        measureSystems=''
        numberOfCQIValues = 0 
        numberOfHeaderParamters = 0
        numberOfParametersPerCQI = 0
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            measureSystems = int(line[3 + NumberOfContextID])
            logObj.modeSystem = MeasureSysConverter(measureSystems)
            
        if logObj.modeSystem == 'UMTS FDD':
            if ((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') :
                numberOfHeaderParamters = int(line[4 + NumberOfContextID])
            if ((5 + NumberOfContextID + numberOfHeaderParamters) < length) and (line[5 + NumberOfContextID + numberOfHeaderParamters] != '') :
                numberOfCQIValues = int(line[5 + NumberOfContextID + numberOfHeaderParamters])
            if ((6 + NumberOfContextID + numberOfHeaderParamters) < length) and (line[6 + NumberOfContextID + numberOfHeaderParamters] != '') :
                numberOfParametersPerCQI = int(line[6 + NumberOfContextID + numberOfHeaderParamters])
            
            for cqi in range (0, numberOfCQIValues):
                for param in range(1, numberOfParametersPerCQI):
                    
                    if param == 2:#CQI
                        if ((6 + NumberOfContextID + numberOfHeaderParamters+param) < length) and (line[6 + NumberOfContextID + numberOfHeaderParamters+param] != '') :                     
                            logObj.CQI = int(line[6 + NumberOfContextID + numberOfHeaderParamters+param])
                    if param == 3:#CQI Type
                        if ((6 + NumberOfContextID + numberOfHeaderParamters+param) < length) and (line[6 + NumberOfContextID + numberOfHeaderParamters+param] != '') :                         
                            cqiType = int(line[6 + NumberOfContextID + numberOfHeaderParamters+param])
                        if cqiType == 1:
                            logObj.CQIType = 'CQI type A'
                        elif cqiType == 2:
                            logObj.CQIType = 'CQI type B'
                    if param == 5:#Cell Type
                        if ((6 + NumberOfContextID + numberOfHeaderParamters+param) < length) and (line[6 + NumberOfContextID + numberOfHeaderParamters+param] != '') :                         
                            cqiType = int(line[6 + NumberOfContextID + numberOfHeaderParamters+param])
                            if cqiType == 1:
                                logObj.cellType = 'Primary'
                            else:
                                logObj.cellType = 'Secondary'
                listOfLogObj.append(logObj)
            
        elif logObj.modeSystem == 'LTE FDD' or logObj.modeSystem == 'LTE TDD':
            numberOfParameters = 0
            if ((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') :
                numberOfParameters = int(line[4 + NumberOfContextID])
            
            if numberOfParameters > 2:
                if ((6 + NumberOfContextID) < length) and (line[6 + NumberOfContextID] != '') :
                    logObj.WBCQI0 = int(line[6 + NumberOfContextID])
                    
                if numberOfParameters > 3:
                    if ((7 + NumberOfContextID) < length) and (line[7 + NumberOfContextID] != '') :
                        logObj.WBCQI1 = int(line[7 + NumberOfContextID])
                    
                    if numberOfParameters > 4:
                        if ((8 + NumberOfContextID) < length) and (line[8 + NumberOfContextID] != '') :
                            logObj.SBCQI0 = int(line[8 + NumberOfContextID])
                        
                        if numberOfParameters > 5:
                            if ((9 + NumberOfContextID) < length) and (line[9 + NumberOfContextID] != '') :
                                logObj.SBCQI1 = int(line[9 + NumberOfContextID])
                                
                            if numberOfParameters > 7:
                                if ((11 + NumberOfContextID) < length) and (line[11 + NumberOfContextID] != '') :
                                    cellType = int(line[11 + NumberOfContextID])
                                    
                                    if cellType == 0:
                                        logObj.cellType = 'PCell'
                                    elif cellType == 1:
                                        logObj.cellType = 'SCell 0'
                                    elif cellType == 2:
                                        logObj.cellType = 'SCell 1'
                            
                listOfLogObj.append(logObj)
        return 1
    else:
        return 0
#     except:
#         return 0

