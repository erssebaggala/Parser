#!/usr/bin/env python
# coding: utf-8

# In[2]:

# Packet Error Rate
# Parameters
# Items Sequence
# 1.  EventID = DRATE             [0]
# 2.  Time                        [1]
# 3.  Context ID Count            [2] = N
# 3a. Data Connection Context ID  [N]
# 4.  Application Protocol        [3+N]
# 5.  PER Uplink                  [4+N]
# 6.  PER Downlink                [5+N]
# 7.  Packets Uploaded            [6+N]
# 8.  Packets Downloaded          [7+N]
# 9.  Errors Uploaded             [8+N]
# 10. Errors Downloaded           [9+N]

from LogDTClass import LogDT


# In[26]:



def ParsePER (line, logObj):
    dataOfPER = ""
    length = len(line)
    if 2 < length:
        applicationProtocol = "Unknown"
        NumberOfContextID = int(line[2])

        logObj.event = "Packet Error Rate"
        logObj.msgType = ' '
        logObj.time = line[1]
        applicationProtocolInt = -1
        if (3 < length) and (line[3] != ''):
            dataTranferContextID = line[3]
            
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            logObj.ULPER = line[4+NumberOfContextID] #add
        if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
            logObj.DLPER = line[5+NumberOfContextID] #add
        if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
            logObj.ULPackets = line[6+NumberOfContextID]
        if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
            logObj.DLPackets = line[7+NumberOfContextID]
        if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
            logObj.ULErrors = line[8+NumberOfContextID]
        if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
            logObj.DLErrors = line[9+NumberOfContextID]
        
        dataOfPER = "Data Transfer Context ID: "+dataTranferContextID

        if logObj.eventInfo == '':
            logObj.eventInfo = dataOfPER
        else:
            dataOfPER = ";" + dataOfPER
            logObj.eventInfo += dataOfPER
        
        return 1
    else:
        dataOfPER = "No of context id not found"
        return 0
#     except:
#         return 0


# In[ ]:




