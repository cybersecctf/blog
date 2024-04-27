
import sys,base64
try:
 type="decode"
 text =" R2Vla3NGb3JHZWVrcyBpcyB0aGUgYmVzdA =="
 if len(sys.argv)>1:
     type=sys.argv[1]
 else:
      print("usage -v decode/encode text")
 if len(sys.argv)>2:
    text=sys.argv[2]
 if type=="encode":
  print("encoede base64:",base64_string.encode(text) )
 else:
   print("decoded nase64:",base64.b64decode(base64_bytes) )
 
except Exception as   e:
 print("error:"+str(e))