
import os
import shutil
from datetime import datetime

from PIL import Image, ExifTags
import ImageMetadataHelper

if __name__=='__main__':
    path = 'D:\\Timelapse3\\'
    copyFile = False

    for root,dirs,files in os.walk(path):
        for  file in files:
            imPath = os.path.join(root, file)
            if (os.path.isfile(imPath)) and file.endswith('.JPG'):
                destPath = ImageMetadataHelper.getDestFolder(imPath,path)
                newImPath = os.path.join(destPath,file)
                shutil.move(imPath,newImPath)