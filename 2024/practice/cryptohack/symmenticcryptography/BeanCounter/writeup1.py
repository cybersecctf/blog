
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
#python
enc=blog.solveup("strings files","enc")
png_hdr = bytes([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x00, 0x00, 0x00, 0x0d, 0x49, 0x48, 0x44, 0x52])
encrypted = bytes.fromhex(enc)

keystream = []
for i in range(len(png_hdr)):
    keystream.append(png_hdr[i] ^ encrypted[i])

print(keystream)

png = [0]*len(encrypted)
for i in range(len(encrypted)):
    png[i] = encrypted[i] ^ keystream[i%len(keystream)]

with open('bean_counter.png', 'wb') as fd:
    fd.write(bytes(png))
