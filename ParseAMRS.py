#!/usr/bin/env python
# coding: utf-8

# In[2]:

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from ParseAMRCodec import ParseAMRCodec
def ParseAMRS (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])        
        logObj.event = "AMR Status"
        logObj.msgType = ''
        logObj.time = line[1]  
        chi = 0
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        if logObj.modeSystem == 'GSM':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.AMRModeUL = ParseAMRCodec(int(line[4 + NumberOfContextID])) #add this
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                logObj.AMRModeDL = ParseAMRCodec(int(line[5 + NumberOfContextID]))
            if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                chi = int(line[8 + NumberOfContextID])
                if chi == 1:
                    logObj.AMRICMI = "Half rate"
                elif chi == 2:
                    logObj.AMRICMI = "Full rate"
                elif chi == 3:
                    logObj.AMRICMI = "Wideband rate"
        elif logObj.modeSystem == 'UMTS FDD' or logObj.modeSystem == 'UMTS TD-SCDMA' or logObj.modeSystem == 'LTE FDD' or logObj.modeSystem == 'LTE TDD':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.AMRModeUL = ParseAMRCodec(int(line[4 + NumberOfContextID])) 
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                logObj.AMRModeDL = ParseAMRCodec(int(line[5 + NumberOfContextID]))
        return 1
    
    else:
        return 0
#     except:
#         return 0


# In[ ]:




