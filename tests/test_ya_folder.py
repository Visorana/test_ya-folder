import unittest
from main import YaUploader


class TestYaFolder(unittest.TestCase):

    def test_created_folder(self, disk):
        disk = YaUploader(token).create_folder('folder_1')
        self.assertEqual(disk.status_code, 201)

    def test_existed_folder(self, disk):
        disk = YaUploader(token).create_folder('folder_1')
        self.assertEqual(disk.status_code, 409)

    def test_failed_access(self, disk):
        disk = YaUploader(wrong_token).create_folder('folder_2')
        self.assertEqual(disk.status_code, 401)






