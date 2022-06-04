import os
import requests
from pprint import pprint

BASE_PATH = os.getcwd()
filename = 'test1.txt'
file_path = os.path.join(BASE_PATH, filename)

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, yadisk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": yadisk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, yadisk_file_path, file_path):
        href = self._get_upload_link(yadisk_file_path=yadisk_file_path).get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл успешно загружен')

if __name__ == '__main__':
    path_to_file = file_path
    TOKEN = ' '
    ya = YaUploader(token=TOKEN)
    result = ya.upload_file_to_disk(filename, path_to_file)