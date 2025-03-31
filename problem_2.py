# def fibonacci(num_terms):
#     a, b = 0, 1
#     for _ in range(num_terms):
#         yield a
#         a, b = b, a + b

# # Print the first 10 Fibonacci numbers
# for value in fibonacci(10):
#     print(value)

s = 0
n = 4_000_000
a = 0
b = 1
next = b  
count = 1

while next < n:
    
    count += 1
    a, b = b, next
    next = a + b
    
    if next % 2 == 0:
        s += next
print(s)
