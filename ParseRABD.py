from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter

def ParseRABD (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2]) 
        dataOfRABD = ''
        numberOfRABRBs = 0
        logObj.event = "RAB Release"
        logObj.msgType = 'Complete'
        logObj.time = line[1] 
        rabContextID = 0
        rabType = 0
        rabFailType = 0
        numberOfHeaderParam = 0
        if (3 < length) and (line[3] != '') :
            rabContextID = int(line[3])
            dataOfRABD = 'Context ID: ' + str(rabContextID)+ ';'
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
            dataOfRABD += ('Measure System: ' + logObj.modeSystem) + ';'
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            numberOfHeaderParam = int(line[4 + NumberOfContextID])
        if numberOfHeaderParam > 0:
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                rabType = int(line[5 + NumberOfContextID])
            if rabType == 1:
                logObj.rabType = 'CS'
                dataOfRABD += 'RAB Type: CS;' 
            if rabType == 2:
                logObj.rabType = 'PS'
                dataOfRABD += 'RAB Type: PS;' 
            if numberOfHeaderParam > 1:
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.RABID = int(line[6+NumberOfContextID])
        if ((5 + NumberOfContextID + numberOfHeaderParam) < length) and (line[5+NumberOfContextID+numberOfHeaderParam] != '') :
            rabFailType = int(line[5+NumberOfContextID+numberOfHeaderParam])
            if rabFailType == 1:
                logObj.RABRelaseType = "Network Release"
                dataOfRABD += "Release Type: Network Release; "
            elif rabFailType == 2:
                logObj.RABRelaseType = "UE Release"
                dataOfRABD += "Release Type: UE Release; "
        logObj.eventInfo = dataOfRABD        
        return 1    
    else:
        return 0
#     except:
#         return 0

