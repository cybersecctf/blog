 

<!DOCTYPE html>
<html>
 
<body>
    <h1>picoctf2019---glory of garden  Writeup </h1>

    <h2>Challenge Description</h2>
    <p> This garden contains more than it seems.
garden:https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol> 
        <li>after using binawalk and exiftool not working using 

<pre>
import blog
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

def generate_keys(e, s=2048):
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=e,
        key_size=s,
    )

    # Generate public key
    public_key = private_key.public_key()
    return private_key, public_key

def write_keys_to_files(private_key, public_key, private_key_file, public_key_file):
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

def read_keys_from_files(private_key_file, public_key_file):
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
def sign_and_encrypt_file(private_key, recipient_public_key, input_file, output_file):
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

    # Encrypt the signed message
    encrypted_message = recipient_public_key.encrypt(
        signature + message,
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
def sign_message(private_key, message):
    # Sign the message
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    # Verify the signature
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature verified!")

def solve(search="", file=""):
    if search == "generate keys":
        private_key, public_key = generate_keys(65537)
        write_keys_to_files(private_key, public_key, "private_key.pem", "public_key.pem")
        print("Keys generated and written to files.")
    
    elif search == "sign file":
        private_key, public_key = read_keys_from_files("private_key.pem", "public_key.pem")
        with open(file, "rb") as f:
            message = f.read()
        signature = sign_message(private_key, message)
        with open(file + ".sig", "wb") as f:
            f.write(signature)
        print("File signed and signature written to file.")
    elif search == "read keys":
        private_key, public_key = read_keys_from_files("private_key.pem", "public_key.pem")
        print("Keys read from files.")
    else:
        print("Invalid search parameter.")
if __name__ == "__main__" :
 # Example usage
 #solve("generate keys")
 #solve("sign file", "example.txt")
 #solve("read keys")
 private_key, public_key = read_keys_from_files("private_key.pem", "public_key.pem")
 sign_and_encrypt_file(private_key, public_key, "example.txt", "encrypted_file.gpg")
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{more_than_m33ts_the_3y3657BaB2C}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for work on develper tools in in chrome and web exploitations</p>

</body>
</html>
