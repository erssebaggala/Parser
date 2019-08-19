#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def parseSMSFailureCause(type):
    switcher = { 
        1: "Unassigned (unallocated) number",
        8: "Operator determined barring",
        10: "Call barred",
        21: "Short message transfer rejected",
        27: "Destination out of service",
        28: "Unidentified subscriber",
        29: "Facility rejected",
        30: "Unknown subscriber",
        38: "Network out of order",
        41: "Temporary failure",
        42: "Congestion",
        47: "Resources unavailable, unspecified",
        50: "Requested facility not subscribed",
        69: "Requested facility not implemented",
        81: "Invalid short message transfer referencevalue",
        95: "Invalid message, unspecified",
        96: "Invalid mandatory information",
        97: "Message type non-existent or not implemented",
        98: "Message not compatible with short message protocol state",
        99: "Information element non-existent or notimplemented",
        111: "Protocol error, unspecified",
        127: "Interworking, unspecified",
        128: "Telematic longerworking not supported",
        129: "Short message Type 0 not supported",
        130: "Cannot replace short message",
        143: "Unspecified TP-PID error",
        144: "Data coding scheme (alphabet) not supported",
        145: "Message class not supported",
        159: "Unspecified TP-DCS error",
        160: "Command cannot be actioned",
        161: "Command unsupported",
        175: "Unspecified TP-Command error",
        176: "TPDU not supported",
        192: "SC busy",
        193: "No SC subscription",
        194: "SC system failure",
        195: "Invalid SME address",
        196: "Destination SME barred",
        197: "SM Rejected-Duplicate SM",
        198: "TP-VPF not supported",
        199: "TP-VP not supported",
        208: "SIM SMS storage full",
        209: "No SMS storage capability in SIM",
        210: "Error in MS",
        211: "Memory Capacity Exceeded",
        212: "SIM Application Toolkit Busy",
        255: "Unspecified error cause",
        300: "ME failure",
        301: "SMS service of ME reserved",
        302: "Operation not allowed",
        303: "Operation not supported",
        304: "Invalid PDU mode parameter",
        305: "Invalid text mode parameter",
        310: "SIM not inserted",
        311: "SIM PIN required",
        312: "PH-SIM PIN required",
        313: "SIM failure",
        314: "SIM busy",
        315: "SIM wrong",
        316: "SIM PUK required",
        317: "SIM PIN2 required",
        318: "SIM PUK2 required",
        320: "Memory failure",
        321: "invalid memory index",
        322: "memory full",
        330: "SMSC address unknown",
        331: "no network service",
        332: "network timeout",
        340: "No +CNMA acknowledgement expected",
        500: "Unknown error",
        512: "Manufacturer specific",
    } 
    return switcher.get(type, "Unknown")

