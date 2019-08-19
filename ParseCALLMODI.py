#!/usr/bin/env python
# coding: utf-8

# In[49]:

# Call modification indication
# Items Sequence
# 1.  EventID = CAC                   [0]
# 2.  Time                            [1]
# 3.  Call Context ID Count           [2] = N
# 3a. Call Context ID                 [N]
# 4.  Measured System                 [3+N]
# 5.  Call Type                       [4+N]

from LogDTClass import LogDT
from ParseCALLMODICallModificationType import parseCALLMODICallModificationType
from ParseCALLMODICallModificationResult import parseCALLMODICallModificationResult


# In[50]:


def ParseCALLMODI (line, logObj):
    try:
        dataOfCALLMODI = ""
        length = len(line)
        if 2 < length:
            contextID = "UnKnown"
            callModificationType = "Unknown"
            logObj.event = "Call Modification"
            logObj.msgType = "Modification"
            callModificationResult = "Unknown";
            
            NumberOfContextID = int(line[2])
            
            if (3 < length) and (line[3] != ''):
                contextID = line[3]
            if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
                callModificationType = line[3+NumberOfContextID]
                callModificationType = parseCALLMODICallModificationType(int(callModificationType))
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                callModificationResult = line[5+NumberOfContextID]
                callModificationResult = parseCALLMODICallModificationResult(int(callModificationResult))
                
            
            dataOfCALLMODI = "Context ID: "+contextID+";Call Modification Type:"+callModificationType+";Call Modification Result: "+callModificationResult
            
            logObj.eventInfo = dataOfCALLMODI
            return 1
        else:
            dataOfCALLMODI = "No of context id not found"
            return 0
    except:
        return 0


# In[ ]:




