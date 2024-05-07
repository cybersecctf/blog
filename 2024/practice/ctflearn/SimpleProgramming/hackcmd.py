
count=0
with open("data.dat","r") as f:
     lines=f.readlines()
for line in lines:
 if line.count('0')%3==0 or line.count('1')%2==0:
   count+=1
print(count)

#python
import sys
file="data.dat"
if len(sys.argv)>1:
    file=sys.argv[1]
count=0
with open("data.dat","r") as f:
     lines=f.readlines()
for line in lines:
 if line.count('0')%3==0 or line.count('1')%2==0:
   count+=1
print(count)