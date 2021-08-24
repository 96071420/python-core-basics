lengths = []
words = []
for word in words:
    lengths.append(len(word))

lengths 
[3, 9, 1, 4, 8, 2, 3, 10, 6, 6, 9]
from math import factorial
f = [len(str(factorial(x))) for x in range(20)]
f
[1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18]
type(f)


from math import  factorial
s ={len(str(factorial(x))) for x in range(20)}
type (s)

print(s)
{1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,18}