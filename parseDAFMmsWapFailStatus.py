#!/usr/bin/env python
# coding: utf-8

# In[1]:


def parseDAFMmsWapFailStatus(type):
    switcher = { 
        1: "Timeout",
        2: "Invalid remote address",
        4: "Invalid remote file",
        5: "Invalid local file",
        50: "Unknown Only used with the MMS protocol.",
        51: "Protocol error Only used with the MMS protocol.",
        52: "Invalid TID Only used with the MMS protocol.",
        53: "Not implemented class 2 Only used with the MMS protocol.",
        54: "Not implemented SAR Only used with the MMS protocol.",
        55: "Not implemented user acknowledgement Only used with the MMS protocol.",
        56: "WTP version zero Only used with the MMS protocol.",
        57: "Capacity temporarily exceeded Only used with the MMS protocol.",
        58: "No response Only used with the MMS protocol.",
        59: "Message too large Only used with the MMS protocol.",
        100: "Continue",
        101: "Switching Protocols",
        129: "Unspecified Only used with the MMS protocol.",
        130: "Service denied Only used with the MMS protocol.",
        131: "Message format corrupt Only used with the MMS protocol.",
        132: "Sending address unresolved Only used with the MMS protocol.",
        133: "Message not found Only used with the MMS protocol.",
        134: "Network problem Only used with the MMS protocol.",
        135: "Content not accepted Only used with the MMS protocol.",
        136: "Unsupported message Only used with the MMS protocol.",
        200: "OK, success",
        201: "Created",
        202: "Accepted",
        203: "NonAuthoritative information",
        204: "No content",
        205: "Reset content",
        206: "Partial content",
        300: "Multiple choices",
        301: "Moved permanently",
        302: "Moved temporarily",
        303: "See other",
        304: "Not modified",
        305: "Use proxy",
        306: "Reserved",
        307: "Temporary redirect",
        400: "Bad request server could not understand request",
        401: "Unauthorized",
        402: "Payment required",
        403: "Forbidden operation is understood but refused",
        404: "Not found",
        405: "Method not allowed",
        406: "Not acceptable",
        407: "Proxy authentication required",
        408: "Request timeout",
        409: "Conflict",
        410: "Gone",
        411: "Length required",
        412: "Precondition failed",
        413: "Request entity too large",
        414: "RequestURI too large",
        415: "Unsupported media type",
        416: "Requested range not satisfiable",
        417: "Expectation failed",
        500: "Internal server error",
        501: "Not implemented",
        502: "Bad gateway",
        503: "Service unavailable",
        504: "Gateway timeout",
        505: "HTTP version not supported",
    } 
    return switcher.get(type, "Unknown")


# In[ ]:




