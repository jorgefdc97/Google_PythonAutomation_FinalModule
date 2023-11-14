#!/usr/bin/env python3

from os import listdir
from PIL import Image
import re

#list all the files
for file in listdir("/home/student-02-7e2a3189f672/supplier-data/images"):
#identify .TIFF format
  if (re.search(r"[0-9]\.tiff", file) != None):
#convert file into Image
    print(file)
    image = Image.open("/home/student-02-7e2a3189f672/supplier-data/images/" + file)
#convert file from RGBA to RGB
    image_jpeg = image.convert("RGB")
#change image format
    file_jpeg = re.sub("tiff", "jpeg", file)
    image_jpeg.resize((600,400)).save("/home/student-02-7e2a3189f672/supplier-data/images/"+file_jpeg)
