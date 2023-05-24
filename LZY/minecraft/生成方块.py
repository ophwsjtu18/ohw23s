import mcpi.minecraft as minecraft
#导入mcpi库
import time 
mc = minecraft.Minecraft.create()
#连接我的世界
pos = mc.player.getTilePos()
#获取玩家坐标
# y衡量高度
# 造房子
for i in range(5):
    for j in range(5):
        for m in range(5):
            if 0 < j < 4 and 1<=i<=3 and 1<=m<=3:
                mc.setBlock(pos.x+i,pos.y+j,pos.z+m,0) # 可以去网上查不同物品的id，都是共通的，0指空气
            elif j==0:
                mc.setBlock(pos.x+i,pos.y+j,pos.z+m,42)
            elif j==4:
                mc.setBlock(pos.x+i,pos.y+j,pos.z+m,41)
            elif j<=2 and i==2 and m==4:
                mc.setBlock(pos.x+i,pos.y+j,pos.z+m,0)
            else:
                mc.setBlock(pos.x+i,pos.y+j,pos.z+m,57)
    # time.sleep(0.2)

