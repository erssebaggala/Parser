
import copy
from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter

def ParseRBI (line, listOfLogObj, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
    dataOfRBI = ""
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
            logObj.modeSystem = line[3 + NumberOfContextID]
            
        headerParams = 0
        if ((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != ''):
            headerParams = int(line[4 + NumberOfContextID])
        numberOfParamsPerRB = 0
        if ((5 + NumberOfContextID + headerParams) < length) and (line[5 + NumberOfContextID + headerParams] != ''):
            numberOfParamsPerRB = int(line[5 + NumberOfContextID + headerParams])
        numberOfRBs = 0
        if ((6 + NumberOfContextID + headerParams) < length) and (line[6 + NumberOfContextID + headerParams] != ''):
            numberOfRBs = int(line[6 + NumberOfContextID + headerParams])

        for c in range (0, numberOfRBs):
            currentLog = LogDT()
            currentLog = copy.deepcopy(logObj)
                
            for p in range(0,numberOfParamsPerRB):
                paramNumber = 6 + NumberOfContextID + (c * numberOfParamsPerRB) + p
                if ((paramNumber) < length) and (line[paramNumber] != '') :
                    if p == 0:#RB ID
                        if currentLog.modeSystem == 'UMTS FDD':
                            currentLog.RBID = int(line[paramNumber]) 
                    elif p == 3:#Direction
                        if currentLog.modeSystem == 'UMTS FDD':
                            if int(line[paramNumber]) == 0:
                                currentLog.direction = 'Uplink'
                            elif int(line[paramNumber]) == 1:
                                currentLog.direction = 'Downlink'
                    elif p == 4:#Logical Channel
                        if currentLog.modeSystem == 'UMTS FDD':
                            if int(line[paramNumber]) == 0:
                                currentLog.direction = 'BCCH'
                            elif int(line[paramNumber]) == 1:
                                currentLog.direction = 'PCCH'
                            elif int(line[paramNumber]) == 2:
                                currentLog.direction = 'CCCH' 
                            elif int(line[paramNumber]) == 3:
                                currentLog.direction = 'DCCH' 
                            elif int(line[paramNumber]) == 4:
                                currentLog.direction = 'CTCH' 
                            elif int(line[paramNumber]) == 5:
                                currentLog.direction = 'DTCH' 
                            elif int(line[paramNumber]) == 6:
                                currentLog.direction = 'SHCCH' 
                    elif p == 5:#RLC mode
                        if currentLog.modeSystem == 'UMTS FDD':
                            if int(line[paramNumber]) == 0:
                                currentLog.RLCMode = 'TM'
                            elif int(line[paramNumber]) == 1:
                                currentLog.RLCMode = 'UM'
                            elif int(line[paramNumber]) == 2:
                                currentLog.RLCMode = 'AM'
                    elif p == 6:#Radio Bearer Ciphering
                        if currentLog.modeSystem == 'UMTS FDD':
                            if int(line[paramNumber]) == 0:
                                currentLog.RBCiphering = 'Disabled'
                            elif int(line[paramNumber]) == 1:
                                currentLog.RBCiphering = 'Enabled'
                    elif p == 7:#TrCh Type
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
                                
            listOfLogObj.append(currentLog)

        return 1
    else:
        dataOfRBI = "No of context id not found"
        return 0


# In[ ]:




