#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class PacketSessionInfo:
    def __init__(self,PacketSessionContextID ='',AttemptTime ='',SuccessTime ='',DisconnectTime ='',FailureTime ='',ApplicationProtocol =''):
        self.PacketSessionContextID = PacketSessionContextID
        self.AttemptTime = AttemptTime
        self.SuccessTime  = SuccessTime
        self.DisconnectTime = DisconnectTime
        self.FailureTime = FailureTime
        self.ApplicationProtocol = ApplicationProtocol

