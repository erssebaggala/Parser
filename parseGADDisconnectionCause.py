#!/usr/bin/env python
# coding: utf-8

# In[2]:


def parseGADDisconnectionCause(type):
    switcher = { 
        2: "IMSI unknown in HLR/HSS",
        3: "Illegal MS",
        5: "IMEI not accepted",
        6: "Illegal ME",
        7: "GPRS/EPS services not allowed",
        8: "GPRS/EPS services and non-GPRS/non-EPS services not allowed",
        9: "MS identity cannot be derived by the network",
        10: "Implicitly detached",
        11: "PLMN not allowed",
        12: "Location/tracking area not allowed",
        13: "Roaming not allowed in this location area",
        14: "GPRS/EPS services not allowed in this PLMN",
        15: "No suitable cells in location/tracking area",
        16: "MSC temporarily not reachable",
        17: "Network failure",
        18: "CS domain not available LTE only.",
        19: "ESM failure LTE only.",
        20: "MAC failure",
        21: "Synch failure",
        22: "Congestion",
        23: "MS security capabilities mismatch",
        24: "Security mode rejected, unspecified",
        25: "Not authorized for this CSG LTE only.",
        26: "Non-EPS authentication unacceptable LTE only.",
        39: "CS domain temporarily not available LTE only.",
        40: "No PDP/EPS bearer context activated",
        95: "Semantically incorrect message",
        96: "Invalid mandatory information",
        97: "Message type non-existent or not implemented",
        98: "Message type not compatible with the protocol state",
        99: "Information element non-existent or not implemented",
        100: "Conditional IE error",
        101: "Message not compatible with the protocol state",
        111: "Protocol error, unspecified",
    } 
    return switcher.get(type, "Unknown")


# In[ ]:




