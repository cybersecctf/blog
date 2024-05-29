#python
import binwalk,os
import sys
sys.path.append('/home/mrrobot/Desktop/blog')  # This is an absolute path
import blog 
def solve(file_path, search_text):
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
if __name__ == "__main__" :
 print("d")
 file=blog.set('test.bin',1)
 search=blog.set('text',2)
 print("d")
 solve(file,search)