# # coding=utf-8
import glob
import os

import shutil
from PIL import  Image
import cv2

#
# # print(glob.glob(r'D:\VideoPhotos\sign\*.jpg'))
# path = r'C:\Users\sy\Desktop\user_image'
# images = glob.glob(path + r"\*.jpg")
# for img in images:
#
#     im = Image.open(img)
# print(im.format, im.size, im.mode)
# size = 1224, 1632
# print(size)
# name = os.path.join(path, img)
# im.thumbnail(size)
# im.save(name, 'JPEG')
# print(im.format, im.size, im.mode)

inputfile=r'C:\Users\sy\Desktop\user_input_image'
outputfile=r'C:\Users\sy\Desktop\user_image'
flag=1024*1024

for img in os.listdir(inputfile):
    file_fullname = inputfile + '/' + img
    im = Image.open(file_fullname)
    print(im.format, im.size, im.mode)
    size_tmp = os.path.getsize(file_fullname)
    (x,y)=im.size
    if size_tmp > flag:
        if x>1920:
            x_s=1920
            y_s=int(y*1920/x)
            out = im.resize((x_s, y_s), Image.ANTIALIAS)
            out.save(outputfile + '/' + img)
            print(out.format, out.size, out.mode)

        # if y>1920:
        #     y_s=1920
        #     x_s=int(x*1920/y)
        #     out = im.resize((x_s,y_s), Image.ANTIALIAS)
        #     out.save(outputfile + '/' + img)
        #     print(out.format, out.size, out.mode)
    else:
        shutil.copy(inputfile+ '/'+img, outputfile+ '/'+img)
#size_tmp =os.path.getsize(file_fullname)
#flag=1024*1024
#(x,y)=im.size

#while size_tmp > flag and q > 0:

#size=1920,1080
#out=im.thumbnail(size)
#size_tmp = os.path.getsize(outputfile)
# out = im.resize((x_s,y_s),Image.ANTIALIAS)
# print(out.format,out.size,out.mode)
# out.save(outputfile+'/target.jpg')


