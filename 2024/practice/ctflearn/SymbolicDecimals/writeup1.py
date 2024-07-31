
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
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
