#!/usr/bin/env python
# coding: utf-8

# In[2]:
from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
from ParseCellMeasuresParseBand import parseCellMeasuresParseBand
from ParseGpsQuality import parseGpsQuality

def ParseGPS (line, logObj):
    dataOfGPS = ""
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        callContextID = 0
        status = 'Unknown'
        quality = 'Unknown'
        logObj.event = "GPS Position Valid"
        logObj.msgType = 'Position, velocity and time packet'
        logObj.time = line[1] 
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.longg = float(line[3 + NumberOfContextID])
        if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
            logObj.lat = float(line[4 + NumberOfContextID])
        if ((5 + NumberOfContextID) < length) and (line[5+NumberOfContextID] != '') :
            dataOfGPS = 'Height: ' + line[5+NumberOfContextID] + ';'
        if ((6 + NumberOfContextID) < length) and (line[6+NumberOfContextID] != '') :
            dataOfGPS += 'Distance: ' + line[6+NumberOfContextID] + ';'
        if ((7 + NumberOfContextID) < length) and (line[7+NumberOfContextID] != '') :
            quality = parseGpsQuality(line[7+NumberOfContextID])
            dataOfGPS += 'Quality: ' + quality + ';'
        if ((8 + NumberOfContextID) < length) and (line[8+NumberOfContextID] != '') :
            dataOfGPS += 'Satellites Count: ' + line[8+NumberOfContextID] + ';'
        if ((9 + NumberOfContextID) < length) and (line[9+NumberOfContextID] != '') :
            dataOfGPS += 'Velocity: ' + line[9+NumberOfContextID] + ';'
        if ((10 + NumberOfContextID) < length) and (line[10+NumberOfContextID] != '') :
            dataOfGPS += 'PDOP: ' + line[10+NumberOfContextID] + ';'
        if ((11 + NumberOfContextID) < length) and (line[11+NumberOfContextID] != '') :
            dataOfGPS += 'HDOP: ' + line[11+NumberOfContextID] + ';'
        if ((12 + NumberOfContextID) < length) and (line[12+NumberOfContextID] != '') :
            dataOfGPS += 'VDOP: ' + line[12+NumberOfContextID] + ';'
        if ((13 + NumberOfContextID) < length) and (line[13+NumberOfContextID] != '') :
            if line[13+NumberOfContextID] == '0':
                status = 'No fix'
            elif line[13+NumberOfContextID] == '1':
                status = 'Fix'
            elif line[13+NumberOfContextID] == '2':
                status = 'Time drift'
            elif line[13+NumberOfContextID] == '3':
                status = 'Stale position'
            dataOfGPS += 'Status: ' + status
        logObj.eventInfo = dataOfGPS 
        return 1
    
    else:
        dataOfGPS = "No of context id not found"
        return 0
#     except:
#         return 0


# In[ ]:




