import math 
a, b = int(input('a = ')), int(input('b = '))
print(a * b // math.gcd(a, b))
