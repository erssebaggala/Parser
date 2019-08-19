#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter


# In[1]:


def ParseL3SM (line, logObj):
    length = len(line)
    if 2 < length:
        dataOfL3SM = ''
        L3SMContextID = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') :
                    L3SMContextID = int(line[3])

        dataOfL3SM = "Call Context ID: " + str(L3SMContextID)
        
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') : 
            measureSystem = MeasureSysConverter (int(line[3 + NumberOfContextID]))
            logObj.modeSystem = measureSystem
        for i in range(0, (len(line)- 4 + NumberOfContextID)):
            param = i + 4 + NumberOfContextID
            if(param < length) and (line[param] != '') :
                if i == 0:
                    if line[param] == '1':
                        logObj.direction = 'UL'
                    elif line[param] == '2':
                        logObj.direction = 'DL'
                dataOfL3SM += ";Direction: "+logObj.direction
                
                if i == 1:
                    logObj.L3Message = line[param]
                    dataOfL3SM += ";Message: "+logObj.L3Message
                if i == 2:
                    logObj.SubChannel = line[param]
                if i == 3:
                    logObj.L3Channel = int(line[param])
                if i == 4:
                    if measureSystem == 'GSM':
                        logObj.BSIC = int(line[param])
                    elif measureSystem == 'UMTS FDD' or measureSystem == 'UMTS TD-SCDMA' or measureSystem == 'LTE FDD' or measureSystem == 'LTE TDD':
                        logObj.SC = int(line[param])
                if i == 5:
                    if measureSystem == 'GSM': 
                        if int (line[param]) == 1:
                            logObj.L3MessageType = "Normal"
                        elif int (line[param]) == 2:
                            logObj.L3MessageType = "Short L2 header"
                        elif int (line[param]) == 3:
                            logObj.L3MessageType = "8 bit access burst"
                        elif int (line[param]) == 4:
                            logObj.L3MessageType = "11 bit access burst"
                        elif int (line[param]) == 5:
                            logObj.L3MessageType = "11 bit EGRPS access burst"
                        elif int (line[param]) == 6:
                            logObj.L3MessageType = "Message without header"
                            
                        dataOfL3SM += "Message Type: "+(logObj.L3MessageType)
                    elif measureSystem == 'UMTS FDD' or measureSystem == 'UMTS TD-SCDMA' or measureSystem == 'LTE FDD' or measureSystem == 'LTE TDD':
                        logObj.L3Data = line[param]
                if i== 6:
                    if measureSystem == 'GSM': 
                        logObj.L3Data = line[param]
                
        logObj.eventInfo = dataOfL3SM
        logObj.event = "Layer 3 Message - " + logObj.L3Message
        return 1

