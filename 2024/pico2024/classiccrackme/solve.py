secret1 = 85
secret2 = 51
secret3 = 15
fix = 97

def encode_text(input1, secret1, secret2, secret3, fix, i_0):
    for t in range(65, 125):
        input_val = t
        for i in range(3):
            random1 = (secret1 & (i_0 % 255)) + (secret1 & ((i_0 % 255) >> 1))
            random2 = (random1 & secret2) + (secret2 & (random1 >> 2))
            x = ((random2 & secret3) + input_val - fix + (secret3 & (random2 >> 4))) 
            if x < 0:
                input_val = x + fix
            else:
                input_val = x % 26 + fix
        if input_val == input1:
            print(chr(t), end="")
            break

output = "mpknnphjngbhgzydttvkahppevhkmpwgdzxsykkokriepfnrdm"

for i_0 in range(len(output)):
    encode_text(ord(output[i_0]), 85, 51, 15, 97, i_0)