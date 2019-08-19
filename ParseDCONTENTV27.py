#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from LogDTClass import LogDT
from ParseApplicationProtocol import ParseApplicationProtocol
def ParseDCONTENTV27 (line, logObj):
    length = len(line)
    if 2 < length:
        applicationProtocol = "Unknown"
        NumberOfContextID = 0
        if line[2] != '':
            NumberOfContextID = int(line[2])
        logObj.event = "Data Content"
        logObj.msgType = ''
        logObj.time = line[1]
        if ((3 + NumberOfContextID) < length) and (line[3+NumberOfContextID] != '') :
            logObj.applicationProtocol = ParseApplicationProtocol(int(line[3 + NumberOfContextID]))
        return 1
    else:
        return 0
#     except:
#         return 0

