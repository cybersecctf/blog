<title>Magikarp Ground Mission- picoctf2021</title>

<!DOCTYPE html>
<html>

<body>
    <h1>Magikarp Ground Mission- picoctf2021</h1>

    <h2>Challenge Description</h2>
AUTHOR: MADSTACKS

Description
I've hidden a flag in this file. Can you find it? 
    <a href="https://mercury.picoctf.net/static/9a7436948cc502e9cacf5bc84d2cccb5/Forensics%20is%20fun.pptm">Forensics is fun.pptm</a>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
         remove space in name and convert it   to <a href="https://mercury.picoctf.net/static/9a7436948cc502e9cacf5bc84d2cccb5/Forensicsisfun.pptm">Forensics is fun.pptm</a>
    and see is hidden file use command cat ppt/slideMasters/hidden and get text is like base64 but not complete mode so use this code for get flag from this
<pre>
#python
import base64,sys

def test_base64(string):
    try:
        # Try to decode the string
        base64.b64decode(string)
        # If decoding succeeds, return True
        return True
    except:
        # If decoding fails, return False
        return False

def add_padding(string):
    # Add padding ('=') to the string
    padded_string = string + '=' * ((4 - len(string) % 4) % 4)
    return padded_string

def check_base64_with_padding(string):
    # Check if the string is already valid base64
    if test_base64(string):
        return string
    else:
        # Try adding padding and test if it's valid base64
        padded_string = add_padding(string)
        if test_base64(padded_string):
            return padded_string
        else:
            # If adding padding doesn't work, return None
            return None

# Test the function with your string
base64_string = "Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q"
if len(sys.argv)>1:
       base64_string=sys.argv[1]
# Remove spaces from the string
base64_string = base64_string.replace(" ", "")
# Check if the string is valid base64 with padding
valid_base64 = check_base64_with_padding(base64_string)
if valid_base64:
    print("Valid base64 string and text:", valid_base64, base64.b64decode(valid_base64))
else:
    print("Not a valid base64 string.")

</pre> 
after run can get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{D1d_u_kn0w_ppts_r_z1p5}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for search on pptm and decrypt b</p>
</body>
</html>


