#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from ParseMessageType import ParseMessageType

def ParseMSGA (line, logObj):
    dataOfParseMSGA = ''
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])     
        logObj.event = "Message Sending/Receiving Attempt"
        logObj.msgType = 'Attempt'
        logObj.time = line[1]  
        msgType = -1
        transportProtocol = -1
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            logObj.MessagingType = ParseMessageType(line[4+NumberOfContextID])
        if (logObj.MessagingType == "SMS") or (logObj.MessagingType == "IMS SMS"):
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                dataOfParseMSGA = 'SMS ContextID: ' + line[5+NumberOfContextID]
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                msgType = "Unknown"
                try:
                    msgType = int(line[6+NumberOfContextID])
                except:
                    pass
                if msgType == 1:
                    logObj.smsMessageType = 'Receive' #add
                elif msgType == 2:
                    logObj.smsMessageType = 'Send' #add
                elif msgType == 3:
                    logObj.smsMessageType = 'Status Report' #add
                elif msgType == 4:
                    logObj.smsMessageType = 'Command' #add
                elif msgType == 5:
                    logObj.smsMessageType = 'Broadcast' #add
            if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                logObj.SMSNumber = line[7+NumberOfContextID]#add
            if ((11 + NumberOfContextID) < length) and (line[11+NumberOfContextID] != '') :
                logObj.SMSTimeout = int(line[11+NumberOfContextID])#add
        elif logObj.MessagingType == "MMS":
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                dataOfParseMSGA = 'MMS ContextID: ' + line[5+NumberOfContextID]
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                msgType = int(line[6+NumberOfContextID])
                if msgType == 1:
                    logObj.mmsMessageType = 'Send' #add
                elif msgType == 2:
                    logObj.mmsMessageType = 'Retrieve' #add
                elif msgType == 3:
                    logObj.mmsMessageType = 'Notification' #add
                elif msgType == 4:
                    logObj.mmsMessageType = 'Delivery Report' #add
            if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                transportProtocol = int(line[7+NumberOfContextID])
                if transportProtocol == 1:
                    logObj.mmsTransportProtocol = 'WAP 1.0' #add
                elif transportProtocol == 2:
                    logObj.mmsTransportProtocol = 'SMS' #add
                elif transportProtocol == 3:
                    logObj.mmsTransportProtocol = 'WAP 2.0' #add
            if ((11 + NumberOfContextID) < length) and (line[11+NumberOfContextID] != '') :
                logObj.MMSTimeout = int(line[11+NumberOfContextID])#add
        elif logObj.MessagingType == "USSD":
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                dataOfParseMSGA = 'USSD ContextID: ' + line[5+NumberOfContextID]
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                dataOfParseMSGA += ';USSD Sequencey Context ID: ' + line[6+NumberOfContextID]
            if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                msgType = int(line[7+NumberOfContextID])
                if msgType == 1:
                    logObj.USSDMessageType = 'Mobile request' #add
                elif msgType == 2:
                    logObj.USSDMessageType = 'Mobile response' #add
                elif msgType == 3:
                    logObj.USSDMessageType = 'Network request' #add
                elif msgType == 4:
                    logObj.USSDMessageType = 'Network response' #add
                elif msgType == 5:
                    logObj.USSDMessageType = 'Network notification' #add
        logObj.eventInfo = dataOfParseMSGA
        return 1    
    else:
        return 0
#     except:
#         return 0               
            
                                                

