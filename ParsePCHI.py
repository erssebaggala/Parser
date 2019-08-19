#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from ParsePacketTechnology import parsePacketTechnology
from ParsePacketState import parsePacketState
# In[1]:


def ParsePCHI (line, logObj):
    length = len(line)
    if 2 < length:
        dataOfPCHI = ''
        PCHIContextID = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if(3 < length) and (line[3] != '') :
                    PCHIContextID = int(line[3])

        logObj.event = 'Parse Packet Channel Information'     
        dataOfPCHI = "Call Context ID: " + str(PCHIContextID)
        
        if((3 + NumberOfContextID) < length) and (line[3 + NumberOfContextID] != '') : 
            measureSystem = MeasureSysConverter (int(line[3 + NumberOfContextID]))           
        if measureSystem == 'GSM':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                logObj.PacketTechnology = parsePacketTechnology(int(line[4 + NumberOfContextID]))
            if((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') : 
                logObj.PacketState = parsePacketState(int(line[5 + NumberOfContextID]))
            if((6 + NumberOfContextID) < length) and (line[6 + NumberOfContextID] != '') : 
                logObj.RAC = int(line[6 + NumberOfContextID])
            if((10 + NumberOfContextID) < length) and (line[10 + NumberOfContextID] != '') : 
                logObj.PSCodingUL = "MCS-"+ (line[10 + NumberOfContextID])
            if((11 + NumberOfContextID) < length) and (line[11 + NumberOfContextID] != '') : 
                logObj.PSCodingDL ='MCS-'+(line[11 + NumberOfContextID])
            if((12 + NumberOfContextID) < length) and (line[12 + NumberOfContextID] != '') : 
                logObj.PSTSLULNumber = int(line[12 + NumberOfContextID])
            if((13 + NumberOfContextID) < length) and (line[13 + NumberOfContextID] != '') : 
                logObj.PSTSLDLNumber = int(line[13 + NumberOfContextID])
                
            cution = (logObj.PSTSLULNumber) + (logObj.PSTSLDLNumber)
                
            if((14 + NumberOfContextID+cution) < length) and (line[14 + NumberOfContextID + cution] != '') : 
                logObj.NMO = "NMO-"+(line[14 + NumberOfContextID+cution])
            if((15 + NumberOfContextID+cution) < length) and (line[15 + NumberOfContextID+cution] != '') : 
                logObj.NCO = "NC-"+(line[15 + NumberOfContextID+cution])
            if((18 + NumberOfContextID+cution) < length) and (line[18 + NumberOfContextID+cution] != '') : 
                logObj.CLRSHyst = float(line[18 + NumberOfContextID+cution])
            if((19 + NumberOfContextID+cution) < length) and (line[19 + NumberOfContextID+cution] != '') : 
                logObj.CLRSTime = int(line[19 + NumberOfContextID+cution])
        
        if measureSystem == 'UMTS FDD':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                logObj.PacketTechnology = parsePacketTechnology(int(line[4 + NumberOfContextID]))
            if((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') : 
                logObj.PacketState = parsePacketState(int(line[5 + NumberOfContextID]))
            if((6 + NumberOfContextID) < length) and (line[6 + NumberOfContextID] != '') : 
                logObj.RAC = int(line[6 + NumberOfContextID])
            if((7 + NumberOfContextID) < length) and (line[7 + NumberOfContextID] != '') : 
                logObj.NMO = "NMO-"+ (line[7 + NumberOfContextID])
            if((8 + NumberOfContextID) < length) and (line[8 + NumberOfContextID] != '') : 
                logObj.HSDPACategory = int (line[8 + NumberOfContextID])
            if((9 + NumberOfContextID) < length) and (line[9 + NumberOfContextID] != '') : 
                logObj.HSDSCHSC = int(line[9 + NumberOfContextID])
            if((11 + NumberOfContextID) < length) and (line[11 + NumberOfContextID] != '') : 
                logObj.PowerOffset = float(line[11 + NumberOfContextID])

            if((14 + NumberOfContextID) < length) and (line[14 + NumberOfContextID ] != '') : 
                logObj.HSUPAUECategory = int(line[14 + NumberOfContextID])
            if((15 + NumberOfContextID) < length) and (line[15 + NumberOfContextID] != '') : 
                logObj.TTI = int(line[15 + NumberOfContextID])
            if((17 + NumberOfContextID) < length) and (line[17 + NumberOfContextID] != '') : 
                rateMaching= int(line[17 + NumberOfContextID])
                if rateMaching == 1:
                    logObj.RateMatching = "Chase Combining"
                elif rateMaching == 2:
                    logObj. RateMatching = "Incremental Redundancy"
             
            if((20 + NumberOfContextID) < length) and (line[20 + NumberOfContextID] != '') : 
                logObj.EDPCCHPowerOffset = float(line[20 + NumberOfContextID])
            if((24 + NumberOfContextID) < length) and (line[24 + NumberOfContextID] != '') : 
                rateMaching= int(line[24 + NumberOfContextID])
                if rateMaching == 1:
                    logObj.HSDPA64QAM = "Disabled"
                elif rateMaching == 2:
                    logObj. HSDPA64QAM = "Enabled"
            if((25 + NumberOfContextID) < length) and (line[25 + NumberOfContextID] != '') : 
                rateMaching= int(line[25 + NumberOfContextID])
                if rateMaching == 1:
                    logObj.HSDPAMIMO = "Disabled"
                elif rateMaching == 2:
                    logObj. HSDPAMIMO = "Enabled"
             
            numberOfCells = 0
            if((27 + NumberOfContextID) < length) and (line[27 + NumberOfContextID] != '') : 
                numberOfCells = int(line[27 + NumberOfContextID])
            numberOfParametersPerCell = 0
            if((28 + NumberOfContextID) < length) and (line[28 + NumberOfContextID] != '') : 
                numberOfParametersPerCell = int(line[28 + NumberOfContextID])
             
            for cell in range(0,numberOfCells):
                for param in range(0, numberOfParametersPerCell):
                    itemNumber = 29 + NumberOfContextID + (cell * numberOfParametersPerCell)
                    if((itemNumber) < length) and (line[itemNumber] != ''):
                        if param == 0:
                            logObj.HSDSCHChannel2 = line[itemNumber]
                        elif param == 1:
                            logObj.HSDSCHSC2 = line[itemNumber]
                        elif param == 5:
                            logObj.PowerOffset2 = line[itemNumber]
                        elif param == 6:
                            if line[itemNumber] == '0':
                                logObj.HSDPA64QAM2 = "Disabled"
                            elif line[itemNumber] == '1':
                                logObj.HSDPA64QAM2 = "Enabled"
                                
        
        if measureSystem == 'LTE TDD' or measureSystem == 'LTE FDD':
            if((4 + NumberOfContextID) < length) and (line[4 + NumberOfContextID] != '') : 
                logObj.PacketTechnology = int(line[4 + NumberOfContextID])
            if((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') : 
                logObj.PacketState = int(line[5 + NumberOfContextID])
     
        logObj.modeSystem = measureSystem
        logObj.eventInfo = dataOfPCHI
        return 1

