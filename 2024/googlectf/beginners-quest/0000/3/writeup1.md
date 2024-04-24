<!DOCTYPE html>
<html>

<body>
    <h1>googlectf beginnersquest-0000-3</h1>

    <h2>Challenge Description</h2>
    <p>This tricky one introduces  Transposition

   <a href="https://cybersecctf.github.io/blog/2024/googlectf/beginners-quest/0000/3/message.txt">message.txt</a>                                       
</p>
 
    <h2>Solution Approach</h2>
    
    <ol>
a transposition cipher (also known as a permutation cipher) is a method of encryption which scrambles the positions of characters (transposition) without changing the characters themselves. Transposition ciphers reorder units of plaintext (typically characters or groups of characters) according to a regular system to produce a ciphertext which is a permutation of the plaintext.see more  <a href="https://en.wikipedia.org/wiki/Transposition_cipher">here....</a>we run this code
<pre>
def read_file(text: str) -> str:
  try:     
    with open(text, 'rb') as f:
        # read special characters
        text = f.read().decode('utf-8')
            
  except:      
     text=text
  return text

def getcolumns(text: str, columns: int) -> str:
    result = ''
    rows = [''] * (len(text)//columns)
    for i in range (len(text)//columns):
        for j in range (columns):
            rows[i] += text[i + j * (len(text)//columns)]

    for row in rows:
        result += row + '\n'
    return result



file_path ='message.txt'
print(getcolumns(read_file(file_path), 6))
</pre>
 we get a lot words.Notice the line FG␣L{A, this is probably ␣FLAG{. We can now use this to figure out the ordering key. The first character should be ␣, which is column 2. The second character should be F, which is column 0. The third character should be L, which is column 3. And so on.
The final key is 2 0 3 5 1 4.
Let's modify our Python script to reorder the columns:
<pre>
#python3
def read_file(text: str) -> str:
  try:     
    with open(text, 'rb') as f:
        # read special characters
        text = f.read().decode('utf-8')
            
  except:      
     text=text
  return text
def detranspose(text: str, columns: int) -> str:
    result = ''
    rows = [''] * (len(text)//columns)
    for i in range (len(text)//columns):
        for j in range (columns):
            rows[i] += text[i + j * (len(text)//columns)]

    for row in rows:
        # change order 2, 0, 3, 5, 1, 4
        result += row[2]
        result += row[0]
        result += row[3]
        result += row[5]
        result += row[1]
        result += row[4]
    return result



file_path = 'message.txt'
print(detranspose(read_file(file_path), 6).replace('␣', ' '))
def read_file(text: str) -> str:
  try:     
    with open(text, 'rb') as f:
        # read special characters
        text = f.read().decode('utf-8')
            
  except:      
     text=text
  return text
</pre>       
    after run code will get flag
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">FLAG{caesar_would_have_liked_these_columns}
</p>

    <h2>Conclusion</h2>
    <p>this is a very   easy chanllenge for caesar chipher   transposition  </p>
</body>
</html>


 
