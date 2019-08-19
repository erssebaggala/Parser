from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from ParseMEILteParseMeasurementEvent import parseMEILteParseMeasurementEvent
from ParseMEIUmtsFddParseMeasurementEvent import parseMEIUmtsFddParseMeasurementEvent
def ParseMEI (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        logObj.event = "Measurement Event Information"
        logObj.msgType = ' '
        logObj.time = line[1]
        measureSystems=''
        measurementEvent = 0
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            measureSystems = int(line[3 + NumberOfContextID])
            logObj.modeSystem = MeasureSysConverter(measureSystems)
            
        if logObj.modeSystem == 'UMTS FDD':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                measurementEvent = int(line[4+NumberOfContextID]) #add
                logObj.MeasurementEvent = parseMEIUmtsFddParseMeasurementEvent(measurementEvent) #addd
        elif logObj.modeSystem == 'LTE FDD' or logObj.modeSystem == 'LTE TDD':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                measurementEvent = int(line[4+NumberOfContextID]) #add
                logObj.MeasurementEvent = parseMEILteParseMeasurementEvent(measurementEvent) #addd
                                
        return 1
    else:
        return 0
#     except:
#         return 0

