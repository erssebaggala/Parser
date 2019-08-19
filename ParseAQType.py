#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def ParseAQType(type):
    switcher = { 
        1: "EMOS",
        2: "PESQ NB",
        3: "3SQM",
        4: "Streaming Quality",
        5: "NiQA-DSP-LQ",
        6: "PESQ WB",
        7: "POLQA NB",
        8: "POLQA SWB",
    } 
    return switcher.get(type, "Unknown")


# In[ ]:




