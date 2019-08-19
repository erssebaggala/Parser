#!/usr/bin/env python
# coding: utf-8

# In[27]:
# Call Disconnect
# Parameters |Parameters for non-VoIP GSM, UMTS FDD, UMTS TDSCDMA, and GAN WLAN |Parameters for nonVoIP TETRA |
# Parameters for non-VoIP cdmaOne, CDMA 1x, and EVDO |Parameters for iDEN |Parameters for VoIP |Parameters for Skype |
# Parameters for QChat |Parameters for Kodiak |Parameters for VoLTE |Parameters for iDEN push-to-talk
# Items Sequence
# 1.  EventID = CAD                   [0]
# 2.  Time                            [1]
# 3.  Call Context ID Count           [2] = N
# 3a. Call Context ID                 [N]
# 4.  Measured System                 [3+N]
# 5.  Call Type                       [4+N]
# 6.  CS Disconnect Status            [5+N]
# Call End, CS Call End Released
# 7.  CS call disconnect cause        [6+N]
# CASE non-TETRA
# 7.  CS call disconnect cause        [6+N]
# CASE non-VoIP cdmaOne, CDMA 1x, and EVDO
# 7.  CS call disconnect cause        [6+N]
# CASE iDEN
# 7.  CS call disconnect cause        [6+N]
# CASE VoIP
# 7.  CS call disconnect cause        [6+N]
# CASE Skype
# 7.  CS call disconnect cause        [6+N]
# CASE QChat
# 7.  CS call disconnect cause        [6+N]
# CASE Kodiak
# 7.  CS call disconnect cause        [6+N]
# CASE IMS-based call
# 7.  CS call disconnect cause        [6+N]
# CASE IDEN Push-to-talk
# 7.  CS call disconnect cause        [6+N]

#This will have a dictionary of all the Call Context IDs
#atm, dictionary is accumulating all the data from Calls
#present

from MeasureSysConverter import MeasureSysConverter
from ParseCallTypes import ParseCallType
from LogDTClass import LogDT
from CallContextId import CallContextID
from ParseCAFFailStatus import parseCAFFailStatus
from ParseCAFDisconnectCause import parseCAFDisconnectCause
import datetime
from datetime import datetime, date
import time
from ParseCADDropStatus import parseCADDropStatus
from ParseCADDisconnectionCause import parseCADDisconnectionCause


# In[28]:


def ParseCAD (line, logObj,dictionary):
    try:
        dataOfCAD = ""
        length = len(line)
        if 2 < length:
            contextID = "UnKnown"
            measureSystem = "UnKnown"
            callType = "UnKnown"
            callDuration = 0
            dropStatus = 'Unknown'

            logObj.time = line[1]
            logObj.event = "Dropped Call"
            logObj.msgType = "Disconnect"

            NumberOfContextID = int(line[2])

            if (3 < length) and (line[3] != ''):
                contextID = line[3]
            logObj.callContextID = contextID

            if contextID in dictionary:
                callContextObj = dictionary[contextID]
            else:
                callContextObj = CallContextID()
                dictionary[contextID] = callContextObj
                callContextObj = dictionary[contextID]

            callContextObj.CallEnd = logObj.time
            tdelta = datetime.strptime(callContextObj.CallEnd.split('.', 1)[0], '%H:%M:%S') - datetime.strptime(callContextObj.CallEstablished.split('.', 1)[0], '%H:%M:%S')        
            callDuration = float(tdelta.seconds)*1000 #MilliSeconds 

            if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
                measureSystem = line[3+NumberOfContextID]
                measureSystem = MeasureSysConverter(int(measureSystem))
            if ((4+NumberOfContextID) < length) and (line[4+NumberOfContextID] != ''):
                callType = line[4+NumberOfContextID]
                callType = ParseCallType(int(callType))


            dataOfCAD = "Context ID:"+contextID+";Call Type:"+callType+";Measure System:"+measureSystem

            if ((5+NumberOfContextID) < length) and (line[5+NumberOfContextID] != ''):
                dropStatus = line[5+NumberOfContextID]
                if dropStatus == '1':
                    logObj.event = 'Call End'
                    logObj.msgType = 'Released'
                elif dropStatus == '14':
                    logObj.event = 'CS Call End'
                dropStatus = parseCADDropStatus(int(dropStatus))

            dataOfCAD += ";Call Duration: "+str(callDuration) + ";End Status:"+dropStatus

            if measureSystem == 'GSM' or measureSystem == 'UMTS FDD' or measureSystem == 'UMTS TDSCDMA' or measureSystem == 'GAN WLAN':
                disConnectionCause = 'Unknown'
                if ((6+NumberOfContextID) < length) and (line[6+NumberOfContextID] != ''):
                    disConnectionCause = int(line[6+NumberOfContextID])
                    if disConnectionCause == 17:
                        logObj.event = 'CS Call End - Rejected'
                    elif disConnectionCause == 27:
                        logObj.event = 'Dropped Call - Abnoraml'
                    disConnectionCause = parseCADDisconnectionCause(int(disConnectionCause))
                dataOfCAD += ";Disconnection Cause:"+disConnectionCause

            logObj.eventInfo = dataOfCAD
            logObj.modeSystem = measureSystem
            return 1
        else:
            dataOfCAD = "No of context id not found"
            return 0
    except:
        return 0


