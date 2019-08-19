#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from RadioResourceInfo import RadioResourceInfo
from MeasureSysConverter import MeasureSysConverter
from ParseRRAUMTSFDD import parseRRAUMTSFDD

# In[3]:


def ParseRRA (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        dataOfRRA = ''
        rrcContextID = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        if(3 < length) and (line[3] != '') :
            rrcContextID = int(line[3])
            RRCContextIdValue = rrcContextID
                    

        if rrcContextID in dictionary:
            RRAInfo = dictionary[rrcContextID]
        else:
            RRAInfo = RadioResourceInfo()
            dictionary[rrcContextID] = RRAInfo
            RRAInfo = dictionary[rrcContextID]
         
        
        cause = "Unknown"
        logObj.event = "Radio resource connection attempt"
        RRAInfo.ConnectionAttempt = line[1]
        dictionary[rrcContextID] = RRAInfo
        logObj.msgType = "Attempt"
        dataOfRRA = "RRC Context ID: " + str(rrcContextID)
        
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') : 
            measureSystem = MeasureSysConverter (int(line[3 + NumberOfContextID]))
            
        establishmentCause = "Unknown"
        if measureSystem == 'UMTS FDD' or measureSystem == 'UMTS TDSCDMA':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                cause = int(line[4 + NumberOfContextID])
                cause = parseRRAUMTSFDD(cause)
        elif measureSystem == 'LTE FDD' or measureSystem == 'LTE TDD':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                cause = int(line[4 + NumberOfContextID])
                if cause == 0:
                    cause = 'Emergency'
                elif cause == 1:
                    cause = 'High priority access'
                elif cause == 2:
                    cause = 'Mobile terminating access'
                elif cause == 3:
                    cause = 'Mobile originating signaling'
                elif cause == 4:
                    cause = 'Mobile originating data'
                
                
        dataOfRRA += ';RRC Establishment Cause: ' + str(cause)
        logObj.eventInfo = dataOfRRA
        logObj.modeSystem = measureSystem
                                                 
        return 1

