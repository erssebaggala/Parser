#!/usr/bin/env python
# coding: utf-8

# In[49]:

# Data Connection Attempt
# Parameters
# Items Sequence
# 1.  EventID = DAA               [0]
# 2.  Time                        [1]
# 3.  Context ID Count            [2] = N
# 3a. Data Connection Context ID  [N 1]
# 3b. Packet Session Context ID   [N 2]
# 3c. Call Context ID             [N 3]
# 4.  Application Protocol        [3+N]
# 5.  Host Address                [4+N]
# 6.  Host Port                   [5+N]
# 7.  Connection Timeout          [6+N]
# 8.  Security Protocol           [7+N]
# 9.  Authentication Scheme       [8+N]

#This will have a dictionary of all the DATA Connection Context IDs
#atm, dictionary is accumulating all the data from data connections
#present

from LogDTClass import LogDT
from DataConnectionEventInfo import DataConnectionEventInfo
from ParseApplicationProtocol import ParseApplicationProtocol


# In[50]:


def ParseDAA (line, logObj, dictionary):
    try:
        dataOfDAA = ""
        length = len(line)
        if 2 < length:
            dataConnectionContextID = "UnKnown"
            packetConnectionContextID = "UnKnown"
            callConnectionContextID = "Unknown"
            hostAddress = "Unknown"
            securityProtocol = 'Unknown'
            authenticationScheme = 'Unknown'
            applicationProtocol = "Unknown"
            connectionTimeOut = 0
            hostPort = 0
            NumberOfContextID = int(line[2])

            logObj.event = "Data Connection Attempt"
            logObj.msgType = 'Setup'
            logObj.time = line[1]

            if (3 < length) and (line[3] != ''):
                dataConnectionContextID = line[3]

            if dataConnectionContextID in dictionary:
                dataContextObj = dictionary[dataConnectionContextID]
            else:
                dataContextObj = DataConnectionEventInfo()
                dictionary[dataConnectionContextID] = dataContextObj
                dataContextObj = dictionary[dataConnectionContextID]

            dataContextObj.AttemptTime = line[1]   
            if NumberOfContextID > 1:
                if (4 < length) and (line[4] != '') :
                    packetConnectionContextID = line[4]
                    dataContextObj.PacketSessionContextID = packetConnectionContextID
            if NumberOfContextID > 2:
                if (5 < length) and (line[5] != '') :
                    callConnectionContextID = line[5]
                    dataContextObj.CallContextID = callConnectionContextID


            dataOfDAA = "Data Connection Context ID: "+dataConnectionContextID+";Packet Connection Context ID: "+packetConnectionContextID+";Call Connection Context ID: "
            callConnectionContextID
            if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
                logObj.applicationProtocol = line[3 + NumberOfContextID]
                applicationProtocol = ParseApplicationProtocol(int(logObj.applicationProtocol))
                dataContextObj.ApplicationProtocol = logObj.applicationProtocol
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                hostAddress = line[4 + NumberOfContextID]
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                hostPort = int(line[5 + NumberOfContextID])
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                connectionTimeOut = int(line[6 + NumberOfContextID])
            if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                securityProtocol = int(line[7 + NumberOfContextID])
                if securityProtocol == 0:
                    securityProtocol = "None"
                elif securityProtocol == 1:
                    securityProtocol = "SSL"
                elif securityProtocol == 2:
                    securityProtocol = "SSH"
            if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                authenticationScheme = int(line[8 + NumberOfContextID])
                if authenticationScheme == 0:
                    authenticationScheme = "Basic"
                elif authenticationScheme == 1:
                    authenticationScheme = "Digest"
                elif authenticationScheme == 3:
                    authenticationScheme = "None"
                elif authenticationScheme == 4:
                    authenticationScheme = "NTLM"
                elif authenticationScheme == 5:
                    authenticationScheme = "Negotiate" 

            dataOfDAA += ";Application Protocol: "+applicationProtocol+";Host Address[Port]: "+hostAddress+'['+str(hostPort)+']'

            if connectionTimeOut != 0:
                dataOfDAA += ";Connection Timeout: "+str(connectionTimeOut)
            dataOfDAA += ";Security Protocol: "+securityProtocol+';"Authentication Scheme: '+authenticationScheme

            logObj.eventInfo = dataOfDAA
            return 1
        else:
            dataOfDAA = "No of context id not found"
            return 0
    except:
        return 0


# In[ ]:




