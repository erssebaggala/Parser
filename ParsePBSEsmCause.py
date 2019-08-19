#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def parsePBSEsmCause(type):
    switcher = { 
        8: "Operator determined barring",
        24: "MBMS bearer capabilities insufficient for the service",
        25: "LLC or SNDCP failure (A/Gb mode only)",
        26: "Insufficient resources",
        27: "Missing or unknown APN",
        28: "Unknown PDP address or PDP type",
        29: "User authentication failed",
        30: "Activation rejected by GGSN, serving GW, or PDN GW",
        31: "Activation rejected, unspecified",
        32: "Service option not supported",
        33: "Requested service option not subscribed",
        34: "Service option temporarily out of order",
        35: "NSAPI/PTI already used",
        36: "Regular deactivation",
        37: "QoS not accepted",
        38: "Network failure",
        39: "Reactivation requested",
        40: "Feature not supported",
        41: "Semantic error in the TFT operation",
        42: "Syntactical error in the TFT operation",
        43: "Unknown PDP context or bearer identity",
        44: "Semantic errors in packet filter(s)",
        45: "Syntactical errors in packet filter(s)",
        46: "PDP context without TFT already activated",
        47: "Multicast group membership time-out or PTI mismatch",
        49: "Last PDN disconnection not allowed",
        50: "PDN type IPv4 only allowed",
        51: "PDN type IPv6 only allowed",
        52: "Single address bearers only allowed",
        53: "ESM information not received",
        54: "PDN connection does not exist",
        55: "Multiple PDN connections for a given APN not allowed",
        56: "Collision with network initiated request",
        59: "Unsupported QCI value",
        81: "Invalid transaction identifier or PTI value",
        95: "Semantically incorrect message",
        96: "Invalid mandatory information",
        97: "Message type non-existent or not implemented",
        98: "Message not compatible with protocol state.",
        99: "Information element non-existent or not implemented",
        100: "Conditional IE error",
        101: "Message not compatible with protocol state",
        111: "Protocol error, unspecified",
        112: "APN restriction value incompatible with active PDP context",
    } 
    return switcher.get(type, "Unknown")

