#!/usr/bin/env python
# coding: utf-8

# In[21]:
#Measure sstem LUT

def MeasureSysConverter (measureSystem):
    if measureSystem == 1:
        measureSystem = "GSM"
    elif measureSystem == 2:
        measureSystem = "TETRA"
    elif measureSystem == 5:
        measureSystem = "UMTS FDD"
    elif measureSystem == 6:
        measureSystem = "UMTS TD-SCDMA"
    elif measureSystem == 7:
        measureSystem = "LTE FDD"
    elif measureSystem == 8:
        measureSystem = "LTE TDD"
    elif measureSystem == 10:
        measureSystem = "cdmaOne"
    elif measureSystem == 11:
        measureSystem = "CDMA 1x"
    elif measureSystem == 12:
        measureSystem = "EVDO"
    elif measureSystem == 20:
        measureSystem = "WLAN"
    elif measureSystem == 21:
        measureSystem = "GAN WLAN"
    elif measureSystem == 25: 
        measureSystem = "WiMAX"
    elif measureSystem == 50:
        measureSystem = "NMT"
    elif measureSystem == 51:
        measureSystem = "AMPS"
    elif measureSystem == 52:
        measureSystem = "NAMPS"
    elif measureSystem == 53:
        measureSystem = "DAMPS"
    elif measureSystem == 54:
        measureSystem = "ETACS"
    elif measureSystem == 55:
        measureSystem = "iDEN"
    elif measureSystem == 60:
        measureSystem = "PSTN"
    elif measureSystem == 61:
        measureSystem = "ISDN"
    elif measureSystem == 65:
        measureSystem = "DVBH"
    else:
        measureSystem = "Unknown"
    return measureSystem


# In[24]:


string = MeasureSysConverter('2')
string


# In[ ]:




