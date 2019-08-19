#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from PacketBearerInfo import PacketBearerInfo

# In[3]:


def ParsePBA (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        dataOfPBA = ''
        PBAContextID = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') :
                    PBAContextID = int(line[3])
                    
        if PBAContextID in dictionary:
            packet = dictionary[PBAContextID]
        else:
            packet = PacketBearerInfo()
            dictionary[PBAContextID] = packet
            packet = dictionary[PBAContextID]
            
        packet.ConnectionAttempt = line[1]
        logObj.event = 'Packet Bearer Allocation Attempt'
        logObj.msgType = 'Attempt'       
        dataOfPBA = "PB Context ID: " + str(PBAContextID)
        
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') : 
            measureSystem = MeasureSysConverter (int(line[3 + NumberOfContextID]))           
        pbType = 'Unknown'
        if measureSystem == 'LTE FDD' or measureSystem == 'LTE TDD':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                pbType = int(line[4 + NumberOfContextID])
                
                if pbType == 1:
                    pbType = "Default"
                elif pbType == 2:
                    pbType = "Dedicated"
        dataOfPBA += ";PB Type: "+pbType
        logObj.modeSystem = measureSystem
        logObj.eventInfo = dataOfPBA             
        return 1

