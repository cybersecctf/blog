
from collections import Counter
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog

calpha = []
dalpha=[]

# Function to get frequency of each letter in the ciphertext
def getfrequency(ciphertext):
    # Clean up the ciphertext to only include letters
    cleaned_ciphertext = ''.join(filter(str.isalpha, ciphertext))
    # Count the frequency of each letter
    frequency = Counter(cleaned_ciphertext)
    return frequency

# Function to replace letters in ciphertext according to a mapping using placeholders
def replacebyword(ciphertext, word1, word2, ismapped):
    
    # Ensure the letters to be replaced are in uppercase
    ciphertext = ciphertext.upper()
    word1 = word1.upper()
    word2 = word2.upper()
    # Create a temporary placeholder for each letter to be replaced
    placeholders = [chr(i + 256) for i in range(len(word1))]
    
    # First pass: replace each letter in word1 with its corresponding placeholder
    for i in range(len(word1)):
        if not ismapped[ord(word1[i])]:
            ciphertext = ciphertext.replace(word1[i], placeholders[i])
            ismapped[ord(word1[i])] = True
    
    # Second pass: replace each placeholder with the corresponding letter in word2
    for i in range(len(word2)):
        ciphertext = ciphertext.replace(placeholders[i], word2[i])
    
    return ciphertext

# Function to set the mapping and replace letters accordingly
def mapping( word1, word2):   
 for i in range(len(word1)):
   if word1[i] not in calpha:
       calpha.append(word1[i])
       dalpha.append(word2[i])
def solve(ciphertext):
    s=[] 
    found=False   
    mapping("MIT","the")#add more by own to reach foull alphabet like below          
    mapping( "TAMLOGFKISREHDWCYZBUXQJVNP", "eatsionrhldcpmuwfbygvkqxz ")
    mapping("MIT","the")#add more by own to reach foull alphabet like below          
    print(calpha)               
    for i in range(len(ciphertext)):
      found=False
      for j in range(len(calpha)):   
        if ciphertext[i]==calpha[j]:
           s.append(dalpha[j]) 
           found=True
      if not found:
        s.append(ciphertext[i])                
    return "".join(s)
# Main execution
if __name__ == "__main__":
    blog.solveup("inspect","https://www.dcode.fr/monoalphabetic-substitution","") #if site not work use code for mapping and run flag
    
    ciphertext = blog.solveup("read file", "Substitution.txt", "")
    ciphertext = blog.set(ciphertext, 1)
    ciphertext=solve(ciphertext)
    print(ciphertext)
 

