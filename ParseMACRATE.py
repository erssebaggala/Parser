#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
import copy

def ParseMACRATE (line, listOfLogObj, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
    
    dataOfMACRATE = ""
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
        logObj.event = "Parse MAC layer throughput downlink"
        logObj.msgType = ''
        logObj.time = line[1]  
        headerParameters = 0
        numberOfTrChs = 0 
        numberOfParamsPerTrCh = 0
        cellType = 0
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
            dataOfMACRATE += ('Measure System: ' + logObj.modeSystem) + ';'
        headerParameters = 0
        if logObj.modeSystem == 'UMTS FDD':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                headerParameters = int(line[4 + NumberOfContextID])
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID + headerParameters] != '') :
                numberOfTrChs = int(line[5 + NumberOfContextID])
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID + headerParameters] != '') :
                numberOfParamsPerTrCh = int(line[6 + NumberOfContextID])
            for c in range(0,numberOfTrChs):
                currentObj = LogDT()
                currentObj = copy.deepcopy(logObj)
                if ((7 + NumberOfContextID + headerParameters + (c * numberOfParamsPerTrCh) + 2) < length) and (line[7 + NumberOfContextID + headerParameters + (c * numberOfParamsPerTrCh) + 2] != '') :
                    currentObj.MAChsBitRate = int(line[7 + NumberOfContextID + headerParameters + (c * numberOfParamsPerTrCh) + 2])
                if ((7 + NumberOfContextID + headerParameters + (c * numberOfParamsPerTrCh) + 8) < length) and (line[7 + NumberOfContextID + headerParameters + (c * numberOfParamsPerTrCh) + 8] != '') :
                    cellType = int(line[7 + NumberOfContextID + headerParameters + (c * numberOfParamsPerTrCh) + 8])
                    if cellType == 1:
                        currentObj.cellType = "Primary"
                    else:
                        currentObj.cellType = "Secondary"
                listOfLogObj.append(currentObj)
        elif logObj.modeSystem == 'LTE FDD' or logObj.modeSystem == 'LTE TDD':
            
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.MACDLBitRate = int(line[4 + NumberOfContextID])
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.MACDLBLER = float(line[6 + NumberOfContextID])
            if ((13 + NumberOfContextID) < length) and (line[13+NumberOfContextID] != '') :
                cellType = int(line[13 + NumberOfContextID])
                if cellType == 0:
                    logObj.cellType = 'PCell'
                elif cellType == 1:
                    logObj.cellType = 'SCell 0'
                elif cellType == 2:
                    logObj.cellType = 'SCell 1'
            listOfLogObj.append(logObj)
        return 1
    
    else:
        dataOfMACRATE = "No of context id not found"
        return 0
#     except:
#         return 0

