
import os
import shutil
from datetime import datetime

from PIL import Image, ExifTags

destPath = 'D:\\Timelapse2\\'

def creation_date(path_to_file):
    img = Image.open(path_to_file)
    exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
    return datetime.strptime(exif['DateTime'], '%Y:%m:%d %H:%M:%S')

def creatonDateInRange(file, fromTime, toTime):
    createDate = creation_date(file)
    return fromTime <= createDate.hour < toTime

def clearAndCreateDestPath():
    if os.path.isdir(destPath):
        shutil.rmtree(destPath)
    os.mkdir(destPath)

def getDestFolder(path_to_file, destPath):
    createDate = creation_date(path_to_file)
    isWeekend = createDate.weekday() >= 5
    destPathNew = destPath + '\\' + createDate.strftime('%Y.%m.%d')
    if isWeekend:
        destPathNew = destPath + '\\' + 'SaSo'
    if not os.path.isdir(destPathNew):
        os.mkdir(destPathNew)
    return destPathNew
