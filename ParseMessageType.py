#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def ParseMessageType(type):
    switcher = { 
        "1": "SMS",
        "2": "MMS",
        "3": "CDMA SMS",
        "4": "USSD",
        "5": "Kodiak IPA",
        "6": "USSD Sequence",
        "7": "IMS SMS",
    } 
    return switcher.get(type, "Unknown")

