#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter

# In[1]:


def ParseLLCRATE (line, logObj):
    length = len(line)
    if 2 < length:
        contextID = 0
        if line[2] != '':
            
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != ''):
                    contextID = int(line[3])
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(line[3 + NumberOfContextID])
        
        if logObj.modeSystem == 'GSM':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') :
                logObj.LLCRateUL = int(line[4 + NumberOfContextID])
            if((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') :
                logObj.LLCRateDL = int(line[5 + NumberOfContextID])
            
            
        return 1

