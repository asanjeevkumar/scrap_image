__author__ = 'Sanjeev K Armugam'
import os
import urllib.request
class image_downloader():
    def __init__(self, file_name = 'import.txt', store_loc = '.' ):
        self.import_file_name = file_name
        self.storage_drive = store_loc

    def _validate_import_file(self):

        if(not os.path.isfile(self.import_file_name)):
            raise FileNotFoundError("%s not found."%self.import_file_name)


    def download_files(self):
        self._validate_import_file()

        with open(self.import_file_name) as f:

            for web_file in f.readlines():
                filename = web_file.split('/')[-1]
                try:
                    urllib.request.urlretrieve(web_file, os.path.join(self.storage_drive,filename))
                    print('Downloaded %s'%filename)
                except :
                    print("error in downloading.. %s"%web_file)

        return True

if __name__ == '__main__':

    img_obj = image_downloader()
    img_obj.download_files()