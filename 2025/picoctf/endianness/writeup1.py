def solve(operation, word, endian_type):
    """
    Encodes or decodes a word based on the specified endian type.

    Parameters:
        operation (str): "encode" or "decode".
        word (str): The word to encode or the encoded hexadecimal string to decode.
        endian_type (str): "little" or "big".

    Returns:
        str: The encoded or decoded result.
    """
    if operation == "encode":
        if endian_type == "little":
            # Encode to little-endian
            return ''.join(f"{ord(word[i]):02X}" for i in range(len(word) - 1, -1, -1))
        elif endian_type == "big":
            # Encode to big-endian
            return ''.join(f"{ord(word[i]):02X}" for i in range(len(word)))
        else:
            raise ValueError("Invalid endian type. Use 'little' or 'big'.")
    elif operation == "decode":
        if endian_type == "little":
            # Decode from little-endian
            hex_pairs = [word[i:i+2] for i in range(0, len(word), 2)]
            chars = [chr(int(hex_pair, 16)) for hex_pair in reversed(hex_pairs)]
            return ''.join(chars)
        elif endian_type == "big":
            # Decode from big-endian
            hex_pairs = [word[i:i+2] for i in range(0, len(word), 2)]
            chars = [chr(int(hex_pair, 16)) for hex_pair in hex_pairs]
            return ''.join(chars)
        else:
            raise ValueError("Invalid endian type. Use 'little' or 'big'.")
    else:
        raise ValueError("Invalid operation. Use 'encode' or 'decode'.")

# Example usage
if __name__ == "__main__":
    word = "hello"
    print(f"Original Word: {word}")

    # Encode to little-endian
    encoded_little = solve("encode", word, "little")
    print(f"Encoded (Little Endian): {encoded_little}")

    # Decode from little-endian
    decoded_little = solve("decode", encoded_little, "little")
    print(f"Decoded (Little Endian): {decoded_little}")

    # Encode to big-endian
    encoded_big = solve("encode", word, "big")
    print(f"Encoded (Big Endian): {encoded_big}")

    # Decode from big-endian
    decoded_big = solve("decode", encoded_big, "big")
    print(f"Decoded (Big Endian): {decoded_big}")