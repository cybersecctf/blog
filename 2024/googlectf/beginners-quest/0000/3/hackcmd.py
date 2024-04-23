
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