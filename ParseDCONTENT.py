from LogDTClass import LogDT
from ParseApplicationProtocol import ParseApplicationProtocol
def ParseDCONTENT (line, logObj):
    length = len(line)
    if 2 < length:
        applicationProtocol = "Unknown"
        NumberOfContextID = int(line[2])
        streamStateInt = -1
        logObj.event = "Data Content"
        logObj.msgType = ' '
        logObj.time = line[1]
        if (3 < length) and (line[3] != ''):
            dataTranferContextID = line[3]

        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.applicationProtocol = line[3 + NumberOfContextID]
            applicationProtocol = ParseApplicationProtocol(int(logObj.applicationProtocol))
        return 1
    else:
        return 0
#     except:
#         return 0

