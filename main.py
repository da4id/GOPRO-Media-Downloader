from tqdm import tqdm
from goproDownloadHelper import GoProDownloadHelper
import os
import ImageMetadataHelper
import shutil

destPath = 'D:\\Timelapse3\\'

if __name__ == '__main__':
    downloadHelper = GoProDownloadHelper()
    directories = downloadHelper.getListOfDirs()
    for directory in directories:
        print("Scan directory:", directory)
        to_download = downloadHelper.getListOfFiles(directory)
        downloadHelper.create_download_folder()
        alreadyDownloaded = downloadHelper.getExistingFiles()
        for current_download in tqdm(to_download):
            if current_download not in alreadyDownloaded:
                imPath = downloadHelper.downloadFile(directory, current_download)

                if os.path.isfile(imPath):
                    copyFile = ImageMetadataHelper.creatonDateInRange(imPath, 7, 18)
                    if copyFile:
                        print(imPath, "copy")
                        shutil.copy(imPath, os.path.join(destPath, current_download))
