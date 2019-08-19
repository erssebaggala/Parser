#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from LogDTClass import LogDT
from MeasureSysConverter import MeasureSysConverter
def ParseMACERATEV27 (line, logObj):
    length = len(line)
    if 2 < length:
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        logObj.event = "MAC-E layer throughput"
        logObj.msgType = ''
        logObj.time = line[1]
        measureSystems=''
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            measureSystems = int(line[3 + NumberOfContextID])
            logObj.modeSystem = MeasureSysConverter(measureSystems)
            
        if logObj.modeSystem == 'UMTS FDD':
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                logObj.MACEBitRate = int(line[4+NumberOfContextID])
            
            if ((4 + NumberOfContextID) < length) and (line[4+NumberOfContextID] != '') :
                celltype = line[9+NumberOfContextID]
                
                if celltype == '1':
                    logObj.cellType = "Primary"
                elif celltype == '2':
                    logObj.cellType = "Secondary"
                
                
        return 1
    else:
        return 0
#     except:
#         return 0

