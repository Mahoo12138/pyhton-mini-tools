# 修改图片尺寸
import os
from PIL import Image

def ResizeImage(filein, fileout, width, height, type):
  img = Image.open(filein)
  out = img.resize((width, height),Image.ANTIALIAS) #resize image with high-quality
  out.save(fileout, type)

if __name__ == "__main__":
  path = "./photos/"
  width = 225
  height = 300
  type = 'jpeg'
  for root, dirs, files in os.walk(path):
    for p in files:
      file_name = path +  p
      ResizeImage(file_name, file_name, width, height, type)