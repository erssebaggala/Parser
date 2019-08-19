#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:

import copy
from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from ParseCellMeasuresParseBand import parseCellMeasuresParseBand
from ParseCellTypeJ import ParseCellTypeJ
from ParseModulation import parseModulation

# In[72]:


def ParsePLAIUV27 (line, listOfLogObj,PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
    dataOfCELLMEAS = ""
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        contextID = 'Unknown'
        numberOfHeaderParamters = 0
        numberOfCells = 0
        numberOfParametersPerCell = 0
        measureSystem = 'Unknown'
        if (3 < length) and (line[3] != ''):
            contextID = line[3]
            
        
        
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            measureSystem = line[3+NumberOfContextID]
            measureSystem = MeasureSysConverter(int(measureSystem))
            if measureSystem == '"UMTS FDD':
                if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                    numberOfHeaderParamters = int(line[4+NumberOfContextID])
                    
                currentLog = LogDT()
                dataOfCELLMEAS = "Context ID:"+contextID
                currentLog.eventInfo = dataOfCELLMEAS
                currentLog.modeSystem = measureSystem
                currentLog.event = 'Packet link adaptation info for uplink'
                currentLog.lat = PREVIOUS_LAT
                currentLog.longg = PREVIOUS_LONG
                currentLog.mcc = PREVIOUS_MCC
                currentLog.mnc = PREVIOUS_MNC
                
                for header in range(1,numberOfHeaderParamters):
                    if ((4 + NumberOfContextID + header) < length) and (line[4+NumberOfContextID + header] != '') :
                        celltype = line[4+NumberOfContextID + header]
                        if header == 2:#E-DPDCH Rate
                            currentLog.EDPDCHRate = int(line[4+NumberOfContextID + header])
                        if header == 8:
                            if celltype == '1':
                                currentLog.cellType = "Primary"
                            elif celltype == '2':
                                currentLog.cellType = "Secondary"
                            
                
                numberOfPLASets = 0
                if ((5 + NumberOfContextID + numberOfHeaderParamters) < length) and (line[5 + NumberOfContextID + numberOfHeaderParamters] != '') :
                    numberOfPLASets = int(line[5 + NumberOfContextID + numberOfHeaderParamters])
                parametersPerPLASet = 0
                if ((6 + NumberOfContextID + numberOfHeaderParamters) < length) and (line[6 + NumberOfContextID + numberOfHeaderParamters] != '') :
                    numberOfPLASets = int(line[6 + NumberOfContextID + numberOfHeaderParamters])
                original = currentLog
                
                for channel in range(0,numberOfPLASets):    
                    currentLog = LogDT()
                    currentLog = copy.deepcopy(original)
                    
                    for parameter in range(0,parametersPerPLASet):
                        if ((NumberOfContextID + 7 + numberOfHeaderParamters + parameter) < length) and (line[NumberOfContextID + 7 + numberOfHeaderParamters + parameter]) :
                            value = int(line[NumberOfContextID + 7 + numberOfHeaderParamters + parameter])
                        if parameter == 1:#Modulation
                            currentLog.Modulation = parseModulation(value,'HSUPA')
                        elif parameter == 4:#SFs
                            if value == 1:
                                currentLog.SFs = "SF 256"
                            elif value == 2:
                                currentLog.SFs = "SF 128" 
                            elif value == 3:
                                currentLog.SFs = "SF 64" 
                            elif value == 4:
                                currentLog.SFs = "SF 32" 
                            elif value == 5:
                                currentLog.SFs = "SF 16" 
                            elif value == 6:
                                currentLog.SFs = "SF 8" 
                            elif value == 7:
                                currentLog.SFs = "SF 4" 
                            elif value == 8:
                                currentLog.SFs = "2 * SF 4"
                            elif value == 9:
                                currentLog.SFs = "2 * SF 2" 
                            elif value == 10:
                                currentLog.SFs = "2 * SF 4 and 2 * SF 2"
                                                                                                              
                        elif parameter == 5:#retransmission rate per LA
                            currentLog.ReTransmissionPerLA = float(value)                                                                                    
                                                                                                           
                    listOfLogObj.append(currentLog) 
                               
            elif measureSystem == "LTE FDD" or measureSystem == "LTE TDD":
                                                                                                              
                currentLog = LogDT()
                dataOfCELLMEAS = "Context ID:"+contextID
                currentLog.eventInfo = dataOfCELLMEAS
                currentLog.modeSystem = measureSystem
                currentLog.event = 'Packet link adaptation info for uplink'
                currentLog.lat = PREVIOUS_LAT
                currentLog.longg = PREVIOUS_LONG
                currentLog.mcc = PREVIOUS_MCC
                currentLog.mnc = PREVIOUS_MNC
                original = currentLog                                                                             
                numberOfHeaderParamters = 0                                                                                          
                if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                    numberOfHeaderParamters = int(line[4+NumberOfContextID])
                                                                                                              
                numberOfPLASets = 0
                if ((5 + NumberOfContextID + numberOfHeaderParamters) < length) and (line[5 + NumberOfContextID + numberOfHeaderParamters] !=''):
                    numberOfPLASets = int(line[5 + NumberOfContextID + numberOfHeaderParamters])
                if ((6 + NumberOfContextID + numberOfHeaderParamters) < length) and (line[6 + NumberOfContextID + numberOfHeaderParamters] !=''):
                    parametersPerPLASet = int(line[6 + NumberOfContextID + numberOfHeaderParamters])
                 
                for channel in range (0,numberOfPLASets):
                    currentLog = LogDT()
                    currentLog = copy.deepcopy(original)
                                                                                     
                    for parameter in range(0,parametersPerPLASet):
                        if ((NumberOfContextID + 7 + numberOfHeaderParamters + parameter) < length) and (line[NumberOfContextID + 7 + numberOfHeaderParamters + parameter]) :
                            value = line[NumberOfContextID + 7 + numberOfHeaderParamters + parameter]
                        if parameter == 2:
                            currentLog.Modulation = parseModulation(value,'PUSCH')
                        elif parameter == 3:#MCS0
                            currentLog.MCS0 = int(value)                                                                                                           
                    listOfLogObj.append(currentLog)
                                                        
        return 1
    else:
        dataOfCELLMEAS = "No of context id not found"
        currentLog.eventInfo = dataOfCELLMEAS
        listOfLogObj.append(currentLog)
        
        return 1
#     except:
#         return 0


# In[ ]:




