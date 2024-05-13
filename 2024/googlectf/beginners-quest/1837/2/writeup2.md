import string,sys
magic = 'ADFGVX'
 
def encode(message, secret_alphabet1,keyword):
   
    # remove duplicate character from keyword -> key
    # keyword = 'checkio' -> key = ['c','h','e','k','i','o']
    key = []
    for c in keyword:
        if c not in key: key.append(c)

    # make sort index -> k
    # keyword = 'cipher' -> k = [0, 4, 3, 2, 1, 2, 5]
    n = len(key)
    k = sorted(range(n), key=lambda i: key[i])

    # encode
    # message = 'I am going' ->
    # s = ['F','A','D','V','A','G','X','X','D','X','F','A','G','D','X','X']
    s = []
    for c in message.lower():
        if c.isalpha() or c.isdigit():
            row, col = divmod(secret_alphabet1.index(c), 6)
            s += [MAGIC[row], MAGIC[col]]

    # reorder
    # reorder index = [0, 6, 12, 4, 10, 3, 9, 15, 1, 7, 13, 2, 8, 14, 5, 11]
    return ''.join(s[j] for i in k for j in range(i, len(s), n))


def decode(message,secret_alphabet1, keyword):
    secret_alphabet1=generate_secret_alphabet(keyword) 
    # remove duplicate character from keyword -> key
    # keyword = 'checkio' -> key = ['c', 'h', 'e', 'k', 'i', 'o']
    key = []
    for c in keyword:
        if c not in key: key.append(c)

    # make sort index -> k
    # keyword = 'cipher' -> k = [0, 4, 3, 2, 1, 2, 5]
    n = len(key)
    k = sorted(range(n), key=lambda i: key[i])

    # make reorder index
    # len(message) == 16 ->
    # x = [0, 6, 12, 4, 10, 3, 9, 15, 1, 7, 13, 2, 8, 14, 5, 11]
    m = len(message)
    x = [j for i in k for j in range(i, m, n)]

    # reorder
    # message = 'FXGAFVXXAXDDDXGA' ->
    # y = ['F','A','D','V','A','G','X','X','D','X','F','A','G','D','X','X']
    y = ['']*m
    for i, c in zip(x, message): y[i] = c

    # decode
    # y -> s = ['i','a','m','g','o','i','n','g']
    s = []
    for i in range(0, m, 2):
        row, col = y[i:i+2]
        s.append(secret_alphabet1[6 * MAGIC.index(row) + MAGIC.index(col)])
    return ''.join(s)



if __name__ == '__main__':
  message=""
  keyword=""
  alphabet=""
  if len(sys.argv)>1:
      message=sys.argv[1]
  if len(sys.argv)>2:
      keywrod=sys.argv[2]
  if len(sys.argv)>3:
      alphabet=sys.argv[3]
  else:
           print("usages:-v message  keyword alphabet")
  isadfvgx=True
  for x in magic:
       if not x in message:
              isadfvgx=False
  if isadfvgx :
          print("decode  of message in adfvgx is",decode(message,alphabet,keyword))
  else:
           print("encode of message in adfvgx is",encode(message,alphabet,keyword))
         
 