import sys,base64
try:
 type="decode"
 text =" VGhlIFZlbm9uYSBwcm9qZWN0IHdhcyBhIFVuaXRlZCBTdGF0ZXMgY291bnRlcmludGVsbGlnZW5jZSBwcm9ncmFtIGluaXRpYXRlZCBkdXJpbmcgV29ybGQgV2FyIElJLg=="
 if len(sys.argv)>1:
     type=sys.argv[1]
 else:
      print("usage -v decode/encode text")
 if len(sys.argv)>2:
    text=sys.argv[2]
 if type=="encode":
  sample_string_bytes = text.encode("ascii") 
  base64_bytes = base64.b64encode(sample_string_bytes) 
  print( "encoded in base64:",base64_bytes.decode("ascii") )
 else:
   base64_bytes = text.encode("ascii") 
   print("decoded from base64:",base64.b64decode(base64_bytes) )
 
except Exception as   e:
 print("error:"+str(e))