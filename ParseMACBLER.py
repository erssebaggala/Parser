#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import copy
from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
def ParseMACBLER (line, listOfLogObj, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
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
        logObj.event = "Parse MAC layer Block Error Rate"
        logObj.msgType = ''
        logObj.time = line[1]  
        headerParameters = 0
        numberOfTrChs = 0 
        numberOfParamsPerTrCh = 0
        cellType = 0
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        if logObj.modeSystem == 'UMTS FDD':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                headerParameters = int(line[4 + NumberOfContextID])
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                numberOfTrChs = int(line[5 + NumberOfContextID])
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                numberOfParamsPerTrCh = int(line[6 + NumberOfContextID])
            for c in range(0,numberOfTrChs):
                currentObj = LogDT()
                currentObj = copy.deepcopy(logObj)
                if ((7 + NumberOfContextID + headerParameters + (c * numberOfParamsPerTrCh) + 3) < length) and (line[7 + NumberOfContextID + headerParameters + (c * numberOfParamsPerTrCh) + 3] != '') :
                    currentObj.MAChsBLER = float(line[7 + NumberOfContextID + headerParameters + (c * numberOfParamsPerTrCh) + 3])
                if ((7 + NumberOfContextID + headerParameters + (c * numberOfParamsPerTrCh) + 6) < length) and (line[7 + NumberOfContextID + headerParameters + (c * numberOfParamsPerTrCh) + 6] != '') :
                    cellType = int(line[7 + NumberOfContextID + headerParameters + (c * numberOfParamsPerTrCh) + 6])
                    if cellType == 1:
                        currentObj.cellType = "Primary"
                    else:
                        currentObj.cellType = "Secondary"
                listOfLogObj.append(currentObj)
        return 1
    
    else:
        return 0
#     except:
#         return 0

