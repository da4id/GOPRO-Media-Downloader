from os import path, listdir
from pathlib import Path

import pandas as pd
import requests

class GoProDownloadHelper:

    def __init__(self, baseUrl='http://10.5.5.9/Videos/DCIM/', downloadFolder='./downloaded'):
        self.baseUrl = baseUrl
        self.downloadFolder = downloadFolder

    def getListOfDirs(self):
        response = requests.get(self.baseUrl)
        index = pd.read_html(response.content)[0]
        wantedDirs = []
        for folder in index.Name[2:]:
            print(folder)
            wantedDirs.append(folder)
        return wantedDirs

    def getListOfFiles(self, dirname):
        response = requests.get(path.join(self.baseUrl, dirname))
        index = pd.read_html(response.content)[0]
        wantedFiles = []
        for file in index.Name[2:]:
            file_ext = file.split('.')[1]
            if file_ext in ('JPG', 'MP4'):
                wantedFiles.append(file)
        return wantedFiles

    def getExistingFiles(self):
        return listdir(self.downloadFolder)

    def downloadFile(self, directory, file_name):
        while True:
            try:
                print(f'Downloading {file_name}')
                p = path.join(self.downloadFolder, file_name)
                downloaded = requests.get(path.join(self.baseUrl, directory, file_name))
                with open(p, 'wb') as f:
                    f.write(downloaded.content)
                print(f'Download of {file_name} completed')
                return p
            except:
                pass

    def create_download_folder(self):
        Path(self.downloadFolder).mkdir(parents=True, exist_ok=True)
