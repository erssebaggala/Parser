#!/usr/bin/env python
# coding: utf-8

# In[49]:

# Data Connection Success
# Parameters
# Items Sequence
# 1.  EventID = DAC               [0]
# 2.  Time                        [1]
# 3.  Context ID Count            [2] = N
# 3a. Data Connection Context ID  [N]
# 4.  Application Protocol        [3+N]

#This will have a dictionary of all the DATA Connection Context IDs
#atm, dictionary is accumulating all the data from data connections
#present

from LogDTClass import LogDT
from DataConnectionEventInfo import DataConnectionEventInfo
from ParseApplicationProtocol import ParseApplicationProtocol
from datetime import datetime, date


# In[50]:


def ParseDAC (line, logObj, dictionary):
    dataOfDAC = ""
    length = len(line)
    if 2 < length:
        dataConnectionContextID = "UnKnown"
        applicationProtocol = "Unknown"
        connectionTime = 0
        NumberOfContextID = int(line[2])

        logObj.event = "Data Connection Success"
        logObj.msgType = 'Connected'
        logObj.time = line[1]
        if (3 < length) and (line[3] != ''):
            dataConnectionContextID = line[3]

        if dataConnectionContextID in dictionary:
            dataContextObj = dictionary[dataConnectionContextID]
        else:
            dataContextObj = DataConnectionEventInfo()
            dictionary[dataConnectionContextID] = dataContextObj
            dataContextObj = dictionary[dataConnectionContextID]

        dataContextObj.SuccessTime = line[1]
        tdelta = datetime.strptime(dataContextObj.SuccessTime.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(dataContextObj.AttemptTime.split('.', 1)[0], '%H:%M:%S')        
        connectionTime = float(tdelta.seconds)*1000 #MilliSeconds 

        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.applicationProtocol = line[3 + NumberOfContextID]
            applicationProtocol = ParseApplicationProtocol(int(logObj.applicationProtocol))
            dataContextObj.ApplicationProtocol = logObj.applicationProtocol

        dataOfDAC = "Data Connection Context ID: "+dataConnectionContextID+";Application Protocol: "+applicationProtocol


        if connectionTime > 0:
            dataOfDAC += ";Connection Time: "+str(connectionTime)

        logObj.eventInfo = dataOfDAC
        return 1
    else:
        dataOfDAC = "No of context id not found"
        return 0
#     except:
#         return 0


# In[ ]:




