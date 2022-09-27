import os
from datetime import *

stats = os.stat("jay.txt")
print("file size in byte:", stats.st_size)
print("file last accessed:", stats.st_atime)
print("file last accessed:", datetime.fromtimestamp(stats.st_atime))
print("file last modified:", stats.st_mtime)
