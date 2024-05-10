import zipfile
import rarfile
import io,os,sys
def extract_and_search(file_path, search_text):
    # Use binwalk to extract files
    for module in binwalk.scan(file_path, signature=True, quiet=False, extract=True):
        print(f"{module.name} Results:")
        for result in module.results:
            print(f"\t{result.file.name}    0x{result.offset:X}    {result.description}")

    # Search for the text in the extracted files
    extracted_dir = file_path + '.extracted'
    for root, dirs, files in os.walk(extracted_dir):
        for file in files:
            with open(os.path.join(root, file), 'r') as f:
                contents = f.read()
                if search_text in contents:
                    print(f"Found '{search_text}' in {file}")
def search_in_zip(zip_path, search_text):
    with zipfile.ZipFile(zip_path, 'r') as myzip:
        for i in myzip.infolist():
            if not i.is_dir() and i.filename.endswith('.txt'):
                with myzip.open(i.filename) as myfile:
                    if search_text in myfile.read().decode():
                        print(f'Found "{search_text}" in {i.filename}')
                         
   

def search_in_rar(rar_path, search_text):
    with rarfile.RarFile(rar_path) as myrar:
        for f in myrar.infolist():
            if not f.isdir() and f.filename.endswith('.txt'):
                with myrar.open(f) as myfile:
                    if search_text in myfile.read().decode():
                        print(f'Found "{search_text}" in {f.filename}')
file="D3EDB.rar"
search=""
type="rar"
if len(sys.argv)>1:
    file=sys.argv[1]
else:
 print("usage file searchtext type(rar/zip/binwalk)")
if len(sys.argv)>2:
    search=sys.argv[2]
if len(sys.argv)>3:
    type=sys.argv[3]  
if type=="rar" or file.endswith("rar"):                                                        
 search_in_rar(file,search)
elif not file.endswith("rar"):
  extract_and_search(file,search)
else:
 search_in_zip(file,search)