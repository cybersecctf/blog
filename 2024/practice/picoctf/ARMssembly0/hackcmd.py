decimal_number = 3742084308
hex_string = hex(decimal_number & 0xFFFFFFFF)  # Masking to ensure it's a 32-bit hex string
print(hex_string)