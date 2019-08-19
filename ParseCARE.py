#!/usr/bin/env python
# coding: utf-8

# In[49]:
# Call re-establishment
# Parameters |Parameters for GSM, UMTS FDD, and UMTS TD-SCDMA
# Items Sequence
# 1.  EventID = CAC                   [0]
# 2.  Time                            [1]
# 3.  Call Context ID Count           [2] = N
# 3a. Call Context IDs                [N]
# 4.  Measrue Sytem                   [3+N]
# CASE GSM, UMTS FDD, and UMTS TD-SCDMA
# 5.  Re-establishment status         [4+N]
# 6.  Re-establishment duration       [5+N]

from MeasureSysConverter import MeasureSysConverter
from LogDTClass import LogDT


# In[50]:


def ParseCARE (line, logObj):
    try:
        dataOfCARE = ""
        length = len(line)
        if 2 < length:
            contextID = "UnKnown"
            logObj.event = "Call Re-establishment"
            logObj.msgType = "Information Update"
            measureSystem = "Unknown"
            NumberOfContextID = int(line[2])
            re_establishStatus = 'Unknown'
            re_establishDuration = "Unknown"
            
            if (3 < length) and (line[3] != ''):
                contextID = line[3]
            if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
                measureSystem = line[3+NumberOfContextID]
                measureSystem = MeasureSysConverter(int(measureSystem))
                if measureSystem != "Unknown":
                    if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                        re_establishStatus = line[4+NumberOfContextID]
                    if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                        re_establishDuration = line[4+NumberOfContextID]
                
            
            dataOfCARE = "Context ID: "+contextID+";Measure System: "+measureSystem+";Re-Establishment Status: "+re_establishStatus+";Re-Establishment Duration: "+re_establishDuration

            if logObj.eventInfo == '':
                logObj.eventInfo = dataOfCARE
            else:
                logObj.eventInfo += dataOfCARE
            return 1
        else:
            dataOfCARE = "No of context id not found"
            return 0
    except:
        return 0


# In[ ]:




