import zipfile,sys,os

def search_zip_files(zip_file, text):
    with zipfile.ZipFile(zip_file, 'r') as myzip:
        for file in myzip.namelist():
            with myzip.open(file, 'r') as myfile:
                try:
                    s = myfile.read().decode('utf-8')
                    print(file)
                    print(s)
                    if text in s:
                        print(f'Found "{text}" in file: {file} inside {zip_file}')
                except UnicodeDecodeError:
                     print("not text",file)
# Replace 'your_zip_file.zip' and 'your_text' with your specific zip file and text
file="TheFlag.zip"
search=""
if len(sys.argv)>1:
   file=sys.argv[1]
if len(sys.argv)>2:
   search=sys.argv[2]
search_zip_files(file, search)

