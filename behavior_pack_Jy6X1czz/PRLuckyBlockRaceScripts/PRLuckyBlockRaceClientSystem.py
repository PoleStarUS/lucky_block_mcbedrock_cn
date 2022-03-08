# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
compFactory = clientApi.GetEngineCompFactory()
import random

class PRLuckyBlockRaceClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        super(PRLuckyBlockRaceClientSystem, self).__init__(namespace, systemName)
        print ("==== PRLuckyBlockRaceClientSystem Init ====")
        self.ListenEvent()
        self.ClientSystem = clientApi.GetSystem("PRLuckyBlockRaceMod", "PRLuckyBlockRaceClientSystem")
        self.mPlayerId = clientApi.GetLocalPlayerId()
        self.mitemName = {}

    def ListenEvent(self):
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnCarriedNewItemChangedClientEvent", self, self.OnCarriedNewItemChangedClientEvent)

    def UnListenEvent(self):
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnCarriedNewItemChangedClientEvent", self, self.OnCarriedNewItemChangedClientEvent)

    def OnCarriedNewItemChangedClientEvent(self, args):
        i = self.mPlayerId
        self.mitemName[i] = args["itemDict"]["itemName"]
        print(self.mitemName)

    def Destroy(self):
        pass