<title>crypto/winter- dicectf2024</title>

<!DOCTYPE html>
<html>

<body>
    <h1>crypto/winter- dicectf2024</h1>

    <h2>Challenge Description</h2>
    <p> A simple implementation of the Winternitz signature scheme.

nc mc.ax 31001
</p>

    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
   The scheme is a Winternitz signature. It should used only to sign a single message but here we are allowed to sign two of them. The message is hashed with SHA256. Then each byte is taken individually and interpreted as integer $n_0, n_1, …, n_{256}$
Each private key $q_0, q_1, …, q_{256}$ is iteratively hashed to obtain the signature $s_0, s_1, …, s_{256}$:
$$s_i = H^{256-n_i}(q_i)$$
The first signature is returned to us. Thus if we are able to find two messages $m_1$ and $m_2$ such that each bytes of the hash $h_1$ of $m_1$ are less than each bytes of the hash $h_2$ of $m_2$ we can forge a new signature by computing:
$$\tilde{s_i} = H^{\tilde{n_i}-n_i}(s_i)$$
To find such message I decided to used Bitcoin blocks which have a lot of null bytes, it would allow to reduce the search space. Then I iterated over bitcoin blocks until I found one with a maximum byte value not too high:
 
<pre>

for i in range(828930,0,-1):
    height = i
    url = "https://blockchain.info/block-height/" + str(height) + "?format=json"
    response = json.loads(urlopen(url).read())
    h = bytes.fromhex(response['blocks'][0]['hash'])
    print(h.hex())
    print(max(list(h)))
</pre>

It turns out that block 000000000000000000035796cb87b186324e5b0620312c413b9472895f302667 was a good candidate. I found the corresponding message with a tool I wrote previously:
<pre> 
python bitcoinHash.py -v -u  https://blockchain.info/rawblock/000000000000000000035796cb87b186324e5b0620312c413b9472895f302667

7d72cd3f54b8764df2a80a5253dbef5a9a7faf0329aa4664c30aaac5cbb0c4d5
6726305f8972943b412c3120065b4e3286b187cb965703000000000000000000
</pre>

Then we need to find another message with the each hash byte bigger the the previous hash:
<pre>
 

m2 = bytes.fromhex("7d72cd3f54b8764df2a80a5253dbef5a9a7faf0329aa4664c30aaac5cbb0c4d5")
h1 = sha256(new_m).digest()
i = 0
while True:
    h2 = sha256(i.to_bytes(8)).digest()

    smaller = True
    for b in range(31,-1,-1):
        if h2[b] < h1[b]:
            smaller = False
            break
            
    if smaller:
        print(i.to_bytes(8).hex())
        break
    i += 1

m1 = i.to_bytes(8)


Now from the signature returned by the server we can forge a new signature for our message:

 
chunks = [sig[i:i+32] for i in range(0, len(sig), 32)]    
h1 = hash(m1, 1)
h2 = hash(m2, 1)

m = [i-j for i, j in zip(m1, m2)]
sig = b''.join([hash(x, n) for x, n in zip(chunks, m)])
<pre>

Finally the server accepts the signature and prints the flag:
<pre>b' dice{according_to_geeksforgeeks}\n'
</pre>       
    
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">dice{according_to_geeksforgeeks}
</p>

    <h2>Conclusion</h2>
    <p>this is a crypto chanllenge for work  winter Winternitz signature scheme.</p>
</body>
</html>
