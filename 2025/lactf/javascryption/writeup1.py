import base64
import urllib.parse


def solve(encrypted_flag = "JTNEJTNEUWZsSlglNUJPTERfREFUQSU1RG85MWNzeFdZMzlWZXNwbmVwSjMlNUJPTERfREFUQSU1RGY5bWI3JTVCT0xEX0RBVEElNURHZGpGR2I="):
 # Reverse the operations step by step
 # Step 1: Base64 decode
 step1 = base64.b64decode(encrypted_flag).decode('utf-8')
 # Step 2: URL decode
 step2 = urllib.parse.unquote(step1)
 # Step 3: Replace "[OLD_DATA]" with "Z"
 step3 = step2.replace("[OLD_DATA]", "Z")
 # Step 4: Reverse the string
 step4 = step3[::-1]
 # Step 5: Base64 decode again
 original_flag = base64.b64decode(step4).decode('utf-8')
 return original_flag
# Output the flag
if __name__=='__main__':
 print(f"Flag: {solve()}")
