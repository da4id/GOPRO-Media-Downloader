import requests
from tqdm import tqdm
import pandas as pd
from os import path, listdir
from pathlib import Path

BASE_URL = 'http://10.5.5.9/Videos/DCIM/'
DOWNLOADED_FOLDER = './downloaded'


def getListOfDirs():
    response = requests.get(BASE_URL)
    index = pd.read_html(response.content)[0]
    wantedDirs = []
    for folder in index.Name[2:]:
        print(folder)
        wantedDirs.append(folder)
    return wantedDirs


def getListOfFiles(dirname):
    response = requests.get(path.join(BASE_URL, dirname))
    index = pd.read_html(response.content)[0]
    wantedFiles = []
    for file in index.Name[2:]:
        file_ext = file.split('.')[1]
        if file_ext in ('JPG', 'MP4'):
            wantedFiles.append(file)
    return wantedFiles


def getExistingFiles():
    return listdir(DOWNLOADED_FOLDER)


def downloadFile(directory, file_name):
    print(f'Downloading {file_name}')
    downloaded = requests.get(path.join(BASE_URL, directory, file_name))
    with open(path.join(DOWNLOADED_FOLDER, file_name), 'wb') as f:
        f.write(downloaded.content)
    print(f'Download of {file_name} completed')


def create_download_folder():
    Path(DOWNLOADED_FOLDER).mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    directories = getListOfDirs()
    for directory in directories:
        print("Scan directory:", directory)
        to_download = getListOfFiles(directory)
        create_download_folder()
        alreadyDownloaded = getExistingFiles()
        for current_download in tqdm(to_download):
            if (current_download not in alreadyDownloaded):
                downloadFile(directory, current_download)
