
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
def solve(encoded_message,symbol_to_number):
 # Define the mapping from symbols to numbers
 
 # Split the encoded message by commas and decode each segment
 decoded_message = []
 for symbol_set in encoded_message.split(','):
    decoded_segment = ''.join(symbol_to_number[symbol] for symbol in symbol_set)
    decoded_message.append(decoded_segment)
 # Join the decoded segments to form the full message
 decoded_message_full = ','.join(decoded_message)
 # Convert the decoded numbers to ASCII characters
 decoded_numbers = [int(num) for num in decoded_message_full.split(',')]
 decoded_chars = [chr(num) for num in decoded_numbers]
 decoded_text = ''.join(decoded_chars)
 return decoded_text
if __name__ == "__main__" :
 # The given encoded message
 encoded_message = blog.set("^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%",1)
 symbol_to_number = blog.set({
    '!': '1',
    '@': '2',
    '#': '3',
    '$': '4',
    '%': '5',
    '^': '6',
    '&': '7',
    '*': '8',
    '(': '9',
    ')': '0'
 },2)
 print(solve(encoded_message,symbol_to_number))
</pre>
    </ol>
<br>
    <h2>Flag</h2>
    <p class="flag">picoCTF{more_than_m33ts_the_3y3657BaB2C}
</p>

    <h2>Conclusion</h2>
    <p>this is a medium chanllenge for work on symbol-to-digit substitution</p>

</body>
</html>
