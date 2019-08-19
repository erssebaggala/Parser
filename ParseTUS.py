
import copy
from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
def ParseTUS (line, listOfLogObj, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC):
    
    dataOfTUS = ""
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        TUSContextID = 0
        numberOfTAC = 0
        parameterPerTAC = 0
        logObj = LogDT()
        logObj.lat = PREVIOUS_LAT
        logObj.longg = PREVIOUS_LONG
        logObj.mcc = PREVIOUS_MCC
        logObj.mnc = PREVIOUS_MNC
        logObj.event = "Tracking Area Update Succcesful"
        logObj.msgType = 'Succces'
        logObj.time = line[1]  
        if (3  < length) and (line[3] != '') :
            TUSContextID = line[3]
            dataOfTUS = "TAU Context ID: " + TUSContextID + ';'
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
            dataOfTUS += ('Measure System: ' + logObj.modeSystem) + ';'
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            numberOfTAC = int(line[4 + NumberOfContextID])
        if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
            parameterPerTAC = int(line[5 + NumberOfContextID])
        for c in range(0,numberOfTAC):
            if c > 0:
                dataOfTUS += (", [")
            else:
                dataOfTUS += ("Parameters: [")
            currentObj = LogDT()
            currentObj = copy.deepcopy(logObj)
            
            if ((6 + NumberOfContextID + (c * parameterPerTAC)+0) < length) and (line[6 + NumberOfContextID + (c * parameterPerTAC)+0] != '') :
                currentObj.mcc = int(line[6 + NumberOfContextID + (c * parameterPerTAC)+0])
                dataOfTUS += ("MCC: " + str(currentObj.mcc))
            if ((6 + NumberOfContextID + (c * parameterPerTAC)+1) < length) and (line[6 + NumberOfContextID + (c * parameterPerTAC)+1] != '') :
                currentObj.mnc = int(line[6 + NumberOfContextID + (c * parameterPerTAC)+1])
                dataOfTUS += ("MNC: " + str(currentObj.mnc))
            if ((6 + NumberOfContextID + (c * parameterPerTAC)+2) < length) and (line[6 + NumberOfContextID + (c * parameterPerTAC)+2] != '') :
                currentObj.TAC = int(line[6 + NumberOfContextID + (c * parameterPerTAC)+2])#add
                dataOfTUS += ("TAC: " + str(currentObj.TAC))
            dataOfTUS += (']')
            if c < (numberOfTAC-1):
                listOfLogObj.append(currentObj)
            else:
                currentObj.eventInfo = dataOfTUS 
                listOfLogObj.append(currentObj)
        return 1
    
    else:
        dataOfTUS = "No of context id not found"
        return 0
#     except:
#         return 0

