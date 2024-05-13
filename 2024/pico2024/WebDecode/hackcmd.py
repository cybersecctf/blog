import base64,sys
try:
 a="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMWY4MzI2MTV9"
 if len(sys.argv)>1:
  a = sys.argv[1]
 print(base64.b64decode(a))
except:
 print("not a base 64 nymber")