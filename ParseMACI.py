#!/usr/bin/env python
# coding: utf-8

# In[2]:

import copy
from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from ParseCellTypeJ import ParseCellTypeJ

# In[26]:


def ParseMACI (line, listOfLogObj,PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
    dataOfMACI = ""
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        contextID = 'Unknown'
        measureSystem = 'Unknown'
        logDTObj = LogDT()
        logDTObj.lat = PREVIOUS_LAT
        logDTObj.longg = PREVIOUS_LONG
        logDTObj.mcc = PREVIOUS_MCC
        logDTObj.mnc = PREVIOUS_MNC
        logDTObj.event = 'Parse MAC layer info'
        if (3 < length) and (line[3] != ''):
            contextID = line[3]
            
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            measureSystem = line[3+NumberOfContextID]
            logDTObj.modeSystem = MeasureSysConverter(int(measureSystem))
            
        numberOfCells = 0
        if ((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') :
            numberOfCells = int(line[4 + NumberOfContextID])
        if ((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') :
            numberOfParameterPerCell = int(line[5 + NumberOfContextID])
            
        for cell in range(0,numberOfCells):
            currentLog = LogDT()
            currentLog = copy.deepcopy(logDTObj)

            for parameter in range(0,numberOfParameterPerCell):
                paramNumber = NumberOfContextID + 6 + (cell * numberOfParameterPerCell) + parameter
                if ((paramNumber) < length) and (line[paramNumber] != '') :

                    if parameter == 0:
                        if currentLog.modeSystem == 'UMTS FDD':
                            if line[paramNumber] == '2':
                                currentLog.cellType = 'Secondary'
                        elif currentLog.modeSystem == 'LTE FDD' or currentLog.modeSystem == 'LTE TDD':
                            currentLog.cellType = ParseCellTypeJ(line[paramNumber],currentLog.modeSystem)

                    elif parameter == 1:
                        if line[paramNumber] == '0':
                            currentLog.cellState = 'Deactivate'
                        elif line[paramNumber] == '1':
                            currentLog.cellState = 'Activate'
            listOfLogObj.append(currentLog)
                            
        return 1
    else:
        return 0
#     except:
#         return 0

