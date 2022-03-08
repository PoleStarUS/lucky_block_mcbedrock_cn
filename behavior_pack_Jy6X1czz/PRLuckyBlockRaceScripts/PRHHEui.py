# -*- coding: utf-8 -*-

# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import mod.client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
# 获取组件工厂，用来创建组件
compFactory = clientApi.GetEngineCompFactory()

# 所有的UI类需要继承自引擎的ScreenNode类
class PRHHEUIScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        # 当前客户端的玩家Id
        self.mPlayerId = clientApi.GetLocalPlayerId()
        self.ClientSystem = clientApi.GetSystem("PRLuckyBlockRaceMod", "PRLuckyBlockRaceClientSystem")

    # Create函数是继承自ScreenNode，会在UI创建完成后被调用
    def Create(self):
        pass

    def Init(self):
        pass

    # 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧"""
    def Update(self):
        """
        node tick function
        """
        pass

    # 瞄准按钮的逻辑
    """def Aim(self):
        # 如果当前是开镜状态，关闭开镜UI并恢复视野范围，并显示角色
        if self.mShowSight:
            self.mShowSight = False
            self.SetVisible(self.mAimImage, True)
            self.SetVisible(self.mAimingImage, False)
            cameraComp = compFactory.CreateCamera(clientApi.GetLevelId())
            cameraComp.SetFov(self.mOriginalFov)
            modelComp = compFactory.CreateModel(self.mPlayerId)
            modelId = modelComp.GetModelId()
            modelComp.ShowModel(modelId)
        # 如果当前是不开镜状态，那么就开镜并调整视野范围，并隐藏角色
        else:
            self.mShowSight = True
            self.SetVisible(self.mAimImage, False)
            self.SetVisible(self.mAimingImage, True)
            cameraComp = compFactory.CreateCamera(clientApi.GetLevelId())
            cameraComp.SetFov(self.mOriginalFov + modConfig.SightFieldOfView)
            modelComp = compFactory.CreateModel(self.mPlayerId)
            modelId = modelComp.GetModelId()
            modelComp.HideModel(modelId)"""

    # 射击按钮的逻辑
    def Shoot(self):
        ClientSystem = clientApi.GetSystem("herobowMod", "heroBowClient")
        ClientSystem.AShoot()
        #print("SHOOT TEST")
        #localPlayerId = clientApi.GetLocalPlayerId()
        #data = {"playerId": localPlayerId}
        #self.ClientSystem.NotifyToServer("OnProjectileShoot", data)
