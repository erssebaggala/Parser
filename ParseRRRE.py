#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from RadioResourceInfo import RadioResourceInfo
from MeasureSysConverter import MeasureSysConverter


# In[3]:


def ParseRRRE (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        dataOfRRRE = ''
        RRREContextID = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') :
                    RRREContextID = int(line[3])
                    RRREContextIdValue = RRREContextID
                    
        if RRREContextID in dictionary:
            RRREInfo = dictionary[RRREContextID]
        else:
            RRREInfo = RadioResourceInfo()
            dictionary[RRREContextID] = RRREInfo
            RRREInfo = dictionary[RRREContextID]
         
        
        logObj.event = "Radio Resource Connection Re-Establishment"
        RRREInfo.ConnectionEnd = line[1]
        dictionary[RRREContextID] = RRREInfo
        logObj.msgType = "Re-Establishment"
        dataOfRRRE = "RRRE Context ID: " + str(RRREContextID)
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') : 
            measureSystem = MeasureSysConverter (int(line[3 + NumberOfContextID]))        
        cause = "Unknown"
        if measureSystem == 'LTE FDD' or measureSystem == 'LTE TDD':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                cause = line[4 + NumberOfContextID]
                if cause == '1':
                    dataOfRRRE += ";Re-Establishment Status: Succeeded; "
                elif cause == '2':
                    dataOfRRRE += ";Re-Establishment Status: Failed; "
                elif cause == '3':
                    dataOfRRRE += ";Re-Establishment Status: Rejected; "
            if((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') : 
                cause = line[5 + NumberOfContextID]
                if cause == '0':
                    dataOfRRRE += ";Re-Establishment Cause: Reconfiguration failure"
                elif cause == '1':
                    dataOfRRRE += ";Re-Establishment Cause: Handover failure; "
                elif cause == '2':
                    dataOfRRRE += ";Re-Establishment Cause: Other Failure; "
                
        logObj.eventInfo = dataOfRRRE
        logObj.modeSystem = measureSystem
                                                 
        return 1

