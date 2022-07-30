import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, folder):
        href = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder}
        result = requests.put(href, headers=headers, params=params)
        return result


if __name__ == '__main__':
    token = input('Введите токен Яндекса: ')
    folder_name = input('Название для папки: ')
    print(YaUploader(token).create_folder(folder_name))