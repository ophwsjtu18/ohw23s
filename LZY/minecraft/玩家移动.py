from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos = mc.player.getTilePos()
print(pos)
time.sleep(10)
# mc.player.setPos(pos.x,pos.y+50,pos.z)
mc.player.setPos(98,30,234)