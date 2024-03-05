
<!DOCTYPE html>
<html>
 
<body>
    <h1>vault-door-1- picoctf2019</h1>

    <h2>Challenge Description</h2>
    <p>This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: 
<a href="https://phantom1ss.github.io/blog/2024/practice/picoctf/vaultdoor1/VaultDoor1.java">VaultDoor1.java</a>
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
        <li> one why is looking at charat code and combine them after picoCTF{ and finish it with }</li>
<code>
    password.length() == 32 &&
               password.charAt(0) == 'd' &&
               password.charAt(29)== '3' &&
               password.charAt(4) == 'r' &&
               password.charAt(2) == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3) == 'c' &&
               password.charAt(17) == '4' &&
</code>   
    another is harder use pyton code for extract password from java file
<pre>
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
</pre>
can use in some other challenge after modify code
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_ff63b0}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on reverse enginering in java with python </p>
</body>
</html>

