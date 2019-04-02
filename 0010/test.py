from functools import reduce

x,y=3,4
f=lambda x,y:x*y
print(f(x,y))

f=reduce(f,range(1,11))
print(f)
