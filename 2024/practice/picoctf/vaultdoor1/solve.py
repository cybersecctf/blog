import re

def extract_password_chars(java_file):
    try:
        with open(java_file, 'r') as file:
            content = file.read()
            # Use regular expression to find lines containing 'password.charAt'
            password_lines = re.findall(r'password\.charAt\((\d+)\)\s*==\s*\'(.)\'', content)
            max_index = max(int(index) for index, _ in password_lines)
            password_chars = [''] * (max_index + 1)  # Initialize array with correct length

            # Extract characters from password lines
            for index, char in password_lines:
                password_chars[int(index)] = char

            return password_chars
    except FileNotFoundError:
        print("Java file not found.")
        return None

def main():
    java_file = "VaultDoor1.java"  # Change this to the path of your Java file
    password_chars = extract_password_chars(java_file)
    s=""
    if password_chars:
        print("Password characters:")
        for i, char in enumerate(password_chars):
            print(f"pass[{i}] = '{char}'")
            s+=char  
    else:
        print("No password characters extracted.")
    print(s) 

if __name__ == "__main__":
    main()
