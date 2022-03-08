# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import json
import random
minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()

class PRLuckyBlockRaceServerSystem(ServerSystem):

    def __init__(self, namespace, systemName):
        super(PRLuckyBlockRaceServerSystem, self).__init__(namespace, systemName)
        self.itemName = {}
        #petcomp = serverApi.GetEngineCompFactory().CreatePet(serverApi.GetLevelId())
        #petcomp.Disable()#禁用Netease Pet
        self.ListenEvent()

    def ListenEvent(self):
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DestroyBlockEvent",self, self.DestroyBlockEvent)

    def UnListenEvent(self):
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DestroyBlockEvent",self, self.DestroyBlockEvent)

    def DestroyBlockEvent(self, args):
        i = args["playerId"]
        dimension = args["dimensionId"]
        ecomp = serverApi.GetEngineCompFactory().CreateActorLoot(i)
        cmdcomp = serverApi.GetEngineCompFactory().CreateCommand(serverApi.GetLevelId())
        rescomp = serverApi.GetEngineCompFactory().CreateEffect(i)
        x = args["x"]
        y = args["y"]
        z = args["z"]
        if args["fullName"] == "pr:race_lucky_block":
            #randomcomp = 66
            randomcomp = random.randint(-15,67)#当此值为负数时，召唤霉运事件。当此值为正数时，召唤幸运事件。
            if randomcomp == -15:#生成黑曜石小屋
                cmdcomp.SetCommand("/fill ~ ~ ~ ~ ~ ~ water",i)
                cmdcomp.SetCommand("/fill ~ ~1 ~ ~ ~1 ~ water",i)
                cmdcomp.SetCommand("/fill ~1 ~-1 ~1 ~-1 ~-1 ~-1 obsidian",i)
                cmdcomp.SetCommand("/fill ~1 ~2 ~1 ~-1 ~2 ~-1 obsidian",i)
                cmdcomp.SetCommand("/fill ~-1 ~0 ~1 ~1 ~1 ~1 obsidian",i)
                cmdcomp.SetCommand("/fill ~-1 ~0 ~-1 ~1 ~1 ~-1 obsidian",i)
                cmdcomp.SetCommand("/fill ~1 ~0 ~1 ~1 ~1 ~-1 obsidian",i)
                cmdcomp.SetCommand("/fill ~-1 ~0 ~ ~-1 ~1 ~ obsidian",i)
                cmdcomp.SetCommand("/fill ~-1 ~1 ~ ~-1 ~1 ~ glass",i)
                cmdcomp.SetCommand("/fill ~1 ~1 ~ ~1 ~1 ~ glass",i)
                cmdcomp.SetCommand("/fill ~ ~1 ~1 ~ ~1 ~1 glass",i)
                cmdcomp.SetCommand("/fill ~ ~1 ~-1 ~ ~1 ~-1 glass",i)
            if randomcomp == -14:#生成8只猪 + 村民
                cmdcomp.SetCommand("/summon villager ~ ~ ~",i)
                for count in range(8):
                    cmdcomp.SetCommand("/summon pig ~ ~ ~",i)
            if randomcomp == -13:#生成红石 + 掉落的TNT
                cmdcomp.SetCommand("/summon tnt "+ str(x) + " " + str(y+1) + " " + str(z),i)
                cmdcomp.SetCommand("/summon tnt "+ str(x) + " " + str(y+1) + " " + str(z),i)
                cmdcomp.SetCommand("/summon tnt "+ str(x) + " " + str(y+1) + " " + str(z),i)
                cmdcomp.SetCommand("/summon tnt "+ str(x) + " " + str(y+1) + " " + str(z),i)
                cmdcomp.SetCommand("/summon tnt "+ str(x) + " " + str(y+1) + " " + str(z),i)
                cmdcomp.SetCommand("/summon tnt "+ str(x) + " " + str(y+1) + " " + str(z),i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y) + " " + str(z) + " redstone_block",i)
            if randomcomp == -12:#生成恶魂
                cmdcomp.SetCommand("/summon ghast ~ ~5 ~",i)
            if randomcomp == -11:#生成基岩 + Sigh
                cmdcomp.SetCommand("/setblock " + str(x) + " " + str(y) + " " + str(z) + " bedrock ",i)
            if randomcomp == -10:#生成监狱 + 顶部铁砧
                cmdcomp.SetCommand("/fill ~1 ~-1 ~1 ~-1 ~-1 ~-1 stonebrick",i)
                cmdcomp.SetCommand("/fill ~-1 ~0 ~1 ~1 ~3 ~1 iron_bars",i)
                cmdcomp.SetCommand("/fill ~-1 ~0 ~-1 ~1 ~3 ~-1 iron_bars",i)
                cmdcomp.SetCommand("/fill ~1 ~0 ~1 ~1 ~3 ~-1 iron_bars",i)
                cmdcomp.SetCommand("/fill ~-1 ~0 ~ ~-1 ~3 ~ iron_bars",i)
                cmdcomp.SetCommand("/fill ~ ~100 ~ ~ ~100 ~ anvil",i)
                cmdcomp.SetCommand("/fill ~ ~101 ~ ~ ~101 ~ anvil",i)
            if randomcomp == -9:#生成监狱 + 顶部岩浆
                cmdcomp.SetCommand("/fill ~1 ~-1 ~1 ~-1 ~-1 ~-1 stonebrick",i)
                cmdcomp.SetCommand("/fill ~-1 ~0 ~1 ~1 ~3 ~1 iron_bars",i)
                cmdcomp.SetCommand("/fill ~-1 ~0 ~-1 ~1 ~3 ~-1 iron_bars",i)
                cmdcomp.SetCommand("/fill ~1 ~0 ~1 ~1 ~3 ~-1 iron_bars",i)
                cmdcomp.SetCommand("/fill ~-1 ~0 ~ ~-1 ~3 ~ iron_bars",i)
                cmdcomp.SetCommand("/fill ~ ~3 ~ ~ ~3 ~ flowing_lava",i)
            if randomcomp == -8:#生成直接爆炸
                cmdcomp.SetCommand("/summon pr:lightning_bolt_explode "+ str(x) + " " + str(y) + " " + str(z),i)
            if randomcomp == -7:#生成大量爆炸的TNT
                cmdcomp.SetCommand("/summon tnt ~ ~5 ~",i)
                cmdcomp.SetCommand("/summon tnt ~ ~5 ~",i)
                cmdcomp.SetCommand("/summon tnt ~ ~5 ~",i)
                cmdcomp.SetCommand("/summon tnt ~ ~5 ~",i)
                cmdcomp.SetCommand("/summon tnt ~ ~5 ~",i)
                cmdcomp.SetCommand("/summon tnt ~ ~5 ~",i)
                cmdcomp.SetCommand("/summon tnt ~ ~5 ~",i)
                cmdcomp.SetCommand("/summon tnt ~ ~5 ~",i)
                cmdcomp.SetCommand("/summon tnt ~ ~5 ~",i)
                cmdcomp.SetCommand("/summon tnt ~ ~5 ~",i)
            if randomcomp == -6:#给予玩家Blindness Slowness，生成大量怪物在周边，将时间调至午夜
                res = rescomp.AddEffectToEntity("blindness", 30, 4, False)
                res = rescomp.AddEffectToEntity("slowness", 30, 4, False)
                cmdcomp.SetCommand("/time set midnight",i)
                cmdcomp.SetCommand("/summon zombie ~ ~ ~3",i)
                cmdcomp.SetCommand("/summon zombie ~ ~ ~-3",i)
                cmdcomp.SetCommand("/summon zombie ~ ~ ~-4",i)
                cmdcomp.SetCommand("/summon zombie ~ ~ ~4",i)
                cmdcomp.SetCommand("/summon zombie ~ ~ ~5",i)
                cmdcomp.SetCommand("/summon zombie ~ ~ ~-5",i)
                cmdcomp.SetCommand("/summon zombie ~3 ~ ~",i)
                cmdcomp.SetCommand("/summon zombie ~-3 ~ ~",i)
                cmdcomp.SetCommand("/summon zombie ~-4 ~ ~",i)
                cmdcomp.SetCommand("/summon zombie ~4 ~ ~",i)
                cmdcomp.SetCommand("/summon zombie ~5 ~ ~",i)
                cmdcomp.SetCommand("/summon zombie ~-5 ~ ~",i)

                cmdcomp.SetCommand("/summon spider ~ ~ ~3",i)
                cmdcomp.SetCommand("/summon spider ~ ~ ~-3",i)
                cmdcomp.SetCommand("/summon spider ~ ~ ~-4",i)
                cmdcomp.SetCommand("/summon spider ~ ~ ~4",i)
                cmdcomp.SetCommand("/summon spider ~ ~ ~5",i)
                cmdcomp.SetCommand("/summon spider ~ ~ ~-5",i)
                cmdcomp.SetCommand("/summon spider ~3 ~ ~",i)
                cmdcomp.SetCommand("/summon spider ~-3 ~ ~",i)
                cmdcomp.SetCommand("/summon spider ~-4 ~ ~",i)
                cmdcomp.SetCommand("/summon spider ~4 ~ ~",i)
                cmdcomp.SetCommand("/summon spider ~5 ~ ~",i)
                cmdcomp.SetCommand("/summon spider ~-5 ~ ~",i)

                cmdcomp.SetCommand("/summon creeper ~ ~ ~3",i)
                cmdcomp.SetCommand("/summon creeper ~ ~ ~-3",i)
                cmdcomp.SetCommand("/summon creeper ~ ~ ~-4",i)
                cmdcomp.SetCommand("/summon creeper ~ ~ ~4",i)

                cmdcomp.SetCommand("/summon endermite ~ ~ ~3",i)
                cmdcomp.SetCommand("/summon endermite ~ ~ ~-3",i)
                cmdcomp.SetCommand("/summon endermite ~ ~ ~-4",i)
                cmdcomp.SetCommand("/summon endermite ~ ~ ~4",i)
                cmdcomp.SetCommand("/summon endermite ~ ~ ~5",i)
                cmdcomp.SetCommand("/summon endermite ~ ~ ~-5",i)
                cmdcomp.SetCommand("/summon endermite ~3 ~ ~",i)
                cmdcomp.SetCommand("/summon endermite ~-3 ~ ~",i)
                cmdcomp.SetCommand("/summon endermite ~-4 ~ ~",i)
                cmdcomp.SetCommand("/summon endermite ~4 ~ ~",i)
                cmdcomp.SetCommand("/summon endermite ~5 ~ ~",i)
                cmdcomp.SetCommand("/summon endermite ~-5 ~ ~",i)


            if randomcomp == -5:#召唤巨型岩浆怪
                cmdcomp.SetCommand("/summon minecraft:magma_cube ~ ~ ~ minecraft:super_magma_slime_large",i)
            if randomcomp == -4:#召唤巨型史莱姆
                cmdcomp.SetCommand("/summon minecraft:slime ~ ~ ~ minecraft:super_slime_large",i)
            if randomcomp == -3:#召唤陷阱
                cmdcomp.SetCommand("/fill ~1 ~ ~1 ~-1 ~-16 ~-1 air",i)
                cmdcomp.SetCommand("/fill ~1 ~-17 ~1 ~-1 ~-17 ~-1 web",i)
                cmdcomp.SetCommand("/fill ~1 ~-18 ~1 ~-1 ~-18 ~-1 lava",i)
            if randomcomp == -2:#召唤骷髅马军团
                cmdcomp.SetCommand("/summon minecraft:skeleton_horse " + str(x) + " " + str(y) + " " + str(z) + " minecraft:set_trap")
            if randomcomp == -1:#召唤女巫和大量蝙蝠
                cmdcomp.SetCommand("/summon minecraft:witch " + str(x) + " " + str(y) + " " + str(z))
                randomcomp = random.randint(20,40)
                for i in range(randomcomp):
                    cmdcomp.SetCommand("/summon minecraft:bat " + str(x) + " " + str(y+1) + " " + str(z),i)
            if randomcomp == 0:#召唤闪电苦力怕
                cmdcomp.SetCommand("/summon minecraft:creeper " + str(x) + " " + str(y) + " " + str(z))
                cmdcomp.SetCommand("/summon minecraft:lightning_bolt " + str(x) + " " + str(y) + " " + str(z))
            if randomcomp == 1:#召唤幸运四叶草
                result = ecomp.SpawnLootTable((x, y, z), 'pureraincube:magic_clover')
            if randomcomp == 2:#生成唱片和唱片机
                itemDict = {
                'itemName': 'minecraft:jukebox',
                'count': 1,
                }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                r_randomcomp = random.randint(1,13)
                if r_randomcomp == 1:
                    itemDict = {
                    'itemName': 'minecraft:record_13',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                if r_randomcomp == 2:
                    itemDict = {
                    'itemName': 'minecraft:record_cat',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                if r_randomcomp == 3:
                    itemDict = {
                    'itemName': 'minecraft:record_blocks',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                if r_randomcomp == 4:
                    itemDict = {
                    'itemName': 'minecraft:record_chirp',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                if r_randomcomp == 5:
                    itemDict = {
                    'itemName': 'minecraft:record_far',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                if r_randomcomp == 6:
                    itemDict = {
                    'itemName': 'minecraft:record_wait',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                if r_randomcomp == 7:
                    itemDict = {
                    'itemName': 'minecraft:record_pigstep',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                if r_randomcomp == 8:
                    itemDict = {
                    'itemName': 'minecraft:record_mall',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                if r_randomcomp == 9:
                    itemDict = {
                    'itemName': 'minecraft:record_mellohi',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                if r_randomcomp == 10:
                    itemDict = {
                    'itemName': 'minecraft:record_stal',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                if r_randomcomp == 11:
                    itemDict = {
                    'itemName': 'minecraft:record_strad',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                if r_randomcomp == 12:
                    itemDict = {
                    'itemName': 'minecraft:record_ward',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                if r_randomcomp == 13:
                    itemDict = {
                    'itemName': 'minecraft:record_11',
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 3:#生成僵尸巨人
                entityId = self.CreateEngineEntityByTypeStr('pr:giant_zombie', (x, y, z), (0, 0), dimension)
            if randomcomp == 4:#生成龙蛋
                itemDict = {
                    'itemName': 'minecraft:dragon_egg',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 5:#生成大量经验瓶
                randomcomp = random.randint(32,64)
                for i in range(randomcomp):
                    cmdcomp.SetCommand("/summon minecraft:xp_bottle " + str(x) + " " + str(y+1) + " " + str(z),i)
            if randomcomp == 6:#生成渔夫套装
                itemDict = {
                    'itemName': 'minecraft:fishing_rod',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(3,6)
                itemDict = {
                    'itemName': 'minecraft:fish',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                
                randomcomp = random.randint(3,6)
                itemDict = {
                    'itemName': 'minecraft:salmon',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(3,6)
                itemDict = {
                    'itemName': 'minecraft:clownfish',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(3,6)
                itemDict = {
                    'itemName': 'minecraft:pufferfish',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

            if randomcomp == 7:#生成大量陶瓦
                clay_dict = ['minecraft:hardened_clay']
                for clay in clay_dict:
                    randomcomp = random.randint(32,64)
                    itemDict = {
                    'itemName': clay,
                    'count': randomcomp,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                    for number in range(0 ,15):
                        randomcomp = random.randint(32,64)
                        itemDict = {
                        'itemName': 'minecraft:stained_hardened_clay',
                        'count': randomcomp,
                        'auxValue': number,
                        }
                        itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                        itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 8:#生成Bob僵尸
                cmdcomp.SetCommand("/summon minecraft:zombie §bBob " + str(x) + " " + str(y) + " " + str(z))
            if randomcomp == 9:#生成信标
                itemDict = {
                    'itemName': 'minecraft:beacon',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 10:#生成末影箱
                randomcomp = random.randint(1,6)
                itemDict = {
                    'itemName': 'minecraft:ender_chest',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 11:#生成金苹果和附魔金苹果
                randomcomp = random.randint(3,6)
                itemDict = {
                    'itemName': 'minecraft:golden_apple',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(3,6)
                itemDict = {
                    'itemName': 'minecraft:appleenchanted',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

            if randomcomp == 12:#生成胡萝卜
                randomcomp = random.randint(1,32)
                itemDict = {
                    'itemName': 'minecraft:golden_carrot',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())

                randomcomp = random.randint(1,32)
                itemDict = {
                    'itemName': 'minecraft:carrot',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
            if randomcomp == 13:#生成花束
                flower_dict = ['minecraft:yellow_flower']
                for flower in flower_dict:
                    randomcomp = random.randint(16,32)
                    itemDict = {
                    'itemName': flower,
                    'count': randomcomp,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                    for number in range(0 ,10):
                        randomcomp = random.randint(16,32)
                        itemDict = {
                        'itemName': 'minecraft:red_flower',
                        'count': randomcomp,
                        'auxValue': number,
                        }
                        itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                        itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 14:#生成木制工具套装
                tool_dict = ['minecraft:wooden_sword','minecraft:wooden_axe','minecraft:wooden_pickaxe','minecraft:wooden_shovel','minecraft:wooden_hoe']
                randomcomp_2 = random.randint(1,5)
                for tool in range(randomcomp_2):
                    td = random.choice(tool_dict)
                    itemDict = {
                    'itemName': td,
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 15:#生成金制工具套装
                tool_dict = ['minecraft:golden_sword','minecraft:golden_axe','minecraft:golden_pickaxe','minecraft:golden_shovel','minecraft:golden_hoe']
                randomcomp_2 = random.randint(1,5)
                for tool in range(randomcomp_2):
                    td = random.choice(tool_dict)
                    itemDict = {
                    'itemName': td,
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 16:#生成石制工具套装
                tool_dict = ['minecraft:stone_sword','minecraft:stone_axe','minecraft:stone_pickaxe','minecraft:stone_shovel','minecraft:stone_hoe']
                randomcomp_2 = random.randint(1,5)
                for tool in range(randomcomp_2):
                    td = random.choice(tool_dict)
                    itemDict = {
                    'itemName': td,
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 17:#生成铁制工具套装
                tool_dict = ['minecraft:iron_sword','minecraft:iron_axe','minecraft:iron_pickaxe','minecraft:iron_shovel','minecraft:iron_hoe']
                randomcomp_2 = random.randint(1,5)
                for tool in range(randomcomp_2):
                    td = random.choice(tool_dict)
                    itemDict = {
                    'itemName': td,
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 18:#生成钻石制工具套装
                tool_dict = ['minecraft:diamond_sword','minecraft:diamond_axe','minecraft:diamond_pickaxe','minecraft:diamond_shovel','minecraft:diamond_hoe']
                randomcomp_2 = random.randint(1,5)
                for tool in range(randomcomp_2):
                    td = random.choice(tool_dict)
                    itemDict = {
                    'itemName': td,
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 19:#生成下界合金制工具套装
                tool_dict = ['minecraft:netherite_sword','minecraft:netherite_axe','minecraft:netherite_pickaxe','minecraft:netherite_shovel','minecraft:netherite_hoe']
                randomcomp_2 = random.randint(1,5)
                for tool in range(randomcomp_2):
                    td = random.choice(tool_dict)
                    itemDict = {
                    'itemName': td,
                    'count': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 20:#生成弓箭套装
                randomcomp = random.randint(32,64)
                itemDict = {
                    'itemName': 'minecraft:arrow',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                itemDict = {
                    'itemName': 'minecraft:bow',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

            if randomcomp == 21:#生成弓弩套装
                randomcomp = random.randint(32,64)
                itemDict = {
                    'itemName': 'minecraft:arrow',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                itemDict = {
                    'itemName': 'minecraft:crossbow',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 22:#生成金锭
                randomcomp = random.randint(12,32)
                itemDict = {
                    'itemName': 'minecraft:gold_ingot',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, 0, (x,y,z))
            if randomcomp == 23:#生成南瓜
                randomcomp = random.randint(10,20)
                itemDict = {
                    'itemName': 'minecraft:pumpkin',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(10,20)
                itemDict = {
                    'itemName': 'minecraft:lit_pumpkin',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 24:#生成鞍
                randomcomp = random.randint(1,3)
                itemDict = {
                    'itemName': 'minecraft:saddle',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 25:#生成图书
                randomcomp = random.randint(1,12)
                itemDict = {
                    'itemName': 'minecraft:bookshelf',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(1,12)
                itemDict = {
                    'itemName': 'minecraft:book',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 26:#生成兔子
                cmdcomp.SetCommand("/summon minecraft:rabbit ~3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:rabbit ~-3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:rabbit ~3 ~ ~-3 ",i)
                cmdcomp.SetCommand("/summon minecraft:rabbit ~-3 ~ ~-3 ",i)
                cmdcomp.SetCommand("/summon minecraft:rabbit ~-3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:rabbit ~ ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:rabbit ~3 ~ ~ ",i)
            if randomcomp == 27:#生成海晶石
                randomcomp = random.randint(16,64)
                itemDict = {
                    'itemName': 'minecraft:prismarine',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(16,64)
                itemDict = {
                    'itemName': 'minecraft:prismarine',
                    'count': randomcomp,
                    'auxValue': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(16,64)
                itemDict = {
                    'itemName': 'minecraft:prismarine_crystals',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(16,64)
                itemDict = {
                    'itemName': 'minecraft:prismarine_shard',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(16,64)
                itemDict = {
                    'itemName': 'minecraft:sealantern',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

            if randomcomp == 28:#生成石英
                randomcomp = random.randint(16,64)
                itemDict = {
                    'itemName': 'minecraft:quartz',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(16,64)
                itemDict = {
                    'itemName': 'minecraft:quartz_block',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(16,64)
                itemDict = {
                    'itemName': 'minecraft:quartz_ore',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 29:#生成马铃薯
                randomcomp = random.randint(16,64)
                itemDict = {
                    'itemName': 'minecraft:potato',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(16,64)
                itemDict = {
                    'itemName': 'minecraft:baked_potato',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(16,64)
                itemDict = {
                    'itemName': 'minecraft:poisonous_potato',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                cmdcomp.SetCommand("/summon minecraft:fireworks_rocket " + str(x) + " " + str(y) + " " + str(z))
            if randomcomp == 30:#生成大量TNT
                randomcomp = random.randint(1,16)
                itemDict = {
                    'itemName': 'minecraft:tnt',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                itemDict = {
                    'itemName': 'minecraft:flint_and_steel',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 31:#生成红石设备
                tool_dict = ['minecraft:redstone','minecraft:repeater','minecraft:comparator','minecraft:redstone_torch','minecraft:lever','minecraft:golden_rail','minecraft:hopper']
                randomcomp_2 = random.randint(1,7)
                for tool in range(randomcomp_2):
                    td = random.choice(tool_dict)
                    randomcomp = random.randint(16,64)
                    itemDict = {
                    'itemName': td,
                    'count': randomcomp,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 32:#生成Dropper
                randomcomp = random.randint(16,64)
                itemDict = {
                    'itemName': 'minecraft:dropper',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 33:#生成大量彩虹羊先生
                cmdcomp.SetCommand("/summon minecraft:sheep jeb_ ~3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:sheep jeb_ ~-3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:sheep jeb_ ~3 ~ ~-3 ",i)
                cmdcomp.SetCommand("/summon minecraft:sheep jeb_ ~-3 ~ ~-3 ",i)
                cmdcomp.SetCommand("/summon minecraft:sheep jeb_ ~-3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:sheep jeb_ ~ ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:sheep jeb_ ~3 ~ ~ ",i)
            if randomcomp == 34:#生成炼药装备
                tool_dict = ['minecraft:blaze_rod','minecraft:blaze_powder','minecraft:rabbit_foot','minecraft:magma_cream','minecraft:fermented_spider_eye','minecraft:phantom_membrane','minecraft:ghast_tear']
                randomcomp_2 = random.randint(1,7)
                for tool in range(randomcomp_2):
                    td = random.choice(tool_dict)
                    randomcomp = random.randint(1,32)
                    itemDict = {
                    'itemName': td,
                    'count': randomcomp,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 35:#生成头颅
                randomcomp_2 = random.randint(0,5)
                if randomcomp_2 ==5:
                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 5,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 ==4:
                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 5,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 4,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 ==3:
                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 5,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 4,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 3,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 ==2:
                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 5,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 4,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 3,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 2,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 ==1:
                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 5,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 4,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 3,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 2,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 ==0:
                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 5,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 4,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 3,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 2,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 1,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                    itemDict = {
                    'itemName': 'minecraft:skull',
                    'count': 1,
                    'auxValue': 0,
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 36:#生成桶 水桶 岩浆桶 牛奶桶
                itemDict = {
                    'itemName': 'minecraft:bucket',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                
                itemDict = {
                    'itemName': 'minecraft:milk_bucket',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                itemDict = {
                    'itemName': 'minecraft:lava_bucket',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                itemDict = {
                    'itemName': 'minecraft:water_bucket',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 37:#生成大量狼
                cmdcomp.SetCommand("/summon minecraft:wolf ~3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:wolf ~-3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:wolf ~3 ~ ~-3 ",i)
                cmdcomp.SetCommand("/summon minecraft:wolf ~-3 ~ ~-3 ",i)
                cmdcomp.SetCommand("/summon minecraft:wolf ~-3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:wolf ~ ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:wolf ~3 ~ ~ ",i)
                randomcomp_2 = random.randint(1,32)
                itemDict = {
                    'itemName': 'minecraft:bone',
                    'count': randomcomp_2,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 38:#生成大量豹猫
                cmdcomp.SetCommand("/summon minecraft:cat ~3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:cat ~-3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:cat ~3 ~ ~-3 ",i)
                cmdcomp.SetCommand("/summon minecraft:cat ~-3 ~ ~-3 ",i)
                cmdcomp.SetCommand("/summon minecraft:cat ~-3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:cat ~ ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:cat ~3 ~ ~ ",i)
                randomcomp_2 = random.randint(1,32)
                itemDict = {
                    'itemName': 'minecraft:fish',
                    'count': randomcomp_2,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 39:#生成南瓜派
                randomcomp = random.randint(1,32)
                itemDict = {
                    'itemName': 'minecraft:pumpkin_pie',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 40:#生成马 骷髅马 僵尸马
                cmdcomp.SetCommand("/summon minecraft:horse ~3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:horse ~-3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:horse ~3 ~ ~-3 ",i)
                cmdcomp.SetCommand("/summon minecraft:horse ~-3 ~ ~-3 ",i)
                cmdcomp.SetCommand("/summon minecraft:zombie_horse ~-3 ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:zombie_horse ~ ~ ~3 ",i)
                cmdcomp.SetCommand("/summon minecraft:skeleton_horse ~3 ~ ~ ",i)
                cmdcomp.SetCommand("/summon minecraft:skeleton_horse ~3 ~ ~-3 ",i)
            if randomcomp == 41:#生成随机生物蛋
                pass
            if randomcomp == 42:#生成钟表
                itemDict = {
                    'itemName': 'minecraft:clock',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 43:#生成黑曜石
                randomcomp_2 = random.randint(1,16)
                itemDict = {
                    'itemName': 'minecraft:obsidian',
                    'count': randomcomp_2,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 44:#生成牛肉
                randomcomp_2 = random.randint(1,16)
                itemDict = {
                    'itemName': 'minecraft:beef',
                    'count': randomcomp_2,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp_2 = random.randint(1,16)
                itemDict = {
                    'itemName': 'minecraft:cooked_beef',
                    'count': randomcomp_2,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 45:#生成青金石块 + 水声音 + 水粒子
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y) + " " + str(z) + " lapis_block",i)
                cmdcomp.SetCommand("/playsound bucket.fill_water @p",i)
                #
                cmdcomp.SetCommand("/particle minecraft:water_splash_particle_manual "+ str(x) + " " + str(y+1) + " " + str(z),i)
                cmdcomp.SetCommand("/particle minecraft:water_splash_particle_manual "+ str(x+1) + " " + str(y) + " " + str(z),i)
                cmdcomp.SetCommand("/particle minecraft:water_splash_particle_manual "+ str(x-1) + " " + str(y) + " " + str(z),i)
                cmdcomp.SetCommand("/particle minecraft:water_splash_particle_manual "+ str(x) + " " + str(y-1) + " " + str(z),i)
                cmdcomp.SetCommand("/particle minecraft:water_splash_particle_manual "+ str(x) + " " + str(y+1) + " " + str(z),i)
            if randomcomp == 46:#生成干草块
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y) + " " + str(z) + " hay_block",i)
            if randomcomp == 47:#生成绿宝石块 + 绿色粒子
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y) + " " + str(z) + " emerald_block",i)
            if randomcomp == 48:#生成大量多彩陶瓦块 + 顶部钻石块 + 顶部雷
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y) + " " + str(z) + " minecraft:silver_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+1) + " " + str(z) + " minecraft:white_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+2) + " " + str(z) + " minecraft:gray_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+3) + " " + str(z) + " minecraft:black_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+4) + " " + str(z) + " minecraft:brown_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+5) + " " + str(z) + " minecraft:red_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+6) + " " + str(z) + " minecraft:orange_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+7) + " " + str(z) + " minecraft:magenta_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+8) + " " + str(z) + " minecraft:yellow_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+9) + " " + str(z) + " minecraft:lime_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+10) + " " + str(z) + " minecraft:green_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+11) + " " + str(z) + " minecraft:cyan_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+12) + " " + str(z) + " minecraft:light_blue_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+13) + " " + str(z) + " minecraft:purple_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+14) + " " + str(z) + " minecraft:pink_glazed_terracotta",i)
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y+15) + " " + str(z) + " minecraft:diamond_block",i)
                cmdcomp.SetCommand("/summon lightning_bolt "+ str(x) + " " + str(y+16) + " " + str(z),i)
            if randomcomp == 49:#生成皮革装备
                randomcomp = random.randint(1,32)
                itemDict = {
                    'itemName': 'minecraft:leather',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 50:#生成兔肉煲
                itemDict = {
                    'itemName': 'minecraft:rabbit_stew',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                itemDict = {
                    'itemName': 'minecraft:rabbit_stew',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                itemDict = {
                    'itemName': 'minecraft:rabbit_stew',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 51:#生成海绵
                itemDict = {
                    'itemName': 'minecraft:sponge',
                    'count': 1,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 52:#生成腐肉
                randomcomp = random.randint(1,32)
                itemDict = {
                    'itemName': 'minecraft:rotten_flesh',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 53:#生成木棍
                randomcomp = random.randint(1,32)
                itemDict = {
                    'itemName': 'minecraft:stick',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 54:#生成鱼和熟的鱼
                randomcomp = random.randint(1,16)
                itemDict = {
                    'itemName': 'minecraft:fish',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(1,16)
                itemDict = {
                    'itemName': 'minecraft:cooked_fish',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 55:#生成鸡肉和熟的鸡肉
                randomcomp = random.randint(1,16)
                itemDict = {
                    'itemName': 'minecraft:chicken',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(1,16)
                itemDict = {
                    'itemName': 'minecraft:cooked_chicken',
                    'count': randomcomp,
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 56:#生成染料
                randomcomp_2 = random.randint(1,16)
                randomcomp = random.randint(1,32)
                if randomcomp_2 == 1:
                    itemDict = {
                    'itemName': 'minecraft:black_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 2:
                    itemDict = {
                    'itemName': 'minecraft:red_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 3:
                    itemDict = {
                    'itemName': 'minecraft:green_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 4:
                    itemDict = {
                    'itemName': 'minecraft:brown_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 5:
                    itemDict = {
                    'itemName': 'minecraft:blue_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 6:
                    itemDict = {
                    'itemName': 'minecraft:purple_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 7:
                    itemDict = {
                    'itemName': 'minecraft:cyan_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 8:
                    itemDict = {
                    'itemName': 'minecraft:light_gray_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 9:
                    itemDict = {
                    'itemName': 'minecraft:gray_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 10:
                    itemDict = {
                    'itemName': 'minecraft:pink_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 11:
                    itemDict = {
                    'itemName': 'minecraft:lime_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 12:
                    itemDict = {
                    'itemName': 'minecraft:yellow_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 13:
                    itemDict = {
                    'itemName': 'minecraft:light_blue_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 14:
                    itemDict = {
                    'itemName': 'minecraft:magenta_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 15:
                    itemDict = {
                    'itemName': 'minecraft:orange_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                if randomcomp_2 == 16:
                    itemDict = {
                    'itemName': 'minecraft:white_dye',
                    'count': randomcomp
                    }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 57:#生成附魔台
                itemDict = {
                    'itemName': 'minecraft:enchanting_table',
                    'count': 1
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(1,16)
                itemDict = {
                    'itemName': 'minecraft:bookshelf',
                    'count': randomcomp
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 58:#生成画
                randomcomp = random.randint(1,16)
                itemDict = {
                    'itemName': 'minecraft:painting',
                    'count': randomcomp
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 59:#钻石块 + 顶部雷
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y) + " " + str(z) + " minecraft:diamond_block",i)
                cmdcomp.SetCommand("/summon lightning_bolt "+ str(x) + " " + str(y+1) + " " + str(z),i)
            if randomcomp == 60:#铁块 + 烟雾
                cmdcomp.SetCommand("/setblock "+ str(x) + " " + str(y) + " " + str(z) + " minecraft:iron_block",i)
                cmdcomp.SetCommand("/summon lightning_bolt "+ str(x) + " " + str(y+1) + " " + str(z),i)
            if randomcomp == 61:#生成原版战利品箱
                randomcomp2 = random.randint(1,44)
                if randomcomp2 == 1:
                    cmdcomp.SetCommand("/structure load chest:chest_1 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 2:
                    cmdcomp.SetCommand("/structure load chest:chest_2 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 3:
                    cmdcomp.SetCommand("/structure load chest:chest_3 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 4:
                    cmdcomp.SetCommand("/structure load chest:chest_4 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 5:
                    cmdcomp.SetCommand("/structure load chest:chest_5 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 6:
                    cmdcomp.SetCommand("/structure load chest:chest_6 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 7:
                    cmdcomp.SetCommand("/structure load chest:chest_7 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 8:
                    cmdcomp.SetCommand("/structure load chest:chest_8 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 9:
                    cmdcomp.SetCommand("/structure load chest:chest_9 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 10:
                    cmdcomp.SetCommand("/structure load chest:chest_10 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 11:
                    cmdcomp.SetCommand("/structure load chest:chest_11 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 12:
                    cmdcomp.SetCommand("/structure load chest:chest_12 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 13:
                    cmdcomp.SetCommand("/structure load chest:chest_13 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 14:
                    cmdcomp.SetCommand("/structure load chest:chest_14 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 15:
                    cmdcomp.SetCommand("/structure load chest:chest_15 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 16:
                    cmdcomp.SetCommand("/structure load chest:chest_16 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 17:
                    cmdcomp.SetCommand("/structure load chest:chest_17 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 18:
                    cmdcomp.SetCommand("/structure load chest:chest_18 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 19:
                    cmdcomp.SetCommand("/structure load chest:chest_19 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 20:
                    cmdcomp.SetCommand("/structure load chest:chest_20 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 21:
                    cmdcomp.SetCommand("/structure load chest:chest_21 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 22:
                    cmdcomp.SetCommand("/structure load chest:chest_22 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 23:
                    cmdcomp.SetCommand("/structure load chest:chest_23 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 24:
                    cmdcomp.SetCommand("/structure load chest:chest_24 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 25:
                    cmdcomp.SetCommand("/structure load chest:chest_25 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 26:
                    cmdcomp.SetCommand("/structure load chest:chest_26 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 27:
                    cmdcomp.SetCommand("/structure load chest:chest_27 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 28:
                    cmdcomp.SetCommand("/structure load chest:chest_28 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 29:
                    cmdcomp.SetCommand("/structure load chest:chest_29 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 30:
                    cmdcomp.SetCommand("/structure load chest:chest_30 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 31:
                    cmdcomp.SetCommand("/structure load chest:chest_31 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 32:
                    cmdcomp.SetCommand("/structure load chest:chest_32 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 33:
                    cmdcomp.SetCommand("/structure load chest:chest_33 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 34:
                    cmdcomp.SetCommand("/structure load chest:chest_34 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 35:
                    cmdcomp.SetCommand("/structure load chest:chest_35 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 36:
                    cmdcomp.SetCommand("/structure load chest:chest_36 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 37:
                    cmdcomp.SetCommand("/structure load chest:chest_37 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 38:
                    cmdcomp.SetCommand("/structure load chest:chest_38 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 39:
                    cmdcomp.SetCommand("/structure load chest:chest_39 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 40:
                    cmdcomp.SetCommand("/structure load chest:chest_40 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 41:
                    cmdcomp.SetCommand("/structure load chest:chest_41 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 42:
                    cmdcomp.SetCommand("/structure load chest:chest_42 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 43:
                    cmdcomp.SetCommand("/structure load chest:chest_43 "+ str(x) + " " + str(y) + " " + str(z),i)
                if randomcomp2 == 44:
                    cmdcomp.SetCommand("/structure load chest:chest_44 "+ str(x) + " " + str(y) + " " + str(z),i)
            if randomcomp == 62:#生成大量矿 + 生成烟火
                cmdcomp.SetCommand("/summon minecraft:fireworks_rocket " + str(x) + " " + str(y) + " " + str(z))
                cmdcomp.SetCommand("/summon minecraft:fireworks_rocket " + str(x) + " " + str(y) + " " + str(z))
                cmdcomp.SetCommand("/summon minecraft:fireworks_rocket " + str(x) + " " + str(y) + " " + str(z))
                randomcomp = random.randint(1,64)
                itemDict = {
                    'itemName': 'minecraft:diamond',
                    'count': randomcomp
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(1,64)
                itemDict = {
                    'itemName': 'minecraft:iron_ingot',
                    'count': randomcomp
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(1,64)
                itemDict = {
                    'itemName': 'minecraft:gold_ingot',
                    'count': randomcomp
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))

                randomcomp = random.randint(1,64)
                itemDict = {
                    'itemName': 'minecraft:emerald',
                    'count': randomcomp
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 63:#生成河豚
                cmdcomp.SetCommand("/summon minecraft:pufferfish " + str(x) + " " + str(y) + " " + str(z))
            if randomcomp == 64:#生成马凯
                itemDict = {
                    'itemName': 'minecraft:horsearmorleather',
                    'count': 1
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                itemDict = {
                    'itemName': 'minecraft:horsearmoriron',
                    'count': 1
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                itemDict = {
                    'itemName': 'minecraft:horsearmorgold',
                    'count': 1
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
                itemDict = {
                    'itemName': 'minecraft:horsearmordiamond',
                    'count': 1
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 65:#生成末地门
                randomcomp = random.randint(1,16)
                itemDict = {
                    'itemName': 'minecraft:end_portal_frame',
                    'count': randomcomp
                    }
                itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 66:#生成粘液块小屋
                cmdcomp.SetCommand("/fill ~2 ~-1 ~2 ~-2 ~-1 ~-2 slime",i)
                cmdcomp.SetCommand("/fill ~2 ~2 ~2 ~-2 ~2 ~-2 slime",i)
                cmdcomp.SetCommand("/fill ~-2 ~0 ~2 ~2 ~2 ~2 slime",i)
                cmdcomp.SetCommand("/fill ~-2 ~0 ~-2 ~2 ~2 ~-2 slime",i)
                cmdcomp.SetCommand("/fill ~2 ~0 ~2 ~2 ~2 ~-2 slime",i)
                cmdcomp.SetCommand("/fill ~-2 ~0 ~ ~-2 ~2 ~ slime",i)
            if randomcomp == 67:#生成幸运鸡
                cmdcomp.SetCommand("/summon chicken "+ str(x) + " " + str(y+1) + " " + str(z),i)
            if randomcomp == 68:#生成大量羊毛
                for number in range(0 ,15):
                    randomcomp = random.randint(1,16)
                    itemDict = {
                        'itemName': 'minecraft:wool',
                        'count': randomcomp,
                        'auxValue': number,
                        }
                    itemcomp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
                    itemcomp.SpawnItemToLevel(itemDict, dimension, (x,y,z))
            if randomcomp == 69:#生成幸运剑
                pass
            if randomcomp == 70:#生成幸运弓
                pass

    def Destroy(self):
        self.UnListenEvent()