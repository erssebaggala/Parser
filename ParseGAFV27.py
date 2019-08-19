#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from AttachmentEventInfo import AttachmentEventInfo
from MeasureSysConverter import MeasureSysConverter
from parseGADDisconnectionCause import parseGADDisconnectionCause


# In[1]:


def ParseGAFV27 (line, logObj,dictionary):
    length = len(line)
    if 2 < length:
        contextID = 0
        dataOfGAF = ''
        NumberOfContextID = 0
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
            
        attachment.Failure = line[1]
        logObj.event = "Attach Failed"
        logObj.MessageType = "Failure"
        dataOfGAF += "Attach Context ID: " + str(contextID)
        measureSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        
        failState = 'Unknown'
        if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') :
            failCheck = int(line[4 + NumberOfContextID])
            if failCheck == 1:
                failState = 'User abort'
            elif failCheck == 2:
                failState = 'Network reject'
            elif failCheck == 3:
                failState = 'Mobile reject'
            elif failCheck == 4:
                failState = 'Timeout'
            elif failCheck == 5:
                failState = 'PPP error'
            elif failCheck == 6:
                failState = 'Test system failure'
        
        dataOfGAF += ";Failure status: "+failState
        disconnectionCause = "Unknown"
        if((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') :
            disconnectionCause = parseGADDisconnectionCause(int(line[5 + NumberOfContextID]))
            
 
        dataOfGAF += ";Disconnection Cause: " + disconnectionCause
        logObj.eventInfo = dataOfGAF
        logObj.modeSystem = measureSystem
        return 1

