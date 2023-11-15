import os
import time

dirPath = os.path.dirname(__file__)
imagesPath = dirPath + "/static"
files = os.listdir(imagesPath)
files = [el for el in files if ".png" in el]
print(files)
