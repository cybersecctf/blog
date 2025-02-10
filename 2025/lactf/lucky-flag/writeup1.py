
import ast

# Encrypted string (from the JavaScript code)
enc = "\\u000e\\u0003\\u0001\\u0016\\u0004\\u0019\\u0015V\\u0011=\\u000bU=\\u000e\\u0017\\u0001\\t=R\\u0010=\\u0011\\t\\u000bSS\\u001f"

# Convert the string with Unicode escapes into actual characters
decoded = enc.encode('utf-8').decode('unicode_escape')

# XOR each character with 0x62 and convert to the original character
flag = ''.join(chr(ord(c) ^ 0x62) for c in decoded)

# Print the decoded flag
print(f"Decoded Flag: {flag}")

