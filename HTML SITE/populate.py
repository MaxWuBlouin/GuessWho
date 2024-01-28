import shutil
import os

src = "blank.jpg"
dst = "IMAGE_OUTPUT"

cmd = 'copy "{src}" "{dst}"'

os.system(cmd)