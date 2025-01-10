
import os
import shutil
from datetime import datetime

from PIL import Image, ExifTags


def creation_date(path_to_file):
    img = Image.open(path_to_file)
    exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
    return datetime.strptime(exif['DateTime'], '%Y:%m:%d %H:%M:%S')

if __name__=='__main__':
    destPath = 'D:\\Timelapse2\\'
    sourcePath = 'D:\\Projekte\\GOPRO-Media-Downloader\\downloaded\\'
    copyFile = False

    if os.path.isdir(destPath):
        shutil.rmtree(destPath)
    os.mkdir(destPath)

    for root,dirs,files in os.walk(sourcePath):
        for  file in files:
            imPath = os.path.join(root, file)
            if (os.path.isfile(imPath)) and file.endswith('.JPG'):
                createDate = creation_date(imPath)
                copyFile =  7 < createDate.hour < 18

                if (copyFile):
                    print(imPath, createDate.strftime('%d.%m.%y %H:%M:%S'),"copy")
                    shutil.copy(imPath, os.path.join(destPath, file))
                else:
                    print(imPath, createDate.strftime('%d.%m.%y %H:%M:%S'))