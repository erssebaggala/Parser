#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from parseCHIEXTChannelType import parseCHIEXTChannelType
from parseCHITransmissionType import parseCHITransmissionType
from ParseCellMeasuresParseBand import parseCellMeasuresParseBand

def ParseCHI (line, logObj):
    dataOfCHI = ""
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        callContextID = 0
        CHIType = 0
        mmCause = 0
        logObj.event = "Parse Channel info"
        logObj.msgType = 'Channel Information'
        logObj.time = line[1]  
        if (3 < length) and (line[3] != ''):
            CHIContextID = line[3]
        if int(CHIContextID) > 0:
            dataOfCHI = 'Call Context ID: ' + CHIContextID
                   
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.modeSystem = MeasureSysConverter(int(line[3 + NumberOfContextID]))
        if logObj.modeSystem == 'GSM':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.Band = parseCellMeasuresParseBand(int(line[4 + NumberOfContextID]))
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                if(line[5+NumberOfContextID] == '1'):
                    logObj.channelType = 'Control channel'
                elif(line[5+NumberOfContextID] == '2'):
                    logObj.channelType = 'Traffic channel'
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.ChannelNum = int(line[6+NumberOfContextID])
            if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                logObj.CellId = int(line[7+NumberOfContextID])
            if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                logObj.LAC = int(line[8+NumberOfContextID])
            if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
                logObj.DTXUL = int(line[9+NumberOfContextID])
            if ((10 + NumberOfContextID) < length) and (line[10+NumberOfContextID] != '') :
                logObj.RLTMax = int(line[10+NumberOfContextID])
            if ((11 + NumberOfContextID) < length) and (line[11+NumberOfContextID] != '') :
                logObj.EXTChannelType = parseCHIEXTChannelType(line[11+NumberOfContextID])
            if ((12 + NumberOfContextID) < length) and (line[12+NumberOfContextID] != '') :
                logObj.TSL = int(line[12+NumberOfContextID])
            if ((13 + NumberOfContextID) < length) and (line[13+NumberOfContextID] != '') :
                logObj.BCCHChannel = int(line[13+NumberOfContextID])
            if ((14 + NumberOfContextID) < length) and (line[14+NumberOfContextID] != '') :
                logObj.BSIC = int(line[14+NumberOfContextID])
            if ((15 + NumberOfContextID) < length) and (line[15+NumberOfContextID] != '') :
                logObj.BCCHBand = parseCellMeasuresParseBand(line[15+NumberOfContextID])
            
        elif logObj.modeSystem == 'UMTS FDD':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.Band = parseCellMeasuresParseBand(int(line[4 + NumberOfContextID]))
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                if(line[5+NumberOfContextID] == '1'):
                    logObj.RRCState = 'Idle'
                elif(line[5+NumberOfContextID] == '2'):
                    logObj.RRCState = 'URA PCH'
                elif(line[5+NumberOfContextID] == '3'):
                    logObj.RRCState = 'Cell PCH'
                elif(line[5+NumberOfContextID] == '4'):
                    logObj.RRCState = 'Cell FACH'
                elif(line[5+NumberOfContextID] == '5'):
                    logObj.RRCState = 'Cell DCH'
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.ChannelNum = int(line[6+NumberOfContextID])
            if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                logObj.CellId = int(line[7+NumberOfContextID])
            if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                logObj.LAC = int(line[8+NumberOfContextID])
            if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
                logObj.AdditionalWindow = float(line[9+NumberOfContextID])
            if ((10 + NumberOfContextID) < length) and (line[10+NumberOfContextID] != '') :
                logObj.TtT1A = int(line[10+NumberOfContextID])
            if ((11 + NumberOfContextID) < length) and (line[11+NumberOfContextID] != '') :
                logObj.DropWindow = float(line[11+NumberOfContextID])
            if ((12 + NumberOfContextID) < length) and (line[12+NumberOfContextID] != '') :
                logObj.TtT1B = int(line[12+NumberOfContextID])
            if ((13 + NumberOfContextID) < length) and (line[13+NumberOfContextID] != '') :
                logObj.ReplacementWindow = float(line[13+NumberOfContextID])
            if ((14 + NumberOfContextID) < length) and (line[14+NumberOfContextID] != '') :
                logObj.TtT1C = int(line[14+NumberOfContextID])
            if ((15 + NumberOfContextID) < length) and (line[15+NumberOfContextID] != '') :
                logObj.DLSF = int(line[15+NumberOfContextID])
            if ((16 + NumberOfContextID) < length) and (line[16+NumberOfContextID] != '') :
                logObj.MinULSF = int(line[16+NumberOfContextID])
            if ((17 + NumberOfContextID) < length) and (line[17+NumberOfContextID] != '') :
                logObj.DRXcycle = int(line[17+NumberOfContextID])
            if ((18 + NumberOfContextID) < length) and (line[18+NumberOfContextID] != '') :
                logObj.MaxTXPower = float(line[18+NumberOfContextID])
            if ((19 + NumberOfContextID) < length) and (line[19+NumberOfContextID] != '') :
                logObj.Treselection = int(line[19+NumberOfContextID])
        elif logObj.modeSystem == 'LTE TDD' or logObj.modeSystem == 'LTE FDD':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.Band = parseCellMeasuresParseBand(int(line[4 + NumberOfContextID]))
            if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
                if(line[5+NumberOfContextID] == '1'):
                    logObj.RRCState = 'Idle'
                elif(line[5+NumberOfContextID] == '2'):
                    logObj.RRCState = 'Connected'
            if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
                logObj.ChannelNum = int(line[7+NumberOfContextID])
            if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
                logObj.PCI = int(line[8+NumberOfContextID])
            if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
                logObj.CellId = int(line[9+NumberOfContextID])
            if ((10 + NumberOfContextID) < length) and (line[10+NumberOfContextID] != '') :
                logObj.TAC = int(line[10+NumberOfContextID])
            if ((12 + NumberOfContextID) < length) and (line[12+NumberOfContextID] != '') :
                logObj.TransmissionMode = parseCHITransmissionType(int(line[12+NumberOfContextID]))
        logObj.eventInfo = dataOfCHI 
        return 1
    
    else:
        dataOfCHI = "No of context id not found"
        return 0
#     except:
#         return 0

