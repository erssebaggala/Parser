#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from datetime import datetime

# In[3]:


def ParsePBF (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        dataOfPBF = ''
        PBFContextID = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') :
                    PBFContextID = int(line[3])
                    
        if PBFContextID in dictionary:
            packet = dictionary[PBFContextID]
        else:
            packet = PacketBearerInfo()
            dictionary[PBFContextID] = packet
            packet = dictionary[PBFContextID]
            
        packet.ConnectionFailure = line[1]
        logObj.event = 'Packet Bearer Allocation Failure'
        logObj.msgType = 'Failure'       
        dataOfPBF = "PB Context ID: " + str(PBFContextID)
        
        if packet.ConnectionFailure != '' and packet.ConnectionAttempt !='':
            tdelta = datetime.strptime(packet.ConnectionFailure.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(packet.ConnectionAttempt.split('.', 1)[0], '%H:%M:%S')        
            Time = float(tdelta.seconds)*1000 #MilliSeconds 
            dataOfPBF += ";PB Connection Failure duration: "+str(Time)
         
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') : 
            measureSystem = MeasureSysConverter (int(line[3 + NumberOfContextID]))           
        esmCause = 'Unknown'
        if measureSystem == 'LTE FDD' or measureSystem == 'LTE TDD':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                esmCause = line[4 + NumberOfContextID]
                esmCause = parseEsmCause(int(esmCause))
        dataOfPBF += ";ESM Cause: " + esmCause
        logObj.modeSystem = measureSystem
        logObj.eventInfo = dataOfPBF             
        return 1

