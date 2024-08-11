
import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
# Generate RSA private and public keys
def generate_keys(e=65537, s=2048):
    try:
        # Generate private key
        private_key = rsa.generate_private_key(
            public_exponent=e,
            key_size=s,
        )

        # Generate public key
        public_key = private_key.public_key()
        return private_key, public_key
    except Exception as e:
        print(f"An error occurred during key generation: {e}")

# Write the private and public keys to files
def write_keys_to_files(private_key, public_key, private_key_file, public_key_file):
    try:
        # Write private key to file
        with open(private_key_file, "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

        # Write public key to file
        with open(public_key_file, "wb") as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
    except Exception as e:
        print(f"An error occurred while writing keys to files: {e}")

# Read the private and public keys from files
def read_keys_from_files(private_key_file, public_key_file):
    try:
        # Read private key from file
        with open(private_key_file, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
            )

        # Read public key from file
        with open(public_key_file, "rb") as f:
            public_key = serialization.load_pem_public_key(
                f.read(),
            )

        return private_key, public_key
    except Exception as e:
        print(f"An error occurred while reading keys from files: {e}")
        return None, None

# Sign and encrypt a file
def sign_and_encrypt_file(private_key, recipient_public_key, input_file, output_file):
    try:
        # Read the file content
        with open(input_file, "rb") as f:
            message = f.read()

        # Sign the message
        signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        # Combine the signature and message
        signed_message = signature + message

        # Encrypt the signed message
        encrypted_message = recipient_public_key.encrypt(
            signed_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Write the encrypted message to the output file
        with open(output_file, "wb") as f:
            f.write(encrypted_message)

        print(f"File '{input_file}' signed, encrypted, and saved to '{output_file}'.")
    except Exception as e:
        import traceback
        print(f"An error occurred during signing and encryption: {e}")
        traceback.print_exc()

def hybrid_encrypt_file(private_key, recipient_public_key, input_file, output_file):
    try:
        # Read the file content
        with open(input_file, "rb") as f:
            message = f.read()

        # Sign the message
        signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        # Generate a random AES key
        aes_key = os.urandom(32)  # AES-256 key size

        # Encrypt the message using AES
        iv = os.urandom(16)  # AES block size for IV is 16 bytes
        cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_message = encryptor.update(signature + message) + encryptor.finalize()

        # Encrypt the AES key with RSA
        encrypted_aes_key = recipient_public_key.encrypt(
            aes_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Write the encrypted AES key and the encrypted message to the output file
        with open(output_file, "wb") as f:
            f.write(encrypted_aes_key + iv + encrypted_message)

        print(f"File '{input_file}' signed, encrypted with AES, and saved to '{output_file}'.")
    except Exception as e:
        import traceback
        print(f"An error occurred during hybrid encryption: {e}")
        traceback.print_exc()

# Main function to demonstrate the usage of the above functions
def solve(search="", file=""):
    if search == "generate keys":
        private_key, public_key = generate_keys()
        write_keys_to_files(private_key, public_key, "private_key.pem", "public_key.pem")
        print("Keys generated and written to files.")
    
    elif search == "sign file":
        private_key, public_key = read_keys_from_files("private_key.pem", "public_key.pem")
        if private_key is not None and public_key is not None:
            with open(file, "rb") as f:
                message = f.read()
            signature = private_key.sign(
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            with open(file + ".sig", "wb") as f:
                f.write(signature)
            print(f"File '{file}' signed and signature written to '{file}.sig'.")
        else:
            print("Failed to read keys from files.")
    
    elif search == "read keys":
        private_key, public_key = read_keys_from_files("private_key.pem", "public_key.pem")
        if private_key is not None and public_key is not None:
            print("Keys read from files successfully.")
        else:
            print("Failed to read keys from files.")
    
    else:
        print("Invalid search parameter.")

# Example usage
if __name__ == "__main__":
   search=blog.set("generate keys",1)
   file=blog.set("example.txt",2)
   solve(search,file)
   # solve("generate keys")
    #solve("sign file", "example.txt")
    #solve("read keys")
    #private_key, public_key = read_keys_from_files("private_key.pem", "public_key.pem")
    #if private_key is not None and public_key is not None:
       # hybrid_encrypt_file(private_key, public_key, "example.txt", "encrypted_file.gpg")
    #else:
     #   print("Failed to proceed with signing and encryption due to key errors.")
