zip_file_path = 'super-secret-files.zip'
search_text = 'utflag'
found_files = search_text_in_zip(zip_file_path, search_text)
if found_files:
    print("Found in the following files:")
 
    for file in found_files:
        print(file)
        os.system("cat "+file)
else:
    print("Text not found in any files.")