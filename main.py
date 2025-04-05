from tqdm import tqdm
from goproDownloadHelper import GoProDownloadHelper
import os
import ImageMetadataHelper
import shutil

destPath = 'D:\\Timelapse4\\'

if __name__ == '__main__':
    downloadHelper = GoProDownloadHelper()
    directories = downloadHelper.getListOfDirs()
    for directory in directories:
        print("Scan directory:", directory)
        to_download = downloadHelper.getListOfFiles(directory)
        downloadHelper.create_download_folder()
        alreadyDownloaded = downloadHelper.getExistingFiles()
        for filename in tqdm(to_download):
            if filename not in alreadyDownloaded:
                imPath = downloadHelper.downloadFile(directory, filename)

                if os.path.isfile(imPath):
                    try:
                        copyFile = ImageMetadataHelper.creatonDateInRange(imPath, 7, 18)
                    except:
                        copyFile = False
                    if copyFile:
                        print(imPath, "copy")
                        newImPath = os.path.join(ImageMetadataHelper.getDestFolder(imPath, destPath), filename)
                        shutil.copy(imPath, newImPath)
