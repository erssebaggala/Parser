#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from AttachmentEventInfo import AttachmentEventInfo
from MeasureSysConverter import MeasureSysConverter
from datetime import datetime

# In[1]:


def ParseGAC (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        contextID = 0
        dataOfGAC = ''
        if line[2] != '':
            
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') and NumberOfContextID == 1 :
                    contextID = int(line[3])
                    
        if contextID in dictionary:
            attachment = dictionary[contextID]
        else:
            attachment = AttachmentEventInfo()
            dictionary[contextID] = attachment
            attachment = dictionary[contextID]
         
        setupTime = 0
        attachment.Established = line[1]
        if attachment.Setup != '' and attachment.Established != '':
            tdelta = datetime.strptime(attachment.Setup.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(attachment.Established.split('.', 1)[0], '%H:%M:%S')        
            setupTime = float(tdelta.seconds)*1000 #MilliSeconds 
        
        logObj.event = "Attach Conneted"
        logObj.msgType = "Connect"
        dataOfGAC += "Attach Context ID: " + str(contextID)
        measureSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        dataOfGAC += ";Measured System: " + measureSystem
        
        if setupTime > 0:
            dataOfGAC += ";Setup time: "+setupTime+"ms"
        logObj.eventInfo = dataOfGAC
        logObj.modeSystem = measureSystem
        return 1

