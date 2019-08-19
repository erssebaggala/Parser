#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def ParseAMRCodec(type):
    switcher = { 
        0: "NB 4.75",
        1: "NB 5.15",
        2: "NB 5.9",
        3: "NB 6.7",
        4: "NB 7.4",
        5: "NB 7.95",
        6: "NB 10.2",
        7: "NB 12.2",
        100: "WB 6.6",
        101: "WB 8.85",
        102: "WB 12.65",
        103: "WB 14.25",
        104: "WB 15.85",
        105: "WB 18.25",
        106: "WB 19.85",
        107: "WB 23.05",
        108: "WB 23.85",
    } 
    return switcher.get(type, "Unknown")

