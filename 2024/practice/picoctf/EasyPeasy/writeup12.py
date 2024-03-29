key_location=0
KEY_FILE="key"
FLAG_FILE="flag"
flag = open(FLAG_FILE).read()
 
kf = open(KEY_FILE, "rb").read()
start = key_location
stop = key_location + len(flag)
key = kf[start:stop]
key_location = stop
result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
print("This is the encrypted flag!\n{}\n".format("".join(result)))