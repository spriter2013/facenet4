from imutils import paths
def get_imgPath(path):
    imagePaths = sorted(list(paths.list_images(path)))
    #print(imagePaths)
    i = 0
    for img_name in imagePaths:
         print(img_name)

         with open("path.txt", "a") as f:
            i += 1
            print(i)
            #print(imagePaths)
            f.write(img_name)
            f.write('\n')
    return imagePaths

pathss = 'E:\\研究生\\face\\facenet 测试程序\\裁剪后图片'

get_imgPath(pathss)