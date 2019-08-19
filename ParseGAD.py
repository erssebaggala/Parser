#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from AttachmentEventInfo import AttachmentEventInfo
from MeasureSysConverter import MeasureSysConverter
from datetime import datetime
from parseGADDisconnectionCause import parseGADDisconnectionCause

# In[1]:


def ParseGAD (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        contextID = 0
        dataOfGAD = ''
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
         
        attachmentDuration = 0
        attachment.End = line[1]
        if attachment.End != '' and attachment.Established != '':
            tdelta = datetime.strptime(attachment.End.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(attachment.Established.split('.', 1)[0], '%H:%M:%S')        
            attachmentDuration = float(tdelta.seconds)*1000 #MilliSeconds 
        
        logObj.event = "Detach"
        logObj.msgType = "Release"
        dataOfGAD += "Detach Context ID: " + str(contextID)
        measureSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        dataOfGAD += ";Measured System: " + measureSystem
        
        detachStatus = 'Unknown'
        if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') :
            detachCheck = int(line[4 + NumberOfContextID])
            if detachCheck == 1:
                detachStatus = 'User detach'
            elif detachCheck == 2:
                detachStatus = 'Network detach (GMM Cause)'
            elif detachCheck == 3:
                detachStatus = 'Mobile detach (GMM Cause)'
            elif detachCheck == 4:
                detachStatus = 'Test system failure'
                
        if attachmentDuration > 0:
            dataOfGAD += ";Attachemt Duration: " + str(attachmentDuration) + 'ms'
        dataOfGAD += ";Detach status: "+detachStatus
        
        disconnectionCause = "Unknown"
        if((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') :
            disconnectionCause = parseGADDisconnectionCause(int(line[5 + NumberOfContextID]))
            
 
        dataOfGAD += ";Disconnection Cause: " + disconnectionCause
        if((6 + NumberOfContextID) < length) and (line[6 + NumberOfContextID] != '') :
            dataOfGAD += ";Detach Time: "+line[6 + NumberOfContextID]
            
        logObj.eventInfo = dataOfGAD
        logObj.modeSystem = measureSystem
        return 1

