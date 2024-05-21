import ast,sys
def set(val, i=1):
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
    return a
 