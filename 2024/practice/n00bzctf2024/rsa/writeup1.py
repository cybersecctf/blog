
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
import gmpy2
import os,subprocess
def solve(n, e,c):
    blog.islog=True
    message=""
    s= blog.solveup("rsa",n,e,c)
   
    if s==None:
      m, exact = gmpy2.iroot(c, e)
      if exact:
       # Convert the integer to bytes
       message_bytes = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')

       try:
        # Decode the bytes to an ASCII string
        message = message_bytes.decode('ascii')
        return message
       except (UnicodeDecodeError, ValueError):
         return  f"{message} not valid ASCI. for  Coppersmith's attack"
    else:
     return "no rsa attack found here"

if __name__ == "__main__" :
  e = 3
  n = 135112325288715136727832177735512070625083219670480717841817583343851445454356579794543601926517886432778754079508684454122465776544049537510760149616899986522216930847357907483054348419798542025184280105958211364798924985051999921354369017984140216806642244876998054533895072842602131552047667500910960834243
  c = 13037717184940851534440408074902031173938827302834506159512256813794613267487160058287930781080450199371859916605839773796744179698270340378901298046506802163106509143441799583051647999737073025726173300915916758770511497524353491642840238968166849681827669150543335788616727518429916536945395813
  print(solve(n,e,c))
