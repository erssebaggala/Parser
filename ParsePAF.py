
from LogDTClass import LogDT
from ParseApplicationProtocol import ParseApplicationProtocol
from ParsePSDisconnectionCause import ParsePSDisconnectionCause
from datetime import datetime

def ParsePAF (line, logObj,packetDictionary):
    dataOfPAC = ''
    length = len(line)
    packetConnectionContextID = 0
    psFailStatus = -1
    cause = ''
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])  
        logObj.event = "Packet Session Connection Failed"
        logObj.msgType = "Failure"
        logObj.time = line[1]   
        if (3 < length) and (line[3] != '') :
            packetConnectionContextID = int(line[3]) 
            dataOfPAC = 'Packet Connection ID: ' + str(packetConnectionContextID) + ';'
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.applicationProtocol = ParseApplicationProtocol(int(line[3 + NumberOfContextID])) #add
        if NumberOfContextID > 0:
            if packetConnectionContextID in packetDictionary:
                packetInfo = packetDictionary[packetConnectionContextID]
            else:
                packetInfo = PacketSessionInfo()
                packetDictionary[packetConnectionContextID] = packetInfo
                packetInfo = packetDictionary[packetConnectionContextID]
            packetInfo.FailureTime = line[1]
            if packetInfo.FailureTime !='' and packetInfo.AttemptTime != '':
                tdelta = datetime.strptime(packetInfo.FailureTime.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(packetInfo.AttemptTime.split('.', 1)[0], '%H:%M:%S')        
            connectionTime = float(tdelta.seconds)*1000 #MilliSeconds 
            dataOfPAC += 'Connection Failure Time: ' + str(connectionTime) + ';'
            packetInfo.applicationProtocol = logObj.applicationProtocol
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            psFailStatus = int(line[4+NumberOfContextID])
            if psFailStatus == 1:
                psFailStatus = 'User abort'
            elif psFailStatus == 2:
                psFailStatus = 'Network reject (SM cause)'
            elif psFailStatus == 3:
                psFailStatus = 'Mobile reject (SM cause)'
            elif psFailStatus == 4:
                psFailStatus = 'Timeout'
            elif psFailStatus == 5:
                psFailStatus = 'PPP error (OS RAS cause)'
            elif psFailStatus == 6:
                psFailStatus = 'Test system failure (OS RAS cause) '
            elif psFailStatus == 7:
                psFailStatus = 'No service'
            else:
                psFailStatus = 'Unknown'
            dataOfPAC += 'Fail Status: ' + psFailStatus + ';'
        if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
            cause = ParsePSDisconnectionCause(int(line[5+NumberOfContextID])) #add
            dataOfPAC += 'Cause: ' + cause + ';'
        logObj.eventInfo = dataOfPAC
        return 1    
    else:
        return 0
#     except:
#         return 0     


# In[ ]:




