print("1)")
import math
a=[2,4,9,16,25]
b=[]
for i in a:
   b.append(math.sqrt(i))
print(b)
    

print("2)")
import math
a=[2,4,9,16,25]
def sqr(x):
    return math.sqrt(x)
print(list(map(sqr,a)))


print("3)")
import math
a=[2,4,9,16,25]
b=[math.sqrt(i) for i in a]
print(b)

