#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import time
import glob, os
from ParseFF import ParseFF
from ParseStart import ParseStart
from ParseStop import ParseStop
from LogDTClass import LogDT
from ParseCAA import ParseCAA
from ParseCAC import ParseCAC
from ParseCAF import ParseCAF
from ParseCAD import ParseCAD
from ParseDAD import ParseDAD
from CallContextId import CallContextID
from ParseVOIPI import ParseVOIPI
from ParseDAA import ParseDAA
from ParseDAC import ParseDAC
from ParseDREQ import ParseDREQ
from ParseDCOMP import ParseDCOMP
from ParseDRATE import ParseDRATE 
from ParseRTT import ParseRTT
from ParseCELLMEAS import ParseCELLMEAS
from ParsePHRATE import ParsePHRATE
from ParseFER import ParseFER
from ParseRLT import ParseRLT
from ParseTAD import ParseTAD
from ParseCI import ParseCI
from ParseTXPC import ParseTXPC
from ParseRXPC import ParseRXPC
from ParseMEI import ParseMEI
from ParseHSSCCHI import ParseHSSCCHI
from ParseHARQI import ParseHARQI
from ParseCQI import ParseCQI
from ParseRXQ import ParseRXQ
from ParsePLAID import ParsePLAID
from ParsePLAIU import ParsePLAIU
from ParseMACERATE import ParseMACERATE
from ParseMACI import ParseMACI
from ParseEDCHI import ParseEDCHI
from ParseSTARTSCAN import ParseSTARTSCAN
from ParseSTOPSCAN import ParseSTOPSCAN
from ParseHOA import ParseHOA
from ParseHOS import ParseHOS
from ParseHOF import ParseHOF
from ParseHOI import ParseHOI
from ParseCREL import ParseCREL
from ParseSHO import ParseSHO
from ParseLUA import ParseLUA
from ParseLUS import ParseLUS
from ParseLUF import ParseLUF
from ParseCHI import ParseCHI
from ParseGPS import ParseGPS
from ParseSEI import ParseSEI
from ParseROAM import ParseROAM
from ParseDCHI import ParseDCHI
from ParseHOP import ParseHOP
from ParseRUA import ParseRUA
from ParseRUS import ParseRUS
from ParseRUF import ParseRUF
from ParseTUA import ParseTUA
from ParseCELLINFO import ParseCELLINFO
from ParseNLIST import ParseNLIST
from ParseNMISS import ParseNMISS
from ParseANRI import ParseANRI
from ParseCELLPOLLUTION import ParseCELLPOLLUTION
from ParseRBI import ParseRBI
from ParseTRCHI import ParseTRCHI
from ParseRRA import ParseRRA
from ParseRRC import ParseRRC
from ParseRRF import ParseRRF
from ParseRRD import ParseRRD
from ParseRRRE import ParseRRRE
from ParseRRCSM import ParseRRCSM
from ParsePBA import ParsePBA
from ParsePBC import ParsePBC
from ParsePBF import ParsePBF
from ParsePBD import ParsePBD
from ParseL3SM import ParseL3SM
from ParsePCHI import ParsePCHI
from ParseGAA import ParseGAA
from ParseGAC import ParseGAC
from ParseGAF import ParseGAF
from ParseGAD import ParseGAD
from ParseRLCBLER import ParseRLCBLER
from ParseRLCRATE import ParseRLCRATE
from ParseLLCRATE import ParseLLCRATE
from ParseRUA import ParseRUA
from ParseTUS import ParseTUS
from ParseTUF import ParseTUF
from ParseMACRATE import ParseMACRATE
from ParseMACRATEU import ParseMACRATEU
from ParseMACBLER import ParseMACBLER
from ParseAMRI import ParseAMRI
from ParseAMRS import ParseAMRS
from ParseAQUL import ParseAQUL
from ParseAQDL import ParseAQDL
from ParseAQI import ParseAQI
from ParseMSGA import ParseMSGA
from ParseMSGS import ParseMSGS
from ParseMSGF import ParseMSGF
from ParsePAUSE import ParsePAUSE
from ParseRESUME import ParseRESUME
from ParseLOCK import ParseLOCK
from ParsePILOTSCAN import ParsePILOTSCAN
from ParsePAA import ParsePAA
from ParsePAC import ParsePAC
from ParsePAF import ParsePAF
from ParsePAD import ParsePAD
from ParseCARE import ParseCARE
from ParseRABA import ParseRABA
from ParseRABC import ParseRABC
from ParseRABF import ParseRABF
from ParseRABD import ParseRABD
from ParseDAF import ParseDAF
from ParseDCONTENT import ParseDCONTENT
from ParseRLCRATEU import ParseRLCRATEU
from ParsePDCPRATED import ParsePDCPRATED
from ParsePDCPRATEDU import ParsePDCPRATEDU
from ParseDCONTENTV27 import ParseDCONTENTV27
from ParsePLAIUV27 import ParsePLAIUV27
from ParseMACERATEV27 import ParseMACERATEV27
from ParseGAFV27 import ParseGAFV27
from ParseGADV27 import ParseGADV27


# In[2]:


#Global variables.......
version = ""
startDate = ""
stopDate = ""
PREVIOUS_LAT = ""
PREVIOUS_LONG = ""
PREVIOUS_MNC = ""
PREVIOUS_MCC = ""
PREVIOUS_APPLICATION_TYPE = ''
LOGDT_LIST = []
CALL_INFO_DICTIONARY = {}
DATA_INFO_DICTIONARY = {}
SCAN_INFO_DICT = {}
RADIO_RESOURCE_INFO_DICT = {}
ATTACHMENT_EVENT_INFO_DICT = {}
PACKET_SESSION_INFO_DICT = {}


# In[3]:


def main(fileName):
    global PREVIOUS_LAT
    global PREVIOUS_LONG
    global PREVIOUS_MNC
    global PREVIOUS_MCC
    global PREVIOUS_APPLICATION_TYPE
    global LOGDT_LIST
    global CALL_INFO_DICTIONARY
    global DATA_INFO_DICTIONARY
    global SCAN_INFO_DICT
    global RADIO_RESOURCE_INFO_DICT
    global ATTACHMENT_EVENT_INFO_DICT 
    global PACKET_SESSION_INFO_DICT 
    
    

    with open(fileName, 'r') as reader:
        fileContent = reader.read()

    lines = fileContent.split('\n')    
    colInLines=[]
    
    fileNameCsv = fileName[:-4]
    fileNameCsv += ".csv"
    
    G = LogDT()
    
    file_object = open(fileNameCsv, 'w')
    csv_file_writer = csv.writer(file_object)
    csv_file_writer.writerow(list(vars(G).keys()))

    for i in range (0,len(lines)):
        colInLines.append (lines[i].split(','))

    for i in range (0,len(colInLines)):
        status = 0
        LOGDT_LIST = []
        listAppended = 0
        if colInLines[i][0] == '#FF':
            global version
            version = ParseFF(colInLines[i])
        elif colInLines[i][0] == '#START':
            global startDate
            startDate = ParseStart(colInLines[i]) 
        elif colInLines[i][0] == '#STOP':
            global stopDate
            stopDate = ParseStop(colInLines[i]) 
        elif colInLines[i][0] == 'CAA':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseCAA(colInLines[i],logDTObj,CALL_INFO_DICTIONARY)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'CAC':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseCAC(colInLines[i],logDTObj,CALL_INFO_DICTIONARY)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'CAF':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseCAF(colInLines[i],logDTObj,CALL_INFO_DICTIONARY)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'CAD':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseCAD(colInLines[i],logDTObj,CALL_INFO_DICTIONARY)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'VOIPI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseVOIPI(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'CARE':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseCARE(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'CALLMODI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseCALLMODI(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'DAA':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseDAA(colInLines[i],logDTObj,DATA_INFO_DICTIONARY)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'DAC':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseDAC(colInLines[i],logDTObj,DATA_INFO_DICTIONARY)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'DAF':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseDAF(colInLines[i],logDTObj,DATA_INFO_DICTIONARY)
            PREVIOUS_APPLICATION_TYPE=''
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'DAD':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseDAD(colInLines[i],logDTObj,DATA_INFO_DICTIONARY)
            PREVIOUS_APPLICATION_TYPE=''
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'DREQ':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseDREQ(colInLines[i],logDTObj,DATA_INFO_DICTIONARY)
            PREVIOUS_APPLICATION_TYPE=logDTObj.applicationProtocol
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'DCOMP':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseDCOMP(colInLines[i],logDTObj,DATA_INFO_DICTIONARY)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'DRATE':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseDRATE(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'PER':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParsePER(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RTT':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseRTT(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'JITTER':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseJITTER(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'DSS':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseDSS(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'DCONTENT':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            if version == '2.27':
                status = ParseDCONTENTV27(colInLines[i],logDTObj)
            else:
                status = ParseDCONTENT(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'DTRACE':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseDTRACE(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'TCPSTAT':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseTCPSTAT(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'CELLMEAS':    
            status = ParseCELLMEAS(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
                   
        elif colInLines[i][0] == 'MIMOMEAS':
            listOfLogObj = []
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status, listOfLogObj = ParseMIMOMEAS(colInLines[i],listOfLogObj)
            if status == 1:
                for i in range(0,len(listOfLogObj)):
                    LOGDT_LIST.append(listOfLogObj[i])
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'FER':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseFER(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RLT':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseRLT(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'TAD':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseTAD(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'CI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseCI(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'TXPC':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseTXPC(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RXPC':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseRXPC(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'BER':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseBER(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'PHRATE':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParsePHRATE(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'PPPRATE':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParsePPPRATE(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'MEI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseMEI(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'POSI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParsePOSI(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'CQI':
            status = ParseCQI(colInLines[i],LOGDT_LIST,PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'HARQI':
            status = ParseHARQI(colInLines[i],LOGDT_LIST,PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'HSSCCHI':
            status = ParseHSSCCHI(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'PLAID':
            status = ParsePLAID(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'PLAIU':
            if version == '2.27':
                status = ParsePLAIUV27(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            else:
                status = ParsePLAIU(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)      
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'MACERATE':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            if version == '2.27':
                status = ParseMACERATEV27(colInLines[i],logDTObj)
            else:
                status = ParseMACERATE(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'MACI':
            status = ParseMACI(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'EDCHI':
            status = ParseEDCHI(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'STARTSCAN':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseSTARTSCAN(colInLines[i],logDTObj,SCAN_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'STOPSCAN':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseSTOPSCAN(colInLines[i],logDTObj,SCAN_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'FREQSCAN':
            status = ParseFREQSCAN(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'SPECTRUMSCAN':
            status = ParseSPECTRUMSCAN(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'HOA':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseHOA(colInLines[i],logDTObj,SCAN_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'HOS':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseHOS(colInLines[i],logDTObj,SCAN_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'HOI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseHOI(colInLines[i],logDTObj,SCAN_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'CREL':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseCREL(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'SHO':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseSHO(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'LUA':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseLUA(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'LUS':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mnc = PREVIOUS_MNC
            logDTObj.mcc = PREVIOUS_MCC
            status = ParseLUS(colInLines[i],logDTObj)
            PREVIOUS_MCC = logDTObj.mcc
            PREVIOUS_MNC = logDTObj.mnc
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'LUF':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mnc = PREVIOUS_MNC
            logDTObj.mcc = PREVIOUS_MCC
            status = ParseLUF(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'CHI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mnc = PREVIOUS_MNC
            logDTObj.mcc = PREVIOUS_MCC
            status = ParseCHI(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'GPS':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mnc = PREVIOUS_MNC
            logDTObj.mcc = PREVIOUS_MCC
            status = ParseGPS(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'VCHI':
            ParseVCHI(colInLines[i])
        elif colInLines[i][0] == 'HOF':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseHOF(colInLines[i],logDTObj,SCAN_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'SEI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseSEI(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'ROAM':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseROAM(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)          
        elif colInLines[i][0] == 'DCHI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseDCHI(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'HOP':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseHOP(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'CELLINFO':
            status = ParseCELLINFO(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'NLIST':
            status = ParseNLIST(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'NMISS':
            status = ParseNMISS(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'ANRI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mnc = PREVIOUS_MNC
            logDTObj.mcc = PREVIOUS_MCC
            status = ParseANRI(colInLines[i],logDTObj)
            PREVIOUS_MCC = logDTObj.mcc
            PREVIOUS_MNC = logDTObj.mnc
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'CELLPOLLUTION':
            status = ParseCELLPOLLUTION(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'RBI':
            status = ParseRBI(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'TRCHI':
            status = ParseTRCHI(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'RRA':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC           
            status = ParseRRA(colInLines[i],logDTObj,RADIO_RESOURCE_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RRC':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC           
            status = ParseRRC(colInLines[i],logDTObj,RADIO_RESOURCE_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RRF':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC           
            status = ParseRRF(colInLines[i],logDTObj,RADIO_RESOURCE_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RRD':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParseRRD(colInLines[i],logDTObj,RADIO_RESOURCE_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RRRE':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParseRRRE(colInLines[i],logDTObj,RADIO_RESOURCE_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'PBA':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParsePBA(colInLines[i],logDTObj,RADIO_RESOURCE_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'PBC':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParsePBC(colInLines[i],logDTObj,RADIO_RESOURCE_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'PBF':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParsePBF(colInLines[i],logDTObj,RADIO_RESOURCE_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'PBD':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParsePBD(colInLines[i],logDTObj,RADIO_RESOURCE_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'L3SM':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseL3SM(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'PCHI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParsePCHI(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'GAA':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParseGAA(colInLines[i],logDTObj,ATTACHMENT_EVENT_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'GAF':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            if version == '2.27':
                status = ParseGAFV27(colInLines[i],logDTObj,ATTACHMENT_EVENT_INFO_DICT)
            else:
                status = ParseGAF(colInLines[i],logDTObj,ATTACHMENT_EVENT_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'GAC':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParseGAC(colInLines[i],logDTObj,ATTACHMENT_EVENT_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'GAD':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            if version == '2.27':
                status = ParseGADV27(colInLines[i],logDTObj,ATTACHMENT_EVENT_INFO_DICT)
            else:
                status = ParseGAD(colInLines[i],logDTObj,ATTACHMENT_EVENT_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RLCBLER':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParseRLCBLER(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RLCRATE':
            status = ParseRLCRATE(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'RLCRATEU':
            status = ParseRLCRATEU(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'PDCPRATED':
            status = ParsePDCPRATED(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'PDCPRATEU':
            status = ParsePDCPRATEDU(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'LLCRATE':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseLLCRATE(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RUA':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseRUA(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RUS':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseRUS(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RUF':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseRUF(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'TUA':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseTUA(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'TUS':
            status = ParseTUS(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'TUF':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseTUF(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'MACRATE':
            status = ParseMACRATE(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'MACRATEU':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseMACRATEU(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'MACBLER':
            status = ParseMACBLER(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'AMRI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseAMRI(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'AMRS':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseAMRS(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'AQUL':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseAQUL(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'AQDL':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseAQDL(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'AQI':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseAQI(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)           
        elif colInLines[i][0] == 'MSGA':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseMSGA(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj) 
        elif colInLines[i][0] == 'MSGF':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseMSGF(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj) 
        elif colInLines[i][0] == 'RXQ':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseRXQ(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'MSGS':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseMSGS(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj) 
        elif colInLines[i][0] == 'PAUSE':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParsePAUSE(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RESUME':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseRESUME(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'LOCK':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseLOCK(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'PILOTSCAN':
            status = ParsePILOTSCAN(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'PAA':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParsePAA(colInLines[i],logDTObj,PACKET_SESSION_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj)   
        elif colInLines[i][0] == 'PAC':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParsePAC(colInLines[i],logDTObj,PACKET_SESSION_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj) 
        elif colInLines[i][0] == 'PAF':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParsePAF(colInLines[i],logDTObj,PACKET_SESSION_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj) 
        elif colInLines[i][0] == 'PAD':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC  
            status = ParsePAD(colInLines[i],logDTObj,PACKET_SESSION_INFO_DICT)
            if status == 1:
                LOGDT_LIST.append(logDTObj) 
        elif colInLines[i][0] == 'RRCSM':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseRRCSM(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RABA':
            status = ParseRABA(colInLines[i],LOGDT_LIST, PREVIOUS_LAT,PREVIOUS_LONG,PREVIOUS_MCC,PREVIOUS_MNC)
            status = 0
            listAppended = 1
        elif colInLines[i][0] == 'RABC':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseRABC(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RABF':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseRABF(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
        elif colInLines[i][0] == 'RABD':
            logDTObj = LogDT()
            logDTObj.lat = PREVIOUS_LAT
            logDTObj.longg = PREVIOUS_LONG
            logDTObj.mcc = PREVIOUS_MCC
            logDTObj.mnc = PREVIOUS_MNC
            status = ParseRABD(colInLines[i],logDTObj)
            if status == 1:
                LOGDT_LIST.append(logDTObj)
                
        if status == 1:
            csv_file_writer.writerow(list(vars(logDTObj).values()))
        if listAppended == 1:
            for i in LOGDT_LIST:
                csv_file_writer.writerow(list(vars(i).values()))
            


# In[4]:


if __name__ == '__main__':
    os.chdir('./nmfFiles')
    count = 1
    fileWrite = 0
    for file in glob.glob("*.nmf"):
        start_time = time.time()
        
        size = os.path.getsize(file)
        print(file + ", " + str(size/1024) + ' KB, '+ str(count))
        main(file)

        count += 1
        
        CALL_INFO_DICTIONARY = {}
        DATA_INFO_DICTIONARY = {}
        SCAN_INFO_DICT = {}
        RADIO_RESOURCE_INFO_DICT = {}
        ATTACHMENT_EVENT_INFO_DICT = {}
        PACKET_SESSION_INFO_DICT = {}
        LOGDT_LIST = []
        print(str(time.time() - start_time) + " seconds\n")
        
        

