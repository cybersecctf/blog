
#python
class Bijection:
    def __init__(self):
        self.int_to_str = {}
        self.str_to_int = {}

    def add(self, i, s):
        if i in self.int_to_str or s in self.str_to_int:
            return
        self.int_to_str[i] = s
        self.str_to_int[s] = i

    def get_str(self, i):
        return self.int_to_str.get(i)

    def get_int(self, s):
        return self.str_to_int.get(s)
#a first elements and b second elements and c elements that you want see
def solve(a,b,c):
  bi = Bijection()
  for x in a:
   for y in b:
    bi.add(x, y)
  for z in c:
    print(bi.get_str(z))   
if __name__ == "__main__" :
    solve([1,2,3],["bijection","two","four"],[1])        
