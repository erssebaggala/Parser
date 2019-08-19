#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from RadioResourceInfo import RadioResourceInfo
from MeasureSysConverter import MeasureSysConverter
from datetime import datetime

# In[3]:


def ParseRRD (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        dataOfRRD = ''
        RRDContextID = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') :
                    RRDContextID = int(line[3])
                    RRDContextIdValue = RRDContextID
                    
        if RRDContextID in dictionary:
            RRDInfo = dictionary[RRDContextID]
        else:
            RRDInfo = RadioResourceInfo()
            dictionary[RRDContextID] = RRDInfo
            RRDInfo = dictionary[RRDContextID]
         
        
        logObj.event = "Radio Resource Connection Closed"
        RRDInfo.ConnectionEnd = line[1]
        dictionary[RRDContextID] = RRDInfo
        logObj.msgType = "Complete"
        dataOfRRD = "RRD Context ID: " + str(RRDContextID)
        
        if RRDInfo.ConnectionSetup != '' and RRDInfo.ConnectionEnd !='':
            tdelta = datetime.strptime(RRDInfo.ConnectionEnd.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(RRDInfo.ConnectionSetup.split('.', 1)[0], '%H:%M:%S')        
            failureTime = float(tdelta.seconds)*1000 #MilliSeconds 
            dataOfRRD += ";RRC Duration: "+str(failureTime)  
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') : 
            measureSystem = MeasureSysConverter (int(line[3 + NumberOfContextID]))         
        cause = "Unknown"
        if measureSystem == 'UMTS FDD' or measureSystem == 'UMTS TDSCDMA':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                cause = line[4 + NumberOfContextID]
                if cause == '1':
                    dataOfRRD += ";Release Status: Normal Relase; "
                elif cause == '2':
                    dataOfRRD += ";Release Status: Dropped RRC Connection; "
                    logObj.eventInfo = 'Radio Resource Connection Dropped'
            if((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') : 
                cause = line[5 + NumberOfContextID]
                if cause == '0':
                    dataOfRRD += "Release Cause: Normal event; "
                elif cause == '1':
                    dataOfRRD += "Release Cause: Unspecified; "
                elif cause == '2':
                    dataOfRRD += "Release Cause: Pre-emptive release; "
                elif cause == '3':
                    dataOfRRD += "Release Cause: Congestion; "
                elif cause == '4':
                    dataOfRRD += "Release Cause: Re-establishment reject; "
                elif cause == '5':
                    dataOfRRD += "Release Cause: Directed signaling connection re-establishment; "
                elif cause == '6':
                    dataOfRRD += "Release Cause: User inactivity; "
                elif cause == '1000':
                    dataOfRRD += "Release Cause: T313 expired; "
                    
        elif measureSystem == 'LTE FDD' or measureSystem == 'LTE TDD':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                cause = line[4 + NumberOfContextID]
                if cause == '1':
                    dataOfRRD += "Release Status: Normal Relase; "
                elif cause == '2':
                    dataOfRRD += "Release Status: Dropped RRC Connection; "
                    logObj.eventInfo = 'Radio Resource Connection Dropped'
            if((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') : 
                cause = line[5 + NumberOfContextID]
                if cause == '0':
                    dataOfRRD += "Release Cause: Load balancing TAU required; "
                elif cause == '1':
                    dataOfRRD += "Release Cause: Other; "
        logObj.eventInfo = dataOfRRD
        logObj.modeSystem = measureSystem
                                                 
        return 1

