<title>googlectf begginerquest-0000-1</title>
<!DOCTYPE html>
<html>

<body>
    <h1>googlectf begginerquest-0000-1</h1>

    <h2>Challenge Description</h2>
    <p> This one is not exactly caeser but it might be      the key
 <a href="https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/0000/1/message.txt">message.txt</a>
</p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
normally caesar chipher with  key is related to  vigenere cipher
so use this code and get flag
   <pre>
#python
# -v message.txt(ormessage)
import os
import blog
def solve(message,key) :
   text=""   
   if  os.path.isfile(message) :
    with open(message, 'r') as f:
        text = f.read()
   else:
            text=  message
   result = ''
   password = key
   i = 0
   for char in text:
        shift = ord('a') - ord(password[i % len(password)])
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
            i += 1
        else:
            result += char
   return result
if __name__ == "__main__" :
 val=blog.set("Vhi Nixgnije tkplwr zu a tglpcltzasgtmu sldsxatlvisf czrhij. Ik ks e eoig sshhzutmuakgd zwrjkor gf kje Gsejcr gapygr, azitj uwws r uirylv uhmxt mclyw tf gngjygv tlw eevivw mvuseye. WNAK{yek_xikyy_nktl_at}",1)
 key=blog.set("caesar",2) 
 print(solve(val,key))
</pre>
       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">FLAG{get_viggy_with_it}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for  caesar chipher with key and vigenere cipher</p>
</body>
</html>


 