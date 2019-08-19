#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from AttachmentEventInfo import AttachmentEventInfo

# In[1]:


def ParseGAA (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        contextID = 0
        dataOfGAA = ''
        NumberOfContextID = 0
        if line[2] != '':
            
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') :
                    contextID = int(line[3])
                    
        if contextID in dictionary:
            attachment = dictionary[contextID]
        else:
            attachment = AttachmentEventInfo()
            dictionary[contextID] = attachment
            attachment = dictionary[contextID]
            
        attachment.Attempt = line[1]        
        logObj.event = "Attach Attempt"
        logObj.msgType = "Setup"
        dataOfGAA += "Attach Context ID: " + str(contextID)
        measureSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        logObj.eventInfo = dataOfGAA
        logObj.modeSystem = measureSystem
        return 1

