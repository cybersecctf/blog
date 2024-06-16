
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import utils

# Generate RSA keys for Alice and Bob
alice_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
alice_public_key = alice_private_key.public_key()

bob_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
bob_public_key = bob_private_key.public_key()

# Function to serialize and deserialize keys for demonstration
def serialize_public_key(pub_key):
    return pub_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

def deserialize_public_key(pem_pub_key):
    return serialization.load_pem_public_key(pem_pub_key)

def solve(operation, value, user):
    if user == "alice":
        pub_key = alice_public_key
        priv_key = alice_private_key
    elif user == "bob":
        pub_key = bob_public_key
        priv_key = bob_private_key
    else:
        raise ValueError("Invalid user. Use 'alice' or 'bob'.")
    
    if operation == "encrypt":
        # Encrypt the message with the user's public key
        encrypted_message = pub_key.encrypt(
            value,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_message
    elif operation == "decrypt":
        # Decrypt the message with the user's private key
        decrypted_message = priv_key.decrypt(
            value,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_message.decode()
    elif operation == "sign":
        # Sign the message with the user's private key
        signature = priv_key.sign(
            value,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
    elif operation == "verify":
        # Verify the message with the user's public key
        signature, message = value
        try:
            pub_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False
    else:
        raise ValueError("Invalid operation. Use 'encrypt', 'decrypt', 'sign', or 'verify'.")
if __name__ == "__main__" :
 # Example usage
 alice_message = b"Hello, Bob! This is a secret message from Alice."
 # Alice encrypts the message using Bob's public key
 encrypted_message = solve("encrypt", alice_message, "bob")
 print("Encrypted message:", encrypted_message)
 # Bob decrypts the message using his private key
 decrypted_message = solve("decrypt", encrypted_message, "bob")
 print("Decrypted message:", decrypted_message)
 # Bob sends a reply to Alice
 bob_message = b"Hello, Alice! I received your message."
 # Bob encrypts the message using Alice's public key
 encrypted_reply = solve("encrypt", bob_message, "alice")
 print("Encrypted reply:", encrypted_reply)
 # Alice decrypts the reply using her private key
 decrypted_reply = solve("decrypt", encrypted_reply, "alice")
 print("Decrypted reply:", decrypted_reply)
 # Alice signs a message
 signature = solve("sign", alice_message, "alice")
 print("Signature:", signature)
 # Bob verifies the signature
 is_valid = solve("verify", (signature, alice_message), "alice")
 print("Signature valid:", is_valid)
 # Modify the message to simulate tampering
 tampered_message = b"Hello, Bob! This is a tampered message from Alice."
 # Bob verifies the tampered message
 is_valid_tampered = solve("verify", (signature, tampered_message), "alice")
 print("Tampered signature valid:", is_valid_tampered)

