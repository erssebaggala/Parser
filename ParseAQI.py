
from LogDTClass import LogDT
from ParseAQType import ParseAQType
def ParseAQI (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])     
        logObj.event = "Parse Audio quality info"
        logObj.msgType = ''
        logObj.time = line[1]  
        AQTestType = -1
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.AQMOSType = ParseAQType(int(line[3 + NumberOfContextID])) #add
            logObj.eventInfo = "MOS Type " + logObj.AQMOSType
        if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
            AQTestType = int(line[5 + NumberOfContextID])
            if AQTestType == 1:
                logObj.AQTestType = 'Loop-back'
            elif AQTestType == 2:
                logObj.AQTestType = 'Uplink'
            elif AQTestType == 3:
                logObj.AQTestType = 'Downlink'
            elif AQTestType == 4:
                logObj.AQTestType = 'Downlink/Uplink'
            elif AQTestType == 5:
                logObj.AQTestType = 'Off'
        return 1
    
    else:
        return 0
#     except:
#         return 0

