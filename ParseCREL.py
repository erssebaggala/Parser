#!/usr/bin/env python
# coding: utf-8

# In[1]:


from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from HOEventInfo import HOEventInfo
from ParseCellMeasuresParseBand import parseCellMeasuresParseBand
from ParseHOAHandoverType import parseHOAHandoverType


# In[2]:


def ParseCREL (line, logObj):
    length = len(line)
    if 2 < length:
        dataOfCREL = ''
        mainHeaderCount = 0
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
            if NumberOfContextID != 0:
                if((3+NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
                    mainHeaderCount = int(line[3+NumberOfContextID])

        logObj.event = "Cell Reselection"
        logObj.msgType = 'Cell Information'
        
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            mainHeaderCount = int(line[3 + NumberOfContextID])
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') and mainHeaderCount > 0:
            crsTime = line[4+NumberOfContextID]  
            dataOfCREL += ("CRS Time: " + crsTime + 'ms;')
            
        crsReason = "Unknown"  
        if ((5 + NumberOfContextID) < length) and (line[5 + NumberOfContextID] != '') and mainHeaderCount > 1 :
            crsReason = line[5 + NumberOfContextID + mainHeaderCount]
            if crsReason == '1001':
                crsReason = 'iDEN comparison between serving cell and neighbor cell quality'
            elif crsReason == '1002':
                crsReason = 'iDEN serving cell becomes barred'
            elif crsReason == '1003':
                crsReason = 'iDEN serving cell failed'
        dataOfCREL += 'CRS Reason: '+crsReason
        
        if ((4 + NumberOfContextID + mainHeaderCount) < length) and (line[4 + NumberOfContextID + mainHeaderCount] != ''):
            oldSystem = MeasureSysConverter(int(line[4 + NumberOfContextID + mainHeaderCount]))
            logObj.OldSystem = oldSystem
            
        oldSystemParameterCount = 0    
        if ((5 + NumberOfContextID + mainHeaderCount) < length) and (line[5 + NumberOfContextID + mainHeaderCount] != ''):
            oldSystemParameterCount = int(line[5 + NumberOfContextID + mainHeaderCount])
            
            
        if oldSystem == 'GSM' or oldSystem == 'UMTS FDD':
            for parameter in range(1,oldSystemParameterCount):
                itemNumber = 6 + NumberOfContextID + mainHeaderCount
                if parameter == 1:#Old LAC
                    if ((itemNumber + parameter) < length) and (line[itemNumber + parameter] != '') :
                        logObj.OldLAC = int(line[itemNumber + parameter])
                elif parameter == 2:#Old Cell ID
                    if ((itemNumber + parameter) < length) and (line[itemNumber + parameter] != '') :
                        logObj.OldCellID = int(line[itemNumber + parameter])
                elif parameter == 3:#Old Band
                    if ((itemNumber + parameter) < length) and (line[itemNumber + parameter] != '') :
                        logObj.OldBand = parseCellMeasuresParseBand(int(line[itemNumber + parameter]))
            dataOfCREL += ';Old System: '+oldSystem + "( LAC: "+str(logObj.OldLAC)+";Cell ID: "+str(logObj.OldCellID) +'Old Band: '+ str(logObj.OldBand) +')'
                        
        elif oldSystem == 'LTE FDD' or oldSystem == 'LTE TDD':
            for parameter in range(1,oldSystemParameterCount):
                itemNumber = 6 + NumberOfContextID + mainHeaderCount
                if parameter == 1:#Old TAC
                    if ((itemNumber + parameter) < length) and (line[itemNumber + parameter] != '') :
                        logObj.OldTAC = int(line[itemNumber + parameter])
                elif parameter == 2:#Old Cell ID
                    if ((itemNumber + parameter) < length) and (line[itemNumber + parameter] != '') :
                        logObj.OldCellID = int(line[itemNumber + parameter])
                elif parameter == 3:#Old Band
                    if ((itemNumber + parameter) < length) and (line[itemNumber + parameter] != '') :
                        logObj.OldBand = parseCellMeasuresParseBand(int(line[itemNumber + parameter]))
            dataOfCREL += ';Old System: '+oldSystem + "( TAC: "+str(logObj.OldTAC)+";Cell ID: "+ str(logObj.OldCellID) +'Old Band: '+ str(logObj.OldBand) +')'
           
        
        
        currentSystem = 'Unknown'
        if ((4 + NumberOfContextID + mainHeaderCount) < length) and (line[4 + NumberOfContextID + mainHeaderCount] != ''):
            currentSystem = MeasureSysConverter(int(line[4 + NumberOfContextID + mainHeaderCount]))
            logObj.AttemptedSystem = currentSystem
            
        newSystemParameterCount = 0    
        if ((5 + NumberOfContextID + mainHeaderCount) < length) and (line[5 + NumberOfContextID + mainHeaderCount] != ''):
            newSystemParameterCount = int(line[5 + NumberOfContextID + mainHeaderCount])
            
        if currentSystem == 'GSM' or currentSystem == 'UMTS FDD':
            for parameter in range(1,newSystemParameterCount):
                itemNumber = 6 + NumberOfContextID + mainHeaderCount
                if parameter == 1:#LAC
                    if ((itemNumber + parameter) < length) and (line[itemNumber + parameter] != '') :
                        logObj.LAC = int(line[itemNumber + parameter])
                elif parameter == 2:#Cell ID
                    if ((itemNumber + parameter) < length) and (line[itemNumber + parameter] != '') :
                        logObj.CellId = int(line[itemNumber + parameter])
                elif parameter == 3:#Band
                    if ((itemNumber + parameter) < length) and (line[itemNumber + parameter] != '') :
                        logObj.Band = parseCellMeasuresParseBand(int(line[itemNumber + parameter]))
            dataOfCREL += ';New System: '+currentSystem + "( LAC: "+str(logObj.LAC)+";Cell ID: "+str(logObj.CellId) +'Band: '+ str(logObj.Band) +')'
                        
        elif currentSystem == 'LTE FDD' or currentSystem == 'LTE TDD':
            for parameter in range(1,oldSystemParameterCount):
                itemNumber = 6 + NumberOfContextID + mainHeaderCount
                if parameter == 1:#TAC
                    if ((itemNumber + parameter) < length) and (line[itemNumber + parameter] != '') :
                        logObj.TAC = int(line[itemNumber + parameter])
                elif parameter == 2:#Cell ID
                    if ((itemNumber + parameter) < length) and (line[itemNumber + parameter] != '') :
                        logObj.CellId = int(line[itemNumber + parameter])
                elif parameter == 3:#Band
                    if ((itemNumber + parameter) < length) and (line[itemNumber + parameter] != '') :
                        logObj.Band = parseCellMeasuresParseBand(int(line[itemNumber + parameter]))
            dataOfCREL += ';New System: '+currentSystem + "( TAC: "+str(logObj.TAC)+";Cell ID: "+str(logObj.CellId) +'Band: '+ str(logObj.Band) +')'
                                       
        logObj.eventInfo = dataOfCREL
                                                 
        return 1


# In[ ]:




