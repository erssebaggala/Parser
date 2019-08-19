#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from RadioResourceInfo import RadioResourceInfo
from MeasureSysConverter import MeasureSysConverter
from datetime import datetime


# In[3]:


def ParseRRC (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        dataOfRRC = ''
        rrcContextID = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') :
                    rrcContextID = int(line[3])
                    RRCContextIdValue = rrcContextID
                    

        if rrcContextID in dictionary:
            RRCInfo = dictionary[rrcContextID]
        else:
            RRCInfo = RadioResourceInfo()
            dictionary[rrcContextID] = RRCInfo
            RRCInfo = dictionary[rrcContextID]
         
        
        logObj.event = "Radio Resource Connection Success"
        RRCInfo.ConnectionSetup = line[1]
        dictionary[rrcContextID] = RRCInfo
        logObj.msgType = "Success"
        dataOfRRC = "RRC Context ID: " + str(rrcContextID)
        
        if RRCInfo.ConnectionSetup != '' and RRCInfo.ConnectionAttempt !='':
            tdelta = datetime.strptime(RRCInfo.ConnectionSetup.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(RRCInfo.ConnectionAttempt.split('.', 1)[0], '%H:%M:%S')        
            setupTime = float(tdelta.seconds)*1000 #MilliSeconds 
            dataOfRRC += ";Setup Time: "+str(setupTime)  
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') : 
            measureSystem = MeasureSysConverter (int(line[3 + NumberOfContextID]))           
        cause = "Unknown"
        if measureSystem == 'UMTS FDD' or measureSystem == 'UMTS TDSCDMA':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                cause = line[4 + NumberOfContextID]
                
                
        dataOfRRC += ';RRC Requests before connection: ' + cause
        logObj.eventInfo = dataOfRRC
        logObj.modeSystem = measureSystem
                                                 
        return 1

