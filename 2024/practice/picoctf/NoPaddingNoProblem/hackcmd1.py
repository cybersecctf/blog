from sage.all import ZZ

def oracle(c):
    """
    Parity oracle function.
    :param c: the ciphertext
    :return: the last bit of the plaintext
    """
    # Example of a basic parity oracle function
    # For demonstration purposes, we'll assume that the LSB of the plaintext is even
    if c % 2 == 0:
        return 0
    else:
        return 1

def attack(N, e, c, oracle):
    """
    Recovers the plaintext from the ciphertext using the LSB oracle (parity oracle) attack.
    :param N: the modulus
    :param e: the public exponent
    :param c: the encrypted message
    :param oracle: a function which returns the last bit of a plaintext for a given ciphertext
    :return: the plaintext
    """
    left = ZZ(0)
    right = ZZ(N)
    while right - left > 1:
        c = (c * pow(2, e, N)) % N
        if oracle(c) == 0:
            right = (right + left) / 2
        else:
            left = (right + left) / 2

    return int(right)

if __name__ == "__main__":
    # Replace these values with the actual values of N, e, and c
    n = 98524538629006920616866965132508384740762164637286054397513191511896967408143387757541544190507265202059306443031292035065714317238341724495034701641903571428795565294055761442024589901825231845904391209607913732358002320345219099874637281965297127466426574938796920221240984800693094926335824061103985537053
    
    e = 65537
    c = 4891645030297899446429574591326970846046146372144618957809891858829368498078724649071669657458090635019167066205906480552401333302465888983738830944954303109671704749593828302042731270232456812684780666211922809016430579885915688915901353179654616097491120262918876320928131489862082861820920496294629094119

    plaintext = attack(n, e, c, oracle)
    print("Recovered plaintext:", plaintext)
