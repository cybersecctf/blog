import base64,sys
try:
 a="QmVwUksrcGs5RFU5UmJBVlpLVWRLbFRGb01DVHFKYy9aQVBTZlFlcDl4a3h6cExYZlFpRFlJK1REd2h6Z3pxTm1xM1VYdStFcjVSbWp2QTJpOHRxa0g4VTM3YkJuaUp1b0ozUzJnWHluU2hVUkJ2ckxSNzFLY0VhSFJqcmpKaCs="
 if len(sys.argv)>1:
  a = sys.argv[1]
 print(base64.b64decode(a))
except:
 print("not a base 64 nymber")