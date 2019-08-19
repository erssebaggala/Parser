#!/usr/bin/env python
# coding: utf-8

# In[49]:

# Data Connection Disconnect
# Parameters
# Items Sequence
# 1.  EventID = DAD               [0]
# 2.  Time                        [1]
# 3.  Context ID Count            [2] = N
# 3a. Data Connection Context ID  [N]
# 4.  Application Protocol        [3+N]
# 5.  Data Disconnect Status      [4+N]
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
from ParseDADDataDisconnectStatus import parseDADDataDisconnectStatus


# In[50]:


def ParseDAD (line, logObj, dictionary):
    dataOfDAD = ""
    length = len(line)
    if 2 < length:
        dataConnectionContextID = "UnKnown"
        cause = "Unknown"
        applicationProtocol = "Unknown"
        totalConnectionTime = 0
        NumberOfContextID = int(line[2])
        dataDisconnectStatus = "Unknown"

        logObj.event = "Data Connection Disconnected"
        logObj.msgType = 'Disconnect'
        logObj.time = line[1]
        if (3 < length) and (line[3] != ''):
            dataConnectionContextID = line[3]

        if dataConnectionContextID in dictionary:
            dataContextObj = dictionary[dataConnectionContextID]
        else:
            dataContextObj = DataConnectionEventInfo()
            dictionary[dataConnectionContextID] = dataContextObj
            dataContextObj = dictionary[dataConnectionContextID]

        dataContextObj.DisconnectTime = line[1]
        tdelta = datetime.strptime(dataContextObj.DisconnectTime.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(dataContextObj.AttemptTime.split('.', 1)[0], '%H:%M:%S')        
        totalConnectionTime = float(tdelta.seconds)*1000 #MilliSeconds 

        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.applicationProtocol = line[3 + NumberOfContextID]
            applicationProtocol = ParseApplicationProtocol(int(logObj.applicationProtocol))
            dataContextObj.ApplicationProtocol = applicationProtocol
            
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            dataDisconnectStatus = line[4 + NumberOfContextID]
            dataDisconnectStatus = parseDADDataDisconnectStatus(int(dataDisconnectStatus))
            
        dataOfDAD = "Data Connection Context ID: "+dataConnectionContextID+";Application Protocol: "+applicationProtocol+"; Disconnect Status: "+dataDisconnectStatus


        if totalConnectionTime > 0:
            dataOfDAD += ";Total Connection Time: "+str(totalConnectionTime)
            
        if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
            cause = line[5 + NumberOfContextID]
            if cause == 'FTP' or cause == 'SFTP':
                cause = parseDAFFtpSftpFailStatus(int(cause))
            elif cause == 'HTTP':
                cause = parseDAFHttpFailStatus(int(cause))
            elif cause == 'MMS' or cause == 'WAP 1.0' or cause == 'WAP 2.0':
                cause = parseDAFMmsWapFailStatus(int(cause))
                
        dataOfDAD += ";Cause: "+cause
        logObj.eventInfo = dataOfDAD
        return 1
    else:
        dataOfDAD = "No of context id not found"
        return 0
#     except:
#         return 0


# In[ ]:




