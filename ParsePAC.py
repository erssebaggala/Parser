#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from LogDTClass import LogDT
from ParseApplicationProtocol import ParseApplicationProtocol
from datetime import datetime

def ParsePAC (line, logObj,packetDictionary):
    dataOfPAC = ''
    length = len(line)
    packetConnectionContextID = 0
    initiator = -1
    protocolType = -1
    headerCompression = -1
    compression = -1
    recievedIP = -1
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        logObj.event = "Packet Session Connection Success"
        logObj.msgType = "Connected"
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
            packetInfo.SuccessTime = line[1]
            if packetInfo.SuccessTime !='' and packetInfo.AttemptTime != '':
                tdelta = datetime.strptime(packetInfo.SuccessTime.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(packetInfo.AttemptTime.split('.', 1)[0], '%H:%M:%S')        
            connectionTime = float(tdelta.seconds)*1000 #MilliSeconds 
            dataOfPAC += 'Connection Time: ' + str(connectionTime) + ';'
            packetInfo.applicationProtocol = logObj.applicationProtocol
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            initiator = int(line[4+NumberOfContextID])
            if initiator == 1:
                dataOfPAC += "PS Activation State: Air longerface connected (in session management layer); "
            elif initiator == 2:
                dataOfPAC += "PS Activation State: Packet session activated; "
        if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') and (line[5+NumberOfContextID] != '""') :
            recievedIP = line[5+NumberOfContextID]
            dataOfPAC += 'Recieved IP: ' + recievedIP + ';'
        logObj.eventInfo = dataOfPAC
        return 1    
    else:
        return 0
#     except:
#         return 0     

