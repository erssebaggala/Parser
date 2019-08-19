#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from ParseCellMeasuresParseBand import parseCellMeasuresParseBand
import copy

# In[2]:


def ParseNLIST (line, listOfLogObj, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
    dataOfNLIST = ""
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
        headerParams = 0
        
        logObj.time = line[1]  
        if ((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != ''):
            headerParams = int(line[3 + NumberOfContextID])
            currentLog = LogDT()
            currentLog = copy.deepcopy(logObj)
        for h in range(0,headerParams):
            paramNumber = h + 4 + NumberOfContextID
            if ((paramNumber) < length) and (line[paramNumber] != '') :
                if h == 0:
                    currentLog.cellType = "Serving";
                    currentLog.modeSystem = MeasureSysConverter(line[paramNumber]) 
                elif h == 1:
                    currentLog.Band = parseCellMeasuresParseBand(items[paramNumber])
                elif h == 2:
                    currentLog.ChannelNum = int(line[paramNumber]); 
                elif h == 3:
                    if currentLog.modeSystem == 'GSM':
                        currentLog.BSIC = int(items[paramNumber])
                    elif currentLog.modeSystem == 'UMTS FDD':
                        currentLog.SC = int(items[paramNumber])
                    elif currentLog.modeSystem == 'UMTS TD-SCDMA':
                        currentLog.CellParameterID = int(items[paramNumber])
        listOfLogObj.append(currentLog)
            
            
        numberOfNeighbourChannels = 0
        if ((4 + NumberOfContextID + headerParams) < length) and (line[4 + NumberOfContextID + headerParams] != '') :
            numberOfNeighbourChannels = int(line[4 + NumberOfContextID + headerParams])
            
            for c in range (0, numberOfNeighbourChannels):
                numberOfParamsPerChannel = 0
                if ((5 + NumberOfContextID + headerParams) < length) and (line[5 + NumberOfContextID + headerParams] != '') :
                    numberOfParamsPerChannel = int(line[5 + NumberOfContextID + headerParams])
                currentLog = LogDT()
                currentLog = copy.deepcopy(logObj)
                for p in range(0,numberOfParamsPerChannel):
                    paramNumber = 6 + NumberOfContextID + headerParams + (c * numberOfParamsPerChannel) + p
                    
                    if ((paramNumber) < length) and (line[paramNumber] != '') :
                        if p == 0:
                            currentLog.cellType = "Neighbor";
                            currentLog.modeSystem = MeasureSysConverter(line[paramNumber]) 
                        elif p == 1:
                            if currentLog.modeSystem == 'GSM':
                                currentLog.NeighbourARFCN = int(line[paramNumber])
                            elif currentLog.modeSystem == 'UMTS TD-SCDMA' or currentLog.modeSystem == 'UMTS FDD':
                                currentLog.UARFCN = int(line[paramNumber])    
                        elif p == 2:
                            if currentLog.modeSystem == 'GSM':
                                currentLog.BSIC = int(items[paramNumber])
                            elif currentLog.modeSystem == 'UMTS FDD':
                                currentLog.SC = int(items[paramNumber])
                            elif currentLog.modeSystem == 'UMTS TD-SCDMA':
                                currentLog.CellParameterID = int(items[paramNumber])
                        elif p== 3:
                            currentLog.Band = parseCellMeasuresParseBand(line[paramNumber])
                        elif p== 4:
                            currentLog.NeighbourCellIndex = int(line[paramNumber])
                listOfLogObj.append(currentLog)

        return 1
    else:
        dataOfNLIST = "No of context id not found"
        return 0


# In[ ]:




