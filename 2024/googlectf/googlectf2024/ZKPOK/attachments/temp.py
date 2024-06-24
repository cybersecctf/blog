import hashlib
import json
import socket
from math import gcd
from multiprocessing import Pool, cpu_count

# Assuming the values of n0 and c0 are given or read from param.py
n0 = 24171281203618227646148614093741897893680590469429862763616651018126182178291141461695534191580515360668625075973491504098523699503259361006971705744958883528932688017993492125655911982492437672677101525815537367543196148286955989998259443227022039948657202846637063972174783694852385201871764707353023520121014358038502097164099583969032343493472077089224564347272106493231739328199151912917075676958849850365616848259436125246050967067344589874063605862103771405549833253395136355961700736614256786908493838913193974834129994601312274562117378906031845836444184578865241200802323432200853511029948808442048002259291
c0 = 23600182227273910099358133594372912582919773199179273829828839557230117943609831825595573879341287133068072066324938879830422663107123488440813527886386741421937058370424389567240063193684312982625133480552982946713492184295067725675638844460661211302254449106480853610767961560376504492963755391502378330793274144402415466915344455650158737984908963924569120855971997414861671220011328054765928819282790122661223003302402664231552404933606540838530514595095462530045601820409339363585308908617319725609553274552355183460158759550133568592098227630339064730597534042467707370525507516032057789381741420573605038396418

def hash(s):
    m = b''
    for si in s:
        sib = int.to_bytes(si, (int(si).bit_length() + 7) // 8, 'big')
        sil = int.to_bytes(len(sib), 2, 'big')
        m += sil
        m += sib
    return hashlib.md5(m).digest()

def verify(n, c, proof):
    s = proof.get('s')
    z = proof.get('z')
    h = int.from_bytes(hash(s), 'big')
    b = [(h >> i) & 1 for i in range(127, -1, -1)]
    if len(s) != 128 or len(z) != 128 or len(b) != 128:
        return False

    for si, zi, bi in zip(s, z, b):
        if pow(zi, 2, n) != si * pow(c, bi, n) % n:
            return False
    
    return True

def generate_proof(n, c, start, step):
    si = start
    while si < n:
        zi = pow(si, (n + 1) // 4, n)  # Calculate zi based on Rabin cryptosystem properties
        s = [si] * 128
        z = [zi] * 128
        proof = {'n': n, 'c': c, 's': s, 'z': z}
        if verify(n, c, proof):
            return proof
        si += step
    return None

def parallel_generate_proof(n, c):
    pool = Pool(cpu_count())
    results = []
    for i in range(cpu_count()):
   
        result = pool.apply_async(generate_proof, args=(n, c, i, cpu_count()))
        print(i,result)
        results.append(result)
    
    pool.close()
    pool.join()
    
    for result in results:
        proof = result.get()
        if proof is not None:
            return proof
    
    return None

def send_proof(proof, address, port):
    proof_json = json.dumps(proof) + '\n'
    print("s",proof) 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((address, port))
        data = s.recv(4096)
        print(data.decode())  # Print server's initial message

        s.sendall(proof_json.encode())
        data = s.recv(4096)
        print(data.decode())  # Print server's response

def main():
    # Server address and port
    address = 'zkpok.2024.ctfcompetition.com'
    port = 1337
    
    # Generate the proof
    proof = parallel_generate_proof(n0, c0)

    # Send the proof to the server
    send_proof(proof, address, port)

if __name__ == '__main__':
    main()
