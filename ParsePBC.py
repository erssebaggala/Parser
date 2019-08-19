#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from datetime import datetime

# In[3]:


def ParsePBC (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        dataOfPBC = ''
        PBCContextID = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') :
                    PBCContextID = int(line[3])
                    
        if PBCContextID in dictionary:
            packet = dictionary[PBCContextID]
        else:
            packet = PacketBearerInfo()
            dictionary[PBCContextID] = packet
            packet = dictionary[PBCContextID]
            
        packet.ConnectionEstablished = line[1]
        logObj.event = 'Packet Bearer Allocation Attempt'
        logObj.msgType = 'Attempt'       
        dataOfPBC = "PB Context ID: " + str(PBCContextID)
        
        if packet.ConnectionEstablished != '' and packet.ConnectionAttempt !='':
            tdelta = datetime.strptime(packet.ConnectionEstablished.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(packet.ConnectionAttempt.split('.', 1)[0], '%H:%M:%S')        
            Time = float(tdelta.seconds)*1000 #MilliSeconds 
            dataOfPBC += ";PB Connection Setup duration: "+str(Time)
         
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') : 
            measureSystem = MeasureSysConverter (int(line[3 + NumberOfContextID]))           
        pbType = 'Unknown'
        if measureSystem == 'LTE FDD' or measureSystem == 'LTE TDD':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                dataOfPBC += ";PB ID: "+line[4 + NumberOfContextID]
            if((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') : 
                dataOfPBC += ";Linked PB ID: "+line[5 + NumberOfContextID]
        logObj.modeSystem = measureSystem
        logObj.eventInfo = dataOfPBC             
        return 1

