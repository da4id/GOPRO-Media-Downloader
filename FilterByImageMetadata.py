
import os
import shutil
from datetime import datetime
import ImageMetadataHelper

from PIL import Image, ExifTags

if __name__=='__main__':
    destPath = 'D:\\Timelapse4\\'
    sourcePath = 'D:\\Projekte\\GOPRO-Media-Downloader\\downloaded\\'
    copyFile = False

    if os.path.isdir(destPath):
        shutil.rmtree(destPath)
    os.mkdir(destPath)

    for root,dirs,files in os.walk(sourcePath):
        for  file in files:
            imPath = os.path.join(root, file)
            if (os.path.isfile(imPath)) and file.endswith('.JPG'):
                copyFile = ImageMetadataHelper.creatonDateInRange(imPath, 7, 18)

                if (copyFile):
                    dst = ImageMetadataHelper.getDestFolder(imPath, destPath)
                    newImPath = os.path.join(dst, file)
                    shutil.copy(imPath, newImPath)
