import base64

def xor_hex_strings(hex_str1, hex_str2):
    # Convert hex strings to bytes
    bytes1 = bytes.fromhex(hex_str1)
    bytes2 = bytes.fromhex(hex_str2)
    
    # Perform XOR operation between bytes
    xor_result = bytes(x ^ y for x, y in zip(bytes1, bytes2))
    
    # Convert result back to hex string
    return xor_result.hex()

# Example usage:
base64_str1 = "bWqznPKmVMkt0Obu8bAINKvcBYpurA2yC0NKkUTXWw24Y8AtW9eK9+zipS2Cs6qBHDF7Jpn4z2jm2iT/RWXw6QbQgNb2Ty64i5IuVZxpHsZ6GGr860eM7g=="
base64_str2 = "dmrn1eTjXYw8y+bIx4V4buP0UcJ8qhG+X3hGnFiSTFiJZskgTI7Tssv9uDeE/b+QGjVsZdX63X28k0rfanPYvBrFjaL2UWucmIMLX+lyEtZtHGD26EmF9g=="

# Convert base64 strings to hex strings
hex_str1 = base64.b64decode(base64_str1).hex()
hex_str2 = base64.b64decode(base64_str2).hex()

# Perform XOR operation between hex strings
xor_result = xor_hex_strings(hex_str1, hex_str2)
print(xor_result)
