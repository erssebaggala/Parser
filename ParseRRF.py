#!/usr/bin/env python
# coding: utf-8

# In[1]:

from datetime import datetime
from LogDTClass import LogDT
from RadioResourceInfo import RadioResourceInfo
from MeasureSysConverter import MeasureSysConverter


# In[3]:


def ParseRRF (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        dataOfRRF = ''
        RRFContextID = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') :
                    RRFContextID = int(line[3])
                    RRFContextIdValue = RRFContextID
                    

        if RRFContextID in dictionary:
            RRFInfo = dictionary[RRFContextID]
        else:
            RRFInfo = RadioResourceInfo()
            dictionary[RRFContextID] = RRFInfo
            RRFInfo = dictionary[RRFContextID]
         
        
        logObj.event = "Radio Resource Connection Failure"
        RRFInfo.ConnectionFailure = line[1]
        dictionary[RRFContextID] = RRFInfo
        logObj.msgType = "Failure"
        dataOfRRF = "RRF Context ID: " + str(RRFContextID)
        
        if RRFInfo.ConnectionFailure != '' and RRFInfo.ConnectionAttempt !='':
            tdelta = datetime.strptime(RRFInfo.ConnectionFailure.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(RRFInfo.ConnectionAttempt.split('.', 1)[0], '%H:%M:%S')        
            setupTime = float(tdelta.seconds)*1000 #MilliSeconds 
            dataOfRRF += ";Failure Time: "+str(setupTime)  
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') : 
            measureSystem = MeasureSysConverter (line[3 + NumberOfContextID])           
        cause = "Unknown"
        if measureSystem == 'UMTS FDD' or measureSystem == 'UMTS TDSCDMA':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                dataOfRRF += "RRC Requests before connection: "+line[4 + NumberOfContextID]
            if((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') : 
                cause = line[5 + NumberOfContextID]
                if cause == '1':
                    dataOfRRF += "Rejection Status: Network Reject"
            if((6 + NumberOfContextID) < length) and (line[6 + NumberOfContextID] != '') : 
                cause = line[6 + NumberOfContextID]
                if cause == '1':
                    dataOfRRF += "Rejection Cause: Congestion"
                elif cause == '2':
                    dataOfRRF += "Rejection Cause: Unspecified"
                    
        elif measureSystem == 'LTE FDD' or measureSystem == 'LTE TDD':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                cause = line[4 + NumberOfContextID]
                if cause == '1':
                    dataOfRRF += "Rejection Status: Network Reject"
                
        dataOfRRF += ';RRF Requests before connection: ' + cause
        logObj.eventInfo = dataOfRRF
        logObj.modeSystem = measureSystem
                                                 
        return 1

