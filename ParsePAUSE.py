#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from LogDTClass import LogDT
def ParsePAUSE (line, logObj):
    logObj.event = "Filemark"
    logObj.msgType = "Old Filemark"
    logObj.eventInfo = "Recording Paused"
    return 1    

