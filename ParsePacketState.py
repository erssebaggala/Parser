#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def parsePacketState(type):
    switcher = { 
        0: "No GPRS Available",
        1: "Detached",
        2: "Attached",
        3: "Standby",
        4: "Packet session active",
        5: "Suspended",
    } 
    return switcher.get(type, "Unknown")

