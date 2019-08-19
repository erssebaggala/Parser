

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
def ParseMACRATEU (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        logObj.event = "Parse MAC layer throughput uplink"
        logObj.msgType = ''
        logObj.time = line[1]  
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        if logObj.modeSystem == 'LTE FDD' or logObj.modeSystem == 'LTE TDD':
            
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.MACULBitRate = int(line[4 + NumberOfContextID])
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.MACULRetr = float(line[6 + NumberOfContextID])
        return 1
    
    else:
        dataOfTAU = "No of context id not found"
        return 0
#     except:
#         return 0

