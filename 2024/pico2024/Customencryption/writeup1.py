def generator(g, x, p):
    return pow(g, x) % p
p = 97
g = 31
a = 97
b = 22
enc =  [151146, 1158786, 1276344, 1360314, 1427490, 1377108, 1074816, 1074816, 386262, 705348, 0, 1393902, 352674, 83970, 1141992, 0, 369468, 1444284, 16794, 1041228, 403056, 453438, 100764, 100764, 285498, 100764, 436644, 856494, 537408, 822906, 436644, 117558, 201528, 285498]


text_key = "trudeau"

u = generator(g, a, p)
v = generator(g, b, p)
key = generator(v, a, p)
b_key = generator(u, b, p)

assert key == b_key

# rev encrypt()

enc1 = ''
for n in enc:
	enc1 += chr(n // (key*311))

print(f'{enc1 = }')


# rev dynamic_xor_encrypt()

dec = ''
for i, char in enumerate(enc1[::-1]):
	key_char = text_key[(len(enc1) - i - 1) % len(text_key)]
	decrypted_char = chr(ord(char) ^ ord(key_char))
	dec += decrypted_char
	
print(dec)