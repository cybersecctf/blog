import zipfile

import os

import os
import stat

def list_files_with_permissions(directory):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            permissions = stat.filemode(os.stat(file_path).st_mode)
            print(f'{permissions} {file_path}')

 
 

# Replace 'your_zip_file.zip' and 'your_text' with your specific zip file and text
list_files_with_permissions('./TheFlag')

