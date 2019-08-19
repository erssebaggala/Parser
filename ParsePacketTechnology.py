#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def parsePacketTechnology(type):
    switcher = { 
        1: "GPRS",
        2: "EGPRS",
        3: "UMTS FDD",
        5: "HSDPA",
        10: "HSPA",
        14: "LTE FDD",
        16: "LTE TDD",
        18: "DC-HSPA",
        19: "LTE CA",
        20: "DC-HSUPA",
        101: "GPRS + WLAN",
        102: "EGPRS + WLAN",
        103: "UMTS FDD + WLAN",
        105: "HSDPA + WLAN",
        110: "HSPA + WLAN",
        114: "LTE FDD + WLAN",
        116: "LTE TDD + WLAN",
        118: "DC-HSPA + WLAN",
        119: "LTE CA + WLAN",
        120: "DC-HSUPA + WLAN",
    } 
    return switcher.get(type, "Unknown")

