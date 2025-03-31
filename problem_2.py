s = 0
n = 4_000_000
a = 0
b = 1
next = b  

while next < n:
    a, b = b, next
    next = a + b
    
    if next % 2 == 0:
        s += next
print(s)
