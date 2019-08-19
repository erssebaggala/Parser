#!/usr/bin/env python
# coding: utf-8

# In[2]:

# Data Transfer Complete
# Parameters
# Items Sequence
# 1.  EventID = DCOMP             [0]
# 2.  Time                        [1]
# 3.  Context ID Count            [2] = N
# 3a. Data Connection Context ID  [N]
# 4.  Application Protocol        [3+N]
# 5.  Transfer Status             [4+N]
# 6.  Multiple Cases - Ignored    [5+N]
# 7.  IP access time              [6+N]
# 8.  IP termination time         [7+N]
# 9.  Bytes UL                    [8+N]
# 10. Bytes DL                    [9+N]
# 11. Header transfer time        [10+N]
# 12. TCP connection time         [11+N]
# 13. Redirect address            [12+N]

#This will have a dictionary of all the DATA Connection Context IDs
#atm, dictionary is accumulating all the data from data connections
#present

from LogDTClass import LogDT
from DataConnectionEventInfo import DataConnectionEventInfo
from ParseApplicationProtocol import ParseApplicationProtocol
from ParseDAFDataFailStatus import parseDAFDataFailStatus
from ParseDAFFtpSftpFailStatus import parseDAFFtpSftpFailStatus
from ParseDAFHttpFailStatus import parseDAFHttpFailStatus
from parseDAFMmsWapFailStatus import parseDAFMmsWapFailStatus
from datetime import datetime


# In[21]:


def ParseDCOMP (line, logObj, dictionary):
    dataOfDCOMP = ""
    length = len(line)
    if 2 < length:
        applicationProtocol = "Unknown"
        NumberOfContextID = int(line[2])

        logObj.event = "Data Tranfer Complete"
        logObj.msgType = 'Disconnect'
        logObj.time = line[1]
        applicationProtocolInt = -1
        operation = ''
        protocolError = False
        cause=''
        dataCompletionStatus = 0
        transferTime = 0        
        if (3 < length) and (line[3] != ''):
            dataTranferContextID = line[3]

        if dataTranferContextID in dictionary:
            dataContextObj = dictionary[dataTranferContextID]
        else:
            dataContextObj = DataConnectionEventInfo()
            dictionary[dataTranferContextID] = dataContextObj
            dataContextObj = dictionary[dataTranferContextID]

        dataContextObj.DataConnectionContextID = dataTranferContextID
        dataContextObj.DataTransferCompleteTime = line[1]
        
        transferTime = 0
        if dataContextObj.DataTransferCompleteTime != '' and dataContextObj.DataTransferRequestTime != '':
            tdelta = datetime.strptime(dataContextObj.DataTransferCompleteTime.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(dataContextObj.DataTransferRequestTime.split('.', 1)[0], '%H:%M:%S')        
            transferTime = float(tdelta.seconds)*1000 #MilliSeconds 

        
        
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.applicationProtocol = line[3 + NumberOfContextID]
            applicationProtocol = ParseApplicationProtocol(int(logObj.applicationProtocol))
            dataContextObj.ApplicationProtocol = applicationProtocol
            
            applicationProtocolInt = int (line[3 + NumberOfContextID])
            
        logObj.direction = 'NA'
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            
            dataCompletionStatus = int (line[4 + NumberOfContextID])
            if dataCompletionStatus == 1:
                dataCompletionStatus = 'Successful'
            elif dataCompletionStatus == 2:
                dataCompletionStatus = 'Socket Error'
            elif dataCompletionStatus == 3:
                dataCompletionStatus = 'Protocol error or timeout'
                protocolError = True
            elif dataCompletionStatus == 5:
                dataCompletionStatus = "User Abort"
                
        dataOfDCOMP = "Data Transfer Context ID: "+dataTranferContextID+";Application Protocol: "+applicationProtocol+";Transfer Completion Status: "+str(dataCompletionStatus)
        
        if transferTime > 0:
            dataOfDCOMP += ';Total Transfer time: '+str(transferTime)
            
        if protocolError == True:
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                cause = line[5 + NumberOfContextID]
                if applicationProtocol == 'FTP' or applicationProtocol == 'SFTP':
                    cause = parseDAFFtpSftpFailStatus(int(cause))
                elif applicationProtocol == 'HTTP':
                    cause = parseDAFHttpFailStatus(int(cause))
                elif applicationProtocol == 'MMS' or applicationProtocol == 'WAP 1.0' or applicationProtocol == 'WAP 2.0':
                    cause = parseDAFMmsWapFailStatus(int(cause))
            dataOfDCOMP += ";Cause: "+cause
            
        if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
            logObj.ipAccessTime = line[6+NumberOfContextID]
        if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
            logObj.ipTerminationTime = line[7+NumberOfContextID]
        if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
            logObj.ULBytes = line[8+NumberOfContextID]
        if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
            logObj.DLBytes = line[9+NumberOfContextID]
        if ((10 + NumberOfContextID) < length) and (line[10+NumberOfContextID] != '') :
            logObj.headerTransferTime = line[10+NumberOfContextID]
        if ((11 + NumberOfContextID) < length) and (line[11+NumberOfContextID] != '') :
            logObj.TCPConnectionTime = line[11+NumberOfContextID]
        if ((12 + NumberOfContextID) < length) and (line[12+NumberOfContextID] != '') :
            logObj.RedirectAddress = line[12+NumberOfContextID]
            
        logObj.eventInfo = dataOfDCOMP
        return 1
    else:
        dataOfDCOMP = "No of context id not found"
        return 0
#     except:
#         return 0






