#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from LogDTClass import LogDT
from ParseCellMeasuresParseBand import parseCellMeasuresParseBand
def ParseLOCK (line, logObj):
    length = len(line)
    lockType = -1
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        logObj.event = "Message Sending/Receiving Failed"
        logObj.msgType = ''
        logObj.time = line[1]  
        lockType = -1
        selectionType = -1
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.numberOfForcings = int(line[3 + NumberOfContextID]) #add
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            lockType = int(line[4+NumberOfContextID])
            if lockType == 1:
                logObj.lockType = "Channel Lock"
            elif lockType == 2:
                logObj.lockType = "UMTS Sector Lock"
            elif lockType == 3:
                logObj.lockType = "System Lock"
            elif lockType == 4:
                logObj.lockType = "Band Lock"
            elif lockType == 5:
                logObj.lockType = "Cell Barring"
            elif lockType == 6:
                logObj.lockType = "Handover Suppression"
            elif lockType == 7:
                logObj.lockType = "GSM Handover Forcing"
            elif lockType == 8:
                logObj.lockType = "UMTS FDD Handover Forcing"
            elif lockType == 9:
                logObj.lockType = "Radio State Off"
            elif lockType == 10:
                logObj.lockType = "LTE Sector Lock"
            elif lockType == 11:
                logObj.lockType = "LTE Handover Forcing"
            elif lockType == 12:
                logObj.lockType = "PLMN Lock"
        if logObj.lockType == "Channel Lock":
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.LockedChannel = int(line[6+NumberOfContextID])
            if ((6 + NumberOfContextID + 1) < length) and (line[6+NumberOfContextID +1] != '') :
                logObj.LockedBand = parseCellMeasuresParseBand(int(line[6+NumberOfContextID+1]))
        elif logObj.lockType == "UMTS Sector Lock":
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.LockedScramblingCode = int(line[6+NumberOfContextID]) #add
            if ((6 + NumberOfContextID + 1) < length) and (line[6+NumberOfContextID +1] != '') :
                logObj.LockedChannel = int(line[6+NumberOfContextID+1])
            if ((6 + NumberOfContextID + 2) < length) and (line[6+NumberOfContextID +2] != '') :
                logObj.LockedBand = parseCellMeasuresParseBand(int(line[6+NumberOfContextID+2]))
        elif logObj.lockType == "System Lock":
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.LockedSystem = parseCellMeasuresParseBand(int(line[6+NumberOfContextID]))
        elif logObj.lockType == "Band Lock":
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.LockedBand = parseCellMeasuresParseBand(int(line[6+NumberOfContextID]))
        elif logObj.lockType == "Cell Barring":
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                selectionType = int(line[6+NumberOfContextID])
                if selectionType == 1:
                    logObj.CellBarringState = "Normal" #add
                if selectionType == 2:
                    logObj.CellBarringState = "Ignored" #add
                if selectionType == 3:
                    logObj.CellBarringState = "Reversed" #add
        elif logObj.lockType == "GSM Handover Forcing":
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.HOForcingBand = parseCellMeasuresParseBand(int(line[6+NumberOfContextID])) #add
            if ((6 + NumberOfContextID + 1) < length) and (line[6+NumberOfContextID +1] != '') :
                logObj.HOForcingChannel = int(line[6+NumberOfContextID+1])
            if ((6 + NumberOfContextID + 2) < length) and (line[6+NumberOfContextID +2] != '') :
                logObj.HOForcingBSIC = int(line[6+NumberOfContextID+2])
            if ((6 + NumberOfContextID + 3) < length) and (line[6+NumberOfContextID+3] != '') :
                logObj.TargetRXLBias = float(line[6+NumberOfContextID+3]) #add
            if ((6 + NumberOfContextID + 4) < length) and (line[6+NumberOfContextID +4] != '') :
                logObj.TargetRXQBias = int(line[6+NumberOfContextID+4])
            if ((6 + NumberOfContextID + 5) < length) and (line[6+NumberOfContextID +5] != '') :
                logObj.NonTargetRXLBias = float(line[6+NumberOfContextID+5])
            if ((6 + NumberOfContextID + 6) < length) and (line[6+NumberOfContextID +6] != '') :
                logObj.NonTargetRXQBias = int(line[6+NumberOfContextID+6])
        elif logObj.lockType == "UMTS FDD Handover Forcing":
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.HOForcingBand = parseCellMeasuresParseBand(int(line[6+NumberOfContextID])) #add
            if ((6 + NumberOfContextID + 1) < length) and (line[6+NumberOfContextID +1] != '') :
                logObj.HOForcingChannel = int(line[6+NumberOfContextID+1])
            if ((6 + NumberOfContextID + 2) < length) and (line[6+NumberOfContextID +2] != '') :
                logObj.HOForcingSC = int(line[6+NumberOfContextID+2])
            if ((6 + NumberOfContextID + 3) < length) and (line[6+NumberOfContextID+3] != '') :
                logObj.TargetRSCPBias = float(line[6+NumberOfContextID+3]) #add
            if ((6 + NumberOfContextID + 4) < length) and (line[6+NumberOfContextID +4] != '') :
                logObj.TargetEcNoBias = float(line[6+NumberOfContextID+4])
            if ((6 + NumberOfContextID + 5) < length) and (line[6+NumberOfContextID +5] != '') :
                logObj.NonTargetRSCPBias = float(line[6+NumberOfContextID+5])
            if ((6 + NumberOfContextID + 6) < length) and (line[6+NumberOfContextID +6] != '') :
                logObj.NonTargetEcNoBias = float(line[6+NumberOfContextID+6])
        elif logObj.lockType == "LTE Sector Lock":
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.LockedPCI = int(line[6+NumberOfContextID]) #add
            if ((6 + NumberOfContextID + 1) < length) and (line[6+NumberOfContextID +1] != '') :
                logObj.LockedChannel = int(line[6+NumberOfContextID+1])
            if ((6 + NumberOfContextID + 2) < length) and (line[6+NumberOfContextID +2] != '') :
                logObj.LockedBand = int(line[6+NumberOfContextID+2])
        elif logObj.lockType == "LTE Handover Forcing":
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                logObj.HOForcingBand = parseCellMeasuresParseBand(int(line[6+NumberOfContextID])) #add
            if ((6 + NumberOfContextID + 1) < length) and (line[6+NumberOfContextID +1] != '') :
                logObj.HOForcingChannel = int(line[6+NumberOfContextID+1])
            if ((6 + NumberOfContextID + 2) < length) and (line[6+NumberOfContextID +2] != '') :
                logObj.HOForcingPCI = int(line[6+NumberOfContextID+2])
        elif logObj.lockType == "PLMN Lock":
            if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
                selectionType = int(line[6+NumberOfContextID])
                if selectionType == 1:
                    logObj.PLMNSelectionMode = "Manual" #add
                if selectionType == 2:
                    logObj.PLMNSelectionMode = "Deregistered" #add
            if ((6 + NumberOfContextID + 1) < length) and (line[6+NumberOfContextID +1] != '') :
                logObj.mcc = int(line[6+NumberOfContextID+1])
            if ((6 + NumberOfContextID + 2) < length) and (line[6+NumberOfContextID +2] != '') :
                logObj.mnc = int(line[6+NumberOfContextID+2])
        return 1    
    else:
        return 0
#     except:
#         return 0          

