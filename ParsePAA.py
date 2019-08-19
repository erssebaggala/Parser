#!/usr/bin/env python
# coding: utf-8

# In[1]:

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from PacketSessionInfo import PacketSessionInfo
from ParseApplicationProtocol import ParseApplicationProtocol

def ParsePAA (line, logObj,packetDictionary):
    dataOfPAA = ''
    length = len(line)
    packetConnectionContextID = 0
    initiator = -1
    protocolType = -1
    headerCompression = -1
    compression = -1
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])  
            
        logObj.event = "Packet Session Connection Attempt"
        logObj.msgType = "Setup"
        logObj.time = line[1]   
        if (3 < length) and (line[3] != '') :
            packetConnectionContextID = int(line[3]) 
            dataOfPAA = 'Packet Connection ID: ' + str(packetConnectionContextID) + ';'
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.applicationProtocol = ParseApplicationProtocol(int(line[3 + NumberOfContextID])) #add
        if NumberOfContextID > 0:
            if packetConnectionContextID in packetDictionary:
                packetInfo = packetDictionary[packetConnectionContextID]
            else:
                packetInfo = PacketSessionInfo()
                packetDictionary[packetConnectionContextID] = packetInfo
                packetInfo = packetDictionary[packetConnectionContextID]
            packetInfo.AttemptTime = line[1]
            packetInfo.applicationProtocol = logObj.applicationProtocol
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            initiator = int(line[4+NumberOfContextID])
            if initiator == 1:
                logObj.PSInitiator = "Mobile station initiated"
            elif initiator == 2:
                logObj.PSInitiator = "Network station initiated"
            else:
                logObj.PSInitiator = "Unknown"
            dataOfPAA += 'Initiator: ' + logObj.PSInitiator + ';'
        if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
            protocolType = int(line[5+NumberOfContextID])
            if protocolType == 1:
                logObj.PSProtocolType = "Mobile station initiated"
            else:
                logObj.PSProtocolType = "Unknown"
            dataOfPAA += 'Protocol Type: ' + logObj.PSInitiator + ';'
        if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') and (line[6+NumberOfContextID] != '""') :
            logObj.APN = line[6+NumberOfContextID]
            dataOfPAA += 'APN: ' + logObj.APN + ';'
        if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') and (line[7+NumberOfContextID] != '""'):
            logObj.staticIP = line[7+NumberOfContextID]
            dataOfPAA += 'Static IP: ' + logObj.staticIP + ';'
        if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
            headerCompression = int(line[8+NumberOfContextID])
            if headerCompression == 0:
                logObj.HeaderCompression = "Off"
            elif headerCompression == 1:
                logObj.HeaderCompression = "On (manufacturer preferred compression) "
            elif headerCompression == 2:
                logObj.HeaderCompression = "RFC1144 (VanJacobsen)"
            elif headerCompression == 3:
                logObj.HeaderCompression = "RFC2507 (Degermark)"
            elif headerCompression == 4:
                logObj.HeaderCompression = "RFC3095 (RoHC)"
            else:
                logObj.HeaderCompression = "Unknown"
            dataOfPAA += 'Header Compression: ' + logObj.HeaderCompression + ';'
        if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
            compression = int(line[9+NumberOfContextID])
            if compression == 0:
                logObj.compression = "Off"
            elif compression == 1:
                logObj.compression = "On (manufacturer preferred compression) "
            elif compression == 2:
                logObj.compression = "V.42bis"
            elif compression == 3:
                logObj.compression = "V.44"
            else:
                logObj.HeaderCompression = "Unknown"
            dataOfPAA += 'Compression: ' + logObj.compression + ';'
        logObj.eventInfo = dataOfPAA
        return 1    
    else:
        return 0
#     except:
#         return 0          


# In[ ]:




