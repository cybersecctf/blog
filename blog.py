import ast,sys
def set(val, i=1,alert="usage argument -v"):
  
    if i<=0:
          print("argument value should be more than 0 not",i)
          return        
    a=val
    if len(sys.argv) > i:
        a = sys.argv[i]
    try:
         a = int(a)
    except ValueError:
      if a.startswith("[") and a.endswith("]") and "," in a:
        a = ast.literal_eval(a)  
    if len(sys.argv) ==1:
       if alert=="usage argument -v"    :  
        print(alert+" "+str(i)+"th value") 
       else:
          print(alert)
    return a
 