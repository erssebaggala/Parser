#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter

# In[1]:


def ParseRLCBLER (line, logObj):
    length = len(line)
    if 2 < length:
        contextID = 0
        NumberOfContextID = 0
        if line[2] != '':   
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != ''):
                    contextID = int(line[3])
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') :
            logObj.BLER = float(line[4 + NumberOfContextID])
        return 1

