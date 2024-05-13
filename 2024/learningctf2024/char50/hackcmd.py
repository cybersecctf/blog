
import random,string
print(''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=50)))