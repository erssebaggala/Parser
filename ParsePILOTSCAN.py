#!/usr/bin/env python
# coding: utf-8

# In[1]:
import copy
from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from ParseCellMeasuresParseBand import parseCellMeasuresParseBand

def ParsePILOTSCAN (line, listOfLogObj, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
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
        logObj.event = "Pilot Scanning results"
        logObj.msgType = ''
        logObj.time = line[1] 
        numberOfHeaderParameters = 0
        channelType = -1
        numberOfCells = 0
        parameterPerCell = 0
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        if logObj.modeSystem == "UMTS FDD":
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                numberOfHeaderParameters = int(line[4+NumberOfContextID])
            if numberOfHeaderParameters > 0:
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    logObj.ChannelNum = int(line[5+NumberOfContextID]) #add
            if numberOfHeaderParameters > 1:
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    channelType = int(line[6+NumberOfContextID]) #add
                    if channelType == 1:
                        logObj.channelType = 'CPICH'
                    elif channelType == 2:
                        logObj.channelType = 'P SCH'
                    elif channelType == 3:
                        logObj.channelType = 'S SCH'
                    elif channelType == 4:
                        logObj.channelType = 'CPICH (TX diversity)'
                    elif channelType == 5:
                        logObj.channelType = 'PPCH'
            if numberOfHeaderParameters > 2:
                if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                    logObj.RSSI = float(line[7+NumberOfContextID]) #add
            if numberOfHeaderParameters > 3:
                if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                    logObj.Band = parseCellMeasuresParseBand(int(line[8+NumberOfContextID])) #add
           
            if ((5 + NumberOfContextID + numberOfHeaderParameters) < length) and (line[5+NumberOfContextID+numberOfHeaderParameters] != '') :
                numberOfCells = int(line[5+NumberOfContextID+numberOfHeaderParameters]) 
            if ((6 + NumberOfContextID + numberOfHeaderParameters) < length) and (line[6+NumberOfContextID+numberOfHeaderParameters] != '') :
                parameterPerCell = int(line[6+NumberOfContextID+numberOfHeaderParameters]) 
            if numberOfCells == 0:
                listOfLogObj.append(logObj)
                
            for i in range(0,numberOfCells):
                currentObj = LogDT()
                currentObj = copy.deepcopy(logObj)
                if ((7 + NumberOfContextID + numberOfHeaderParameters + (i * parameterPerCell) + 0) < length) and (line[7 + NumberOfContextID + numberOfHeaderParameters + (i * parameterPerCell) + 0] != '') :
                    currentObj.scramblingCode = float(line[7 + NumberOfContextID + numberOfHeaderParameters + (i * parameterPerCell) + 0])
                if ((7 + NumberOfContextID + numberOfHeaderParameters + (i * parameterPerCell) + 1) < length) and (line[7 + NumberOfContextID + numberOfHeaderParameters + (i * parameterPerCell) + 1] != '') :
                    currentObj.ServingCPICHEcNo = float(line[7 + NumberOfContextID + numberOfHeaderParameters + (i * parameterPerCell) + 1])
                if ((7 + NumberOfContextID + numberOfHeaderParameters + (i * parameterPerCell) + 2) < length) and (line[7 + NumberOfContextID + numberOfHeaderParameters + (i * parameterPerCell) + 2] != '') :
                    currentObj.ServingCPICHRSCP = float(line[7 + NumberOfContextID + numberOfHeaderParameters + (i * parameterPerCell) + 2])
                if ((7 + NumberOfContextID + numberOfHeaderParameters + (i * parameterPerCell) + 3) < length) and (line[7 + NumberOfContextID + numberOfHeaderParameters + (i * parameterPerCell) + 3] != '') :
                    currentObj.SIR = float(line[7 + NumberOfContextID + numberOfHeaderParameters + (i * parameterPerCell) + 3])
               
                listOfLogObj.append(currentObj)
        return 1 
    
    else:
        return 0
#     except:
#         return 0


# In[ ]:




