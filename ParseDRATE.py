#!/usr/bin/env python
# coding: utf-8
from LogDTClass import LogDT
from ParseApplicationProtocol import ParseApplicationProtocol
# In[ ]:

# Data Throughput
# Parameters
# Items Sequence
# 1.  EventID = DRATE             [0]
# 2.  Time                        [1]
# 3.  Context ID Count            [2] = N
# 3a. Data Connection Context ID  [N]
# 4.  Application Protocol        [3+N]
# 5.  Application Rate Uplink     [4+N]
# 6.  Application Rate Downlink   [5+N]
# 7.  Total Bytes Uploaded        [6+N]
# 8.  Total Bytes Downloaded      [7+N]

def ParseDRATE (line, logObj):
    dataOfDRATE = ""
    length = len(line)
    if 2 < length:
        applicationProtocol = "Unknown"
        NumberOfContextID = int(line[2])

        logObj.event = "Data Tranfer Throughput"
        logObj.msgType = ' '
        logObj.time = line[1]
        applicationProtocolInt = -1
        operation = ''
        protocolError = False
        cause=''
        dataCompletionStatus = 0
        transferTime = 0        
        if (3 < length) and (line[3] != ''):
            dataTranferContextID = line[3]

        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.applicationProtocol = line[3 + NumberOfContextID]
            applicationProtocol = ParseApplicationProtocol(int(logObj.applicationProtocol))
            
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            logObj.ULRate = line[4+NumberOfContextID] #add
        if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
            logObj.DLRate = line[5+NumberOfContextID] #add
        if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
            logObj.ULBytes = line[6+NumberOfContextID]
        if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
            logObj.DLBytes = line[7+NumberOfContextID]
        
        dataOfDRATE = "Data Transfer Context ID: "+dataTranferContextID+";Application Protocol: "+applicationProtocol

        if logObj.eventInfo == '':
            logObj.eventInfo = dataOfDRATE
        else:
            logObj.eventInfo += dataOfDRATE
        
        return 1
    else:
        dataOfDRATE = "No of context id not found"
        return 0
#     except:
#         return 0

