#!/usr/bin/env python
# coding: utf-8

# In[47]:
# VoIP information
# Parameters |Parameters for VoIP |Parameters for IMS Call
# Items Sequence
# 1.  EventID = CAC                   [0]
# 2.  Time                            [1]
# 3.  Call Context ID Count           [2] = N
# 3a. Call Context ID                 [N]
# 4.  VoIP Type                       [3+N]
# 5.  Additional Paramter Count       [4+N]
# CASE VoIP
# 6.  VoIP codec                      [5+N]
# CASE IMS Call
# 6.  VoIP codec                      [5+N]
# 7.  SIP handshake time              [6+N]
# 8.  VoIP Video Codec                [7+N]

from LogDTClass import LogDT


# In[48]:


def ParseVOIPI (line, logObj):
    try:
        dataOfVOIPI = ""
        length = len(line)
        if 2 < length:
            contextID = "UnKnown"
            additionalParameters = "UnKnown"
            voipType = "UnKnown"
            logObj.time = line[1]
            logObj.event = "VOIP Information"
            logObj.msgType = "Information Update"

            NumberOfContextID = int(line[2])

            if (3 < length) and (line[3] != ''):
                contextID = line[3]
            logObj.callContextID = contextID
            if ((4+NumberOfContextID) < length) and (line[4+NumberOfContextID] != ''):
                additionalParameters = int(line[4+NumberOfContextID])
            if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
                voipType = int(line[3+NumberOfContextID])
                if voipType == 1:
                    voipType = "VoIP"
                    if additionalParameters == 1 and ((5+NumberOfContextID) < length) and (line[5+NumberOfContextID] != ''):
                        lobObj.speechCodec = line[5+NumberOfContextID]
                        
                elif voipType == 3 or voipType == 4:
                    voipType = "IMS voice/Video"
                    if additionalParameters == 1 and ((5+NumberOfContextID) < length) and (line[5+NumberOfContextID] != ''):
                        lobObj.speechCodec = line[5+NumberOfContextID]
                    elif additionalParameters == 2 and ((5+NumberOfContextID) < length) and (line[5+NumberOfContextID] != ''):
                        lobObj.speechCodec = line[5+NumberOfContextID]
                        dataOfVOIPI = "SIP Handshake Time: "+line[6+NumberOfContextID]+"ms; VoIP Video Codec: "+line[7+NumberOfContextID]
            
            dataOfVOIPI += ";VOIP Type: "+ voipType

            if logObj.eventInfo == '':
                logObj.eventInfo = dataOfVOIPI
            else:
                logObj.eventInfo += dataOfVOIPI
            return 1
        else:
            dataOfVOIPI = "No of context id not found"
            return 0
    except:
        return 0


# In[ ]:




