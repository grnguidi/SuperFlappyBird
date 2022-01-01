from os import environ
from sys import platform as sys_plat

fps = 60

screen_width = 480
screen_height = 854
tile_size = 64
player_size = 48

# enviroment settings
def platform():
    if 'ANDROID_ARGUMENT' in environ:
        return "android"
    elif sys_plat in ['linux', 'linux32', 'linux3']:
        return "linux"
    elif sys_plat in ['win32', 'cygwin']:
        return "win"

if platform()=="android":
    path="/data/data/org.game.supfb/files/app/"
elif platform()=="linux":
    path="./"

