from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter

def ParseRABF (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2]) 
        dataOfRABF = ''
        numberOfRABRBs = 0
        logObj.event = "RAB Allocation Failed"
        logObj.msgType = 'Setup Failed'
        logObj.time = line[1] 
        rabContextID = 0
        rabType = 0
        rabFailType = 0
        numberOfHeaderParam = 0
        if (3 < length) and (line[3] != '') :
            rabContextID = int(line[3])
            dataOfRABF = 'Context ID: ' + str(rabContextID)+ ';'
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
            dataOfRABF += ('Measure System: ' + logObj.modeSystem) + ';'
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            numberOfHeaderParam = int(line[4 + NumberOfContextID])
        if numberOfHeaderParam > 0:
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                rabType = int(line[5 + NumberOfContextID])
            if rabType == 1:
                logObj.rabType = 'CS'
                dataOfRABF += 'RAB Type: CS;' 
            if rabType == 2:
                logObj.rabType = 'PS'
                dataOfRABF += 'RAB Type: PS;' 
            if numberOfHeaderParam > 1:
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.RABID = int(line[6+NumberOfContextID])
        if ((5 + NumberOfContextID + numberOfHeaderParam) < length) and (line[5+NumberOfContextID+numberOfHeaderParam] != '') :
            rabFailType = int(line[5+NumberOfContextID+numberOfHeaderParam])
            if rabFailType == 1:
                logObj.RABFailType = "LTE re-establishment cause"
                dataOfRABF += "Fail Type: LTE re-establishment cause; "
            elif rabFailType == 2:
                logObj.RABFailType = "UMTS failure cause"
                dataOfRABF += "Fail Type: UMTS failure cause; "
            elif rabFailType == 3:
                logObj.RABFailType = "UMTS ISHO failure cause"
                dataOfRABF += "Fail Type: UMTS ISHO failure cause; "
            elif rabFailType == 4:
                logObj.RABFailType = "GSM RR cause"
                dataOfRABF += "Fail Type: GSM RR cause; "
        logObj.eventInfo = dataOfRABF        
        return 1    
    else:
        return 0
#     except:
#         return 0

