import sys
import os
import math

def resource_path(relative_path): # Needed for when I compile the game into an exe
    try: base_path = sys._MEIPASS
    except Exception: base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

resolution = resX, resY = 640,480
halfWidth,halfHeight = resX//2,resY//2
fps = 30

tilesize = 12

sensitivity = 0.1

fov = 90
half_fov = 45
quality = 3
castedRays = {1:80,2:160,3:320}
half_rays = castedRays[quality] // 2
stepAngle = fov // castedRays[quality]

screenDist = halfWidth/math.tan(half_fov)
scale = resX // castedRays[quality]
