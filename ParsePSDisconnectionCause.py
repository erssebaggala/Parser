#!/usr/bin/env python
# coding: utf-8

# In[2]:


def ParsePSDisconnectionCause(type):
    switcher = { 
        8: "Operator determined barring ",
        24: "MBMS bearer capabilities insufficient for the service ",
        25: "LLC or SNDCP failure (A/Gb mode only) ",
        26: "Insufficient resources ",
        27: "Missing or unknown APN ",
        28: "Unknown PDP address or PDP type ",
        29: "User authentication failed ",
        30: "Activation rejected by GGSN, serving GW, or PDN GW ",
        31: "Activation rejected, unspecified ",
        32: "Service option not supported ",
        33: "Requested service option not subscribed ",
        34: "Service option temporarily out of order ",
        35: "NSAPI/PTI already used ",
        36: "Regular deactivation ",
        37: "QoS not accepted ",
        38: "Network failure ",
        39: "Reactivation requested ",
        40: "Feature not supported ",
        41: "Semantic error in the TFT operation ",
        42: "Syntactical error in the TFT operation ",
        43: "Unknown PDP context or bearer identity ",
        44: "Semantic errors in packet filter(s) ",
        45: "Syntactical errors in packet filter(s) ",
        46: "PDP context without TFT already activated ",
        47: "Multicast group membership time-out or PTI mismatch ",
        49: "Last PDN disconnection not allowed ",
        50: "PDN type IPv4 only allowed ",
        51: "PDN type IPv6 only allowed ",
        52: "Single address bearers only allowed ",
        53: "ESM information not received ",
        54: "PDN connection does not exist ",
        55: "Multiple PDN connections for a given APN not allowed ",
        56: "Collision with network initiated request ",
        59: "Unsupported QCI value ",
        81: "Invalid transaction identifier or PTI value ",
        95: "Semantically incorrect message ",
        96: "Invalid mandatory information ",
        97: "Message type non-existent or not implemented ",
        98: "Message not compatible with protocol state. ",
        99: "Information element non-existent or not implemented ",
        100: "Conditional IE error ",
        101: "Message not compatible with protocol state ",
        111: "Protocol error, unspecified ",
        112: "APN restriction value incompatible with active PDP context ",
        600: "An operation is pending. ",
        601: "An invalid port handle was detected. ",
        602: "The specified port is already open. ",
        603: "The caller's buffer is too small. ",
        604: "Incorrect information was specified. ",
        605: "The port information cannot be set. ",
        606: "The specified port is not connected. ",
        607: "An invalid event was detected. ",
        608: "A device was specified that does not exist. ",
        609: "A device type was specified that does not exist. ",
        610: "An invalid buffer was specified. ",
        611: "A route was specified that is not available. ",
        612: "A route was specified that is not allocated. ",
        613: "An invalid compression was specified. ",
        614: "There were insufficient buffers available. ",
        615: "The specified port was not found. ",
        616: "An asynchronous request is pending. ",
        617: "The modem (or other connecting device) is already disconnecting. ",
        618: "The specified port is not open. ",
        619: "The specified port is not connected. ",
        620: "No endpoints could be determined. ",
        621: "The system could not open the phone book file. ",
        622: "The system could not load the phone book file. ",
        623: "The system could not find the phone book entry for this connection. ",
        624: "The system could not update the phone book file. ",
        625: "The system found invalid information in the phone book file. ",
        626: "A string could not be loaded. ",
        627: "A key could not be found. ",
        628: "The connection was closed. ",
        629: "The connection was closed by the remote computer. ",
        630: "The modem (or other connecting device) was disconnected due to hardware failure. ",
        631: "The user disconnected the modem (or other connecting device). ",
        632: "An incorrect structure size was detected. ",
        633: "The modem (or other connecting device) is already in use or is not configured properly. ",
        634: "Your computer could not be registered on the remote network. ",
        635: "There was an unknown error. ",
        636: "The device attached to the port is not the one expected. ",
        637: "A string was detected that could not be converted. ",
        638: "The request has timed out. ",
        639: "No asynchronous net is available. ",
        640: "An error has occurred involving NetBIOS. ",
        641: "The server cannot allocate NetBIOS resources needed to support the client. ",
        642: "One of your computer's NetBIOS names is already registered on the remote network. ",
        643: "A network adapter at the server failed. ",
        644: "You will not receive network message popups. ",
        645: "There was an longernal authentication error. ",
        646: "The account is not permitted to log on at this time of day. ",
        647: "The account is disabled. ",
        648: "The password for this account has expired. ",
        649: "The account does not have permission to dial in. ",
        650: "The remote access server is not responding. ",
        651: "The modem (or other connecting device) has reported an error. ",
        652: "There was an unrecognized response from the modem (or other connecting device). ",
        653: "A macro required by the modem (or other connecting device) was not found in the device.INF file. ",
        654: "A command or response in the device.INF file section refers to an undefined macro. ",
        655: "The macro was not found in the device.INF file section. ",
        656: "The macro in the device.INF file section contains an undefined macro. ",
        657: "The device.INF file could not be opened. ",
        658: "The device name in the device.INF or media.INI file is too long. ",
        659: "The media.INI file refers to an unknown device name. ",
        660: "The device.INF file contains no responses for the command. ",
        661: "The device.INF file is missing a command. ",
        662: "There was an attempt to set a macro not listed in device.INF file section. ",
        663: "The media.INI file refers to an unknown device type. ",
        664: "The system has run out of memory. ",
        665: "The modem (or other connecting device) is not properly configured. ",
        666: "The modem (or other connecting device) is not functioning. ",
        667: "The system was unable to read the media.INI file. ",
        668: "The connection was terminated. ",
        669: "The usage parameter in the media.INI file is invalid. ",
        670: "The system was unable to read the section name from the media.INI file. ",
        671: "The system was unable to read the device type from the media.INI file. ",
        672: "The system was unable to read the device name from the media.INI file. ",
        673: "The system was unable to read the usage from the media.INI file. ",
        674: "The system was unable to read the maximum connection BPS rate from the media.INI file. ",
        675: "The system was unable to read the maximum carrier connection speed from the media.INI file. ",
        676: "The phone line is busy. ",
        677: "A person answered instead of a modem (or other connecting device). ",
        678: "There was no answer. ",
        679: "The system could not detect the carrier. ",
        680: "There was no dial tone. ",
        681: "The modem (or other connecting device) reported a general error. ",
        682: "There was an error in writing the section name. ",
        683: "There was an error in writing the device type. ",
        684: "There was an error in writing the device name. ",
        685: "There was an error in writing the maximum connection speed. ",
        686: "There was an error in writing the maximum carrier speed.",
        687: "There was an error in writing the usage. ",
        688: "There was an error in writing the default-off. ",
        689: "There was an error in reading the default-off. ",
        690: "ERROR_EMPTY_INI_FILE ",
        691: "Access was denied because the username and/or password was invalid on the domain. ",
        692: "There was a hardware failure in the modem (or other connecting device). ",
        693: "ERROR_NOT_BINARY_MACRO ",
        694: "ERROR_DCB_NOT_FOUND ",
        695: "The state machines are not started. ",
        696: "The state machines are already started. ",
        697: "The response looping did not complete. ",
        698: "A response keyname in the device.INF file is not in the expected format. ",
        699: "The modem (or other connecting device) response caused a buffer overflow. ",
        700: "The expanded command in the device.INF file is too long.",
        701: "The modem moved to a connection speed not supported by the COM driver. ",
        702: "Device response received when none expected. ",
        703: "The connection needs information from you, but the application does not allow user longeraction. ",
        704: "The callback number is invalid. ",
        705: "The authorization state is invalid. ",
        706: "ERROR_WRITING_INITBPS ",
        707: "There was an error related to the X.25 protocol. ",
        708: "The account has expired. ",
        709: "There was an error changing the password on the domain. The password might have been too short or might have matched a previously used password. ",
        710: "Serial overrun errors were detected while communicating with the modem. ",
        711: "The Remote Access Service Manager could not start. Additional information is provided in the event log. ",
        712: "The two-way port is initializing. Wait a few seconds and redial. ",
        713: "No active ISDN lines are available. ",
        714: "No ISDN channels are available to make the call. ",
        715: "Too many errors occurred because of poor phone line quality. ",
        716: "The Remote Access Service IP configuration is unusable.",
        717: "No IP addresses are available in the static pool of Remote Access Service IP addresses. ",
        718: "The connection timed out waiting for a valid response from the remote computer. ",
        719: "The connection was terminated by the remote computer. ",
        720: "The connection attempt failed because your computer and the remote computer could not agree on PPP control protocols. ",
        721: "The remote computer is not responding. ",
        722: "Invalid data was received from the remote computer. This data was ignored. ",
        723: "The phone number, including prefix and suffix, is too long. ",
        724: "The IPX protocol cannot dial out on the modem (or other connecting device) because this computer is not configured for dialing out (it is an IPX router). ",
        725: "The IPX protocol cannot dial in on the modem (or other connecting device) because this computer is not configured for dialing in (the IPX router is not installed). ",
        726: "The IPX protocol cannot be used for dialing out on more than one modem (or other connecting device) at a time. ",
        727: "Cannot access TCPCFG.DLL. ",
        728: "The system cannot find an IP adapter. ",
        729: "SLIP cannot be used unless the IP protocol is installed. ",
        730: "Computer registration is not complete. ",
        731: "The protocol is not configured. ",
        732: "Your computer and the remote computer could not agree on PPP control protocols. ",
        733: "Your computer and the remote computer could not agree on PPP control protocols. ",
        734: "The PPP link control protocol was terminated. ",
        735: "The requested address was rejected by the server. ",
        736: "The remote computer terminated the control protocol. ",
        737: "Loopback was detected. ",
        738: "The server did not assign an address. ",
        739: "The authentication protocol required by the remote server cannot use the stored password. Redial, entering the password explicitly. ",
        740: "An invalid dialing rule was detected. ",
        741: "The local computer does not support the required data encryption type. ",
        742: "The remote computer does not support the required data encryption type. ",
        743: "The remote computer requires data encryption. ",
        744: "The system cannot use the IPX network number assigned by the remote computer. Additional information is provided in the event log. ",
        745: "ERROR_INVALID_SMM ",
        746: "ERROR_SMM_UNINITIALIZED ",
        747: "ERROR_NO_MAC_FOR_PORT ",
        748: "ERROR_SMM_TIMEOUT ",
        749: "ERROR_BAD_PHONE_NUMBER ",
        750: "ERROR_WRONG_MODULE ",
        751: "The callback number contains an invalid character. Only the following 18 characters are allowed: 0 to 9, T, P, W, (, ), -, @, and space. ",
        752: "A syntax error was encountered while processing a script. ",
        753: "The connection could not be disconnected because it was created by the multi-protocol router. ",
        754: "The system could not find the multi-link bundle. ",
        755: "The system cannot perform automated dial because this connection has a custom dialer specified. ",
        756: "This connection is already being dialed. ",
        757: "Remote Access Services could not be started automatically. Additional information is provided in the event log. ",
        758: "Internet Connection Sharing is already enabled on the connection. ",
        759: "An error occurred while the existing longernet Connection Sharing settings were being changed. ",
        760: "An error occurred while routing capabilities were being enabled. ",
        761: "An error occurred while longernet Connection Sharing was being enabled for the connection. ",
        762: "An error occurred while the local network was being configured for sharing. ",
        763: "Internet Connection Sharing cannot be enabled. There is more than one LAN connection other than the connection to be shared. ",
        764: "No smart card reader is installed. ",
        765: "Internet Connection Sharing cannot be enabled. A LAN connection is already configured with the IP address that is required for automatic IP addressing. ",
        766: "A certificate could not be found. Connections that use the L2TP protocol over IPSec require the installation of a machine certificate, also known as a computer certificate. ",
        767: "Internet Connection Sharing cannot be enabled. The LAN connection selected as the private network has more than one IP address configured. Please reconfigure the LAN connection with a single IP address before enabling longernet Connection Sharing. ",
        768: "The connection attempt failed because of failure to encrypt data. ",
        769: "The specified destination is not reachable. ",
        770: "The remote computer rejected the connection attempt. ",
        771: "The connection attempt failed because the network is busy. ",
        772: "The remote computer's network hardware is incompatible with the type of call requested. ",
        773: "The connection attempt failed because the destination number has changed. ",
        774: "The connection attempt failed because of a temporary failure. Try connecting again. ",
        775: "The call was blocked by the remote computer. ",
        776: "The call could not be connected because the remote computer has invoked the Do Not Disturb feature. ",
        777: "The connection attempt failed because the modem (or other connecting device) on the remote computer is out of order. ",
        778: "It was not possible to verify the identity of the server. ",
        779: "To dial out using this connection you must use a smart card. ",
        780: "An attempted function is not valid for this connection. ",
        781: "The encryption attempt failed because no valid certificate was found. ",
        782: "Connection Sharing (NAT) is currently installed as a routing protocol, and must be removed before enabling longernet Connection Sharing. ",
        783: "Internet Connection Sharing cannot be enabled. The LAN connection selected as the private network is either not present, or is disconnected from the network. Please ensure that the LAN adapter is connected before enabling longernet Connection Sharing. ",
        784: "You cannot dial using this connection at logon time, because it is configured to use a user name different than the one on the smart card. If you want to use it at logon time, you must configure it to use the user name on the smart card. ",
        785: "You cannot dial using this connection at logon time, because it is not configured to use a smart card. If you want to use it at logon time, you must edit the properties of this connection so that it uses a smart card. ",
        786: "The L2TP connection attempt failed because there is no valid machine certificate on your computer for security authentication. ",
        787: "The L2TP connection attempt failed because the security layer could not authenticate the remote computer. ",
        788: "The L2TP connection attempt failed because the security layer could not negotiate compatible parameters with the remote computer. ",
        789: "The L2TP connection attempt failed because the security layer encountered a processing error during initial negotiations with the remote computer. ",
        790: "The L2TP connection attempt failed because certificate validation on the remote computer failed. ",
        791: "The L2TP connection attempt failed because security policy for the connection was not found. ",
        792: "The L2TP connection attempt failed because security negotiation timed out. ",
        793: "The L2TP connection attempt failed because an error occurred while negotiating security. ",
        794: "The Framed Protocol RADIUS attribute for this user is not PPP. ",
        795: "The Tunnel Type RADIUS attribute for this user is not correct. ",
        796: "The Service Type RADIUS attribute for this user is neither Framed nor Callback Framed. ",
        797: "The connection failed because the modem (or other connecting device) was not found. Please make sure that the modem or other connecting device is installed. ",
        798: "A certificate could not be found that can be used with this Extensible Authentication Protocol. ",
        799: "Not available",

    } 
    return switcher.get(type, "Unknown")
