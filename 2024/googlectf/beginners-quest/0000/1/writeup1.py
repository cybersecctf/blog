
#python
# -v message.txt(ormessage)
import os
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
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
