
import zipfile
import os
def search_text_in_zip(zip_file_path, search_text):
    found_files = []
    content=[]
    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract the contents to a temporary directory
        extract_dir = "./temp_extract"
        zip_ref.extractall(extract_dir)

        # Traverse through the extracted directory
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Check if the file is a text file
                if file_path.endswith('.txt'):#can use for find specicifc file
                    # Open the text file and search for the text
                    with open(file_path, 'r') as f:
                        if search_text in f.read():
                            found_files.append(file_path)
                            content.append(file_path)
    return found_files

# Example usage
zip_file_path = 'big-zip-files.zip'
search_text = 'pico'
found_files = search_text_in_zip(zip_file_path, search_text)
if found_files:
    print("Found in the following files:")
 
    for file in found_files:
        print(file)
        os.system("cat "+file)
else:
    print("Text not found in any files.")
