#!/usr/bin/env python
# coding: utf-8

# In[49]:

# Data Transfer Request
# Parameters
# Items Sequence
# 1.  EventID = DREQ              [0]
# 2.  Time                        [1]
# 3.  Context ID Count            [2] = N
# 3a. Data Connection Context ID  [N]
# 4.  Application Protocol        [3+N]
# 5.  Transfer Direction          [4+N]
# Parameter for Nemo test protocol
# 6.  File Size                   [5+N]
# 7.  Packet Size                 [6+N]
# 8.  Rate limit                  [7+N]
# 9.  Ping size                   [8+N]
# 10. Ping Rate                   [9+N]
# 11. Ping timeout                [10+N]
# Parameter for FTP and SFTP
# 6.  File Size                   [5+N]
# 7.  File Name                   [6+N]
# 8.  Transfer Attempt #          [7+N]
# 9.  Threads                     [8+N]
# 10. Timeout                     [9+N]
# Parameter for HTTP
# 6.  File Size                   [5+N]
# 7.  File Name                   [6+N]
# 8.  Transfer Attempt #          [7+N]
# 9.  Threads                     [8+N]
# 10. Timeout                     [9+N]
# Parameter for SMTP
# 6.  File Size                   [5+N]
# 7.  File Name                   [6+N]
# 8.  Timeout                     [7+N]
# Parameter for POP3
# 6.  File Size                   [5+N]
# 7.  File Name                   [6+N]
# 8.  Timeout                     [7+N]
# Parameter for MMS
# 6.  MMS File Size               [5+N]
# 7.  MMS File Name               [6+N]
# 8.  Timeout                     [7+N]
# Parameter for WAP 1.0 and 2.0
# 6.  File Size                   [5+N]
# 7.  File Name                   [6+N]
# 8.  Timeout                     [7+N]
# Parameter for Streaming
# 6.  File Size                   [5+N]
# 7.  File Name                   [6+N]
# 8.  Timeout                     [7+N]
# Parameter for HTTP Browsing
# 7.  File Name                   [5+N]
# 8.  Timeout                     [6+N]
# Parameter for ICMP Ping
# 6.  Ping Size                   [5+N]
# 7.  Ping Rate                   [6+N]
# 8.  Ping Timeout                [7+N]
# 9.  Data connection context ID  [8+N]
# Parameter for IPref over TCP
# 6.  Data Size                   [5+N]
# 7.  Threads                     [6+N]
# 8.  Timeout                     [7+N]
# Parameter for IPref over UDP
# 6.  Data Size                   [5+N]
# 7.  Threads                     [6+N]
# 8.  Timeout                     [7+N]
# Parameter for trace route
# 6.  Packet Size                 [5+N]
# 7.  Timeout                     [6+N]
# 8.  TTL                         [7+N]
# 9.  Hop timeout                 [8+N]
# Parameter for IMAP
# 6.  File Size                   [5+N]
# 7.  File Name                   [6+N]
# 8.  Timeout                     [7+N]
# Parameter for Facebook
# 6.  Facebook Operation          [5+N]
# 7.  Timeout                     [6+N]
# Parameter for Twitter
# 6.  Twitter Operation           [5+N]
# 7.  Timeout                     [6+N]
# Parameter for Instagram
# 6.  Instagram Operation         [5+N]
# 7.  Timeout                     [6+N]
# Parameter for Linkedin
# 6.  Linkedin Operation          [5+N]
# 7.  Timeout                     [6+N]
# Parameter for PEVQ-S
# 6.  File Name                   [5+N]
# 7.  Timeout                     [6+N]
# Parameter for Dropbox
# 6.  Dropbox Operation           [5+N]
# 7.  File Name                   [6+N]
# 8.  Timeout                     [7+N]
# 9.  File Size                   [8+N]

#This will have a dictionary of all the DATA Connection Context IDs
#atm, dictionary is accumulating all the data from data connections
#present

from LogDTClass import LogDT
from DataConnectionEventInfo import DataConnectionEventInfo
from ParseApplicationProtocol import ParseApplicationProtocol


# In[50]:


def ParseDREQ (line, logObj, dictionary):
    dataOfDREQ = ""
    length = len(line)
    if 2 < length:
        dataConnectionContextID = "UnKnown"
        applicationProtocol = "Unknown"
        NumberOfContextID = int(line[2])

        logObj.event = "Data Tranfer Request"
        logObj.msgType = 'Disconnect'
        applicationProtocolInt = -1
        operation = ''
        direction = 0
        
        if (3 < length) and (line[3] != ''):
            dataTranferContextID = line[3]
        if (4 < length) and (line[4] != '') and NumberOfContextID > 1:
            dataConnectionContextID = line[4]

        if dataConnectionContextID in dictionary:
            dataContextObj = dictionary[dataConnectionContextID]
        else:
            dataContextObj = DataConnectionEventInfo()
            dictionary[dataConnectionContextID] = dataContextObj
            dataContextObj = dictionary[dataConnectionContextID]

        dataContextObj.DataTransferRequestTime = line[1]
        
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.applicationProtocol = line[3 + NumberOfContextID]
            applicationProtocol = ParseApplicationProtocol(int(logObj.applicationProtocol))
            dataContextObj.ApplicationProtocol = applicationProtocol
            
            applicationProtocolInt = int (line[3 + NumberOfContextID])
            
        logObj.direction = 'NA'
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            
            direction = int (line[4 + NumberOfContextID])
            if direction == 1:
                logObj.direction = 'UL'
            elif direction == 2:
                logObj.direction = 'DL'
            elif direction == 3:
                logObj.direction = 'UD'
                
        if applicationProtocolInt >= 0:
            if applicationProtocolInt == 0 or applicationProtocolInt == 1 or applicationProtocolInt == 2:
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    logObj.fileSize = int(line[5+NumberOfContextID])
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.packetSize = int(line[6 + NumberOfContextID])
                if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                    logObj.rateLimit = int(line[7 + NumberOfContextID])
                if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                    logObj.pingSize = int(line[8 + NumberOfContextID])
                if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
                    logObj.pingRate = int(line[9 + NumberOfContextID])
                if ((10 + NumberOfContextID) < length) and (line[10+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[10 + NumberOfContextID])    
                
            elif applicationProtocolInt == 3 or applicationProtocolInt == 4 or applicationProtocolInt == 16:#FTP, HTTP, SFTP......
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    logObj.fileSize = int(line[5+NumberOfContextID])
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.fileName = line[6 + NumberOfContextID]
                if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                    logObj.tranferAttemptNumber = int(line[7 + NumberOfContextID])
                if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                    logObj.thread = int(line[8 + NumberOfContextID])
                if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[9 + NumberOfContextID])
                
            elif (applicationProtocolInt >= 5 and applicationProtocolInt <=10) or applicationProtocolInt == 17:#SMTP, POP3, MMS,WAP 1.0, STREAMING,WAP 2.0, IMAP
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    logObj.fileSize = int(line[5+NumberOfContextID])
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.fileName = line[6 + NumberOfContextID]
                if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[7 + NumberOfContextID])
                    
            elif applicationProtocolInt == 11:#HTTP Browsing........
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    logObj.fileName = line[5+NumberOfContextID]
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[6 + NumberOfContextID])
                
            elif applicationProtocolInt == 12:#ICMP ping
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    logObj.pingSize = int(line[5+NumberOfContextID])
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.pingRate = int(line[6 + NumberOfContextID])
                if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[7 + NumberOfContextID])
                
            elif applicationProtocolInt == 13 or applicationProtocolInt == 14:#IPerf over TCP and UDP
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    logObj.fileSize = int(line[5+NumberOfContextID])
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.thread = int(line[6 + NumberOfContextID])
                if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[7 + NumberOfContextID])
                
            elif applicationProtocolInt == 15:#TraceRoute.........
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    logObj.packetSize = int(line[5+NumberOfContextID])
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[6 + NumberOfContextID])
                    
                
            elif applicationProtocolInt == 18:#Facebook......
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    operation = int(line[5+NumberOfContextID])
                    if operation == 1:
                        operation = 'Get user feed'
                    elif operation == 2:
                        operation = 'Get friend list'
                    elif operation == 3:
                        operation = 'Post a status update'
                    elif operation == 4:
                        operation = "Post an image"
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[6 + NumberOfContextID])
                
            elif applicationProtocolInt == 19:#Twitter.......
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    operation = int(line[5+NumberOfContextID])
                    if operation == 1:
                        operation = 'Load home page'
                    elif operation == 2:
                        operation = 'Load profile'
                    elif operation == 3:
                        operation = 'Follow Twitter feed'
                    elif operation == 4:
                        operation = 'Text tweet'
                    elif operation == 5:
                        operation = '"Photo tweet'
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[6 + NumberOfContextID])
                
            elif applicationProtocolInt == 20:#Instagram.......
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    operation = int(line[5+NumberOfContextID])
                    if operation == 1:
                        operation = 'Load User Feed'
                    elif operation == 2:
                        operation = 'Load self feed'
                    elif operation == 3:
                        operation = 'Load popular feed'
                    elif operation == 4:
                        operation = "Search media with a tag"
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[6 + NumberOfContextID])
                    
                
            elif applicationProtocolInt == 21:#Linked In...........
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    operation = int(line[5+NumberOfContextID])
                    if operation == 1:
                        operation = 'Load Self Feed'
                    elif operation == 2:
                        operation = 'Load Profile from Contact List'
                    elif operation == 3:
                        operation = 'Load Profile using Public URL'
                    elif operation == 4:
                        operation = 'Share Text and URL'
                    elif operation == 5:
                        operation = 'Load My Info'
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[6 + NumberOfContextID])
                    
            elif applicationProtocolInt == 22:#PEVQ...........
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    logObj.fileName = line[5+NumberOfContextID]
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[6 + NumberOfContextID])
                    
            elif applicationProtocolInt == 23:#DropBox.........
                if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                    operation = int(line[5+NumberOfContextID])
                    if operation == 1:
                        operation = 'Upload'
                    elif operation == 2:
                        operation = 'Download'
                if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                    logObj.fileName = line[6 + NumberOfContextID]
                if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                    logObj.timeOut = int(line[7 + NumberOfContextID])
                if ((8+ NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                    logObj.fileSize = int(line[8 + NumberOfContextID])                    

        dataOfDREQ = "Data Transfer Context ID: "+dataTranferContextID+";Data Connection Context ID: "+dataConnectionContextID+";Application Protocol: "+applicationProtocol

        if operation != '':
            dataOfDREQ += ";Operation: "+operation
            
        logObj.eventInfo = dataOfDREQ
        return 1
    else:
        dataOfDREQ = "No of context id not found"
        return 0
#     except:
#         return 0


# In[ ]:




