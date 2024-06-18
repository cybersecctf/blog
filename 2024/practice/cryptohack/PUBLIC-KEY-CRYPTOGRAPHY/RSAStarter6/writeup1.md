
<!DOCTYPE html>
<html>

<body>
    <h1>RSA Starter 6- cryptohack</h1>

    <h2>Challenge Description</h2>
    <p> How can you ensure that the person receiving your message knows that you wrote it?

You've been asked out on a date, and you want to send a message telling them that you'd love to go, however a jealous lover isn't so happy about this.

When you send your message saying yes, your jealous lover intercepts the message and corrupts it so it now says no!

We can protect against these attacks by signing the message.

Imagine you write a message M. You encrypt this message with your friend's public key: C = Me0 mod N0.

To sign this message, you calculate the hash of the message: H(M) and "encrypt" this with your private key: S = H(M)d1 mod N1.

In real cryptosystems, it's <a href="https://crypto.stackexchange.com/a/12138">best practice to use separate keys</a>  for encrypting and signing messages.


Your friend can decrypt the message using their private key: m = Cd0 mod N0. Using your public key they calculate s = Se1 mod N1.

Now by computing H(m) and comparing it to s: assert H(m) == s, they can ensure that the message you sent them, is the message that they received!

Sign the flag crypto{Immut4ble_m3ssag1ng} using your private key and the SHA256 hash function.

The output of the hash function needs to be converted into a number that can be used with RSA math. Remember the helpful bytes_to_long() function that can be imported from Crypto.Util.number.
 </p>
 
    <h2>Solution Approach</h2>
    <p>Here are the steps we took to solve the challenge:</p>
    <ol>
<pre>
 
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">13371337
</p>

    <h2>Conclusion</h2>
    <p>this is a    medium chanllenge for introduce rsa decrypt with n e c</p>
</body>
</html>
