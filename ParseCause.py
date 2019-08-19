#!/usr/bin/env python
# coding: utf-8

# In[2]:


def parseRRAUMTSFDD(type):
    switcher = { 
        0: "Originating conversation call",
        1: "Originating streaming call",
        2: "Originating longeractive call",
        3: "Originating background call",
        4: "Originating subscribed traffic call",
        5: "Terminating conversational call",
        6: "Terminating streaming call",
        7: "Terminating longeractive call",
        8: "Terminating background call",
        9: "Emergency call",
        10: "Inter-RAT cell reselection",
        11: "Inter-RAT cell change order",
        12: "Registration",
        13: "Detach",
        14: "Originating high priority signaling",
        15: "Originating low priority signaling",
        16: "Call re-establishment",
        17: "Terminating high priority signaling",
        18: "Terminating low priority signaling",
        19: "Terminating - cause unknown",
    } 
    return switcher.get(type, "Unknown")

