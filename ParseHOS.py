#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from HOEventInfo import HOEventInfo
from datetime import datetime


# In[3]:


def ParseHOS (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        dataOfHOS = ''
        handoverContextID = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') :
                    handoverContextID = int(line[3])
                    
        logObj.event = "Handover"
        logObj.msgType = 'Handover Complete'
        dataOfHOS = "Handover Context ID: " + str(handoverContextID)
        measureSystems=''
        handoverType = "Unknown"
        
        if handoverContextID in dictionary:
            HOSInfo = dictionary[handoverContextID]
        else:
            HOSInfo = HOEventInfo()
            dictionary[handoverContextID] = HOSInfo
            HOSInfo = dictionary[handoverContextID]
            
        HOSInfo.HOSuccess = line[1]
        logObj.modeSystem = HOSInfo.ModeSystem
        dictionary[handoverContextID] = HOSInfo
        successTime = "Unknown"
        if HOSInfo.HOSuccess != '' and HOSInfo.HOAttempt != '':
            tdelta = datetime.strptime(HOSInfo.HOSuccess.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(HOSInfo.HOAttempt.split('.', 1)[0], '%H:%M:%S')        
            successTime = float(tdelta.seconds)*1000 #MilliSeconds 

            
        dataOfHOS += ';"Handover Success Time: '+str(successTime) + ';Handover Type: '+HOSInfo.HOType
                                                 
        logObj.eventInfo = dataOfHOS
                                                 
        return 1

