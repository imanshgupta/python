# 3 ways to imporrt packages
from package.level1.p1 import *
from package.level1.level2.p2 import subtract
# in direct import we need to start from bottom to call a fun
import level1.level2.p2
print(level1.level2.p2.subtract(200, 100))
print(subtract(200, 100))
