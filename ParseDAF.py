#!/usr/bin/env python
# coding: utf-8

# In[49]:

# Data Connection Failed
# Parameters
# Items Sequence
# 1.  EventID = DAF               [0]
# 2.  Time                        [1]
# 3.  Context ID Count            [2] = N
# 3a. Data Connection Context ID  [N]
# 4.  Application Protocol        [3+N]
# 5.  Data Fail Status            [4+N]
# Parameters for FTP and SFTP protocol errors
# 6.  FTP cause                   [5+N]
# Parameters for HTTP protocol errors
# 6.  HTTP cause                  [5+N]
# Parameters for WAP and MMS protocol errors
# 6.  WAP and MMS cause           [5+N]
# Others
# 6.  Multiple Cases - Ignored    [5+N]

#This will have a dictionary of all the DATA Connection Context IDs
#atm, dictionary is accumulating all the data from data connections
#present

from LogDTClass import LogDT
from DataConnectionEventInfo import DataConnectionEventInfo
from ParseApplicationProtocol import ParseApplicationProtocol
from datetime import datetime, date
from ParseDAFDataFailStatus import parseDAFDataFailStatus
from ParseDAFFtpSftpFailStatus import parseDAFFtpSftpFailStatus
from ParseDAFHttpFailStatus import parseDAFHttpFailStatus
from parseDAFMmsWapFailStatus import parseDAFMmsWapFailStatus


# In[50]:


def ParseDAF (line, logObj, dictionary):
    dataOfDAF = ""
    length = len(line)
    if 2 < length:
        dataConnectionContextID = "UnKnown"
        cause = "Unknown"
        applicationProtocol = "Unknown"
        failureTime = 0
        NumberOfContextID = int(line[2])
        dataFailStatus = "Unknown"

        logObj.event = "Data Connection Failed"
        logObj.msgType = 'Failure'
        logObj.time = line[1]
        if (3 < length) and (line[3] != ''):
            dataConnectionContextID = line[3]

        if dataConnectionContextID in dictionary:
            dataContextObj = dictionary[dataConnectionContextID]
        else:
            dataContextObj = DataConnectionEventInfo()
            dictionary[dataConnectionContextID] = dataContextObj
            dataContextObj = dictionary[dataConnectionContextID]

        dataContextObj.FailureTime = line[1]
        tdelta = datetime.strptime(dataContextObj.FailureTime.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(dataContextObj.AttemptTime.split('.', 1)[0], '%H:%M:%S')        
        failureTime = float(tdelta.seconds)*1000 #MilliSeconds 

        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.applicationProtocol = line[3 + NumberOfContextID]
            applicationProtocol = ParseApplicationProtocol(int(logObj.applicationProtocol))
            dataContextObj.ApplicationProtocol = applicationProtocol
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            dataFailStatus = line[4 + NumberOfContextID]
            dataFailStatus = parseDAFDataFailStatus(int(dataFailStatus))
            
        dataOfDAF = "Data Connection Context ID: "+dataConnectionContextID+";Application Protocol: "+applicationProtocol+"; Fail Status: "+dataFailStatus


        if failureTime > 0:
            dataOfDAF += ";Failure Time: "+str(failureTime)
            
        if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
            cause = line[5 + NumberOfContextID]
            if applicationProtocol == 'FTP' or applicationProtocol == 'SFTP':
                cause = parseDAFFtpSftpFailStatus(int(cause))
            elif applicationProtocol == 'HTTP':
                cause = parseDAFHttpFailStatus(int(cause))
            elif applicationProtocol == 'MMS' or applicationProtocol == 'WAP 1.0' or applicationProtocol == 'WAP 2.0':
                cause = parseDAFMmsWapFailStatus(int(cause))
                
        dataOfDAF += ";Cause: "+cause
        logObj.eventInfo = dataOfDAF
        return 1
    else:
        dataOfDAF = "No of context id not found"
        return 0
#     except:
#         return 0


# In[ ]:




