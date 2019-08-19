
from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter

def ParseVCHI (line,logObj):
    
    dataOfVCHI = ""
    callContextIDCount = 0
    logObj.event = "Voice Channel Information"
    if line[2] != '':
        callContextIDCount = line[2]
        
    if callContextIDCount == 1 and line[3] != '':
        callContextID = line[3]
        dataOfVCHI += "Call Context ID: "+callContextID
        
    if ((3 + callContextIDCount) < length) and (line[3+callContextIDCount] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + callContextIDCount]))
            
    dataOfVCHI += ";Measured System: "+logObj.modeSystem