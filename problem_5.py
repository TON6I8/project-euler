"""
problem 5

Link to problem:

https://projecteuler.net/problem=5

The way i have comleted this problem is by creating a variable called n, this is our answer.
If n is all the numbers from 1 to 20 multipilied together it will garantee an answer that is evenly dibvisible but it isnt the smallest.
So we need to cancel the the numbers that can be repeated because they are useless which is why i have creadted a list.
The reason why i have added the prime factors with the numbers is because they are basically  the base numbers that cant be divided again.
So we go through each number to see if they are repeatable e.g. 20 isnt repeatable as we dont ahave the neccessary primes to make it.
However 15 is repeatable as we have 3 and 5 already, we then carry this on.
When ewe have all the neccesary numbers (20, 19 18, 17, 14, 11 and 13)we times them together.
To create the answer  232792560.
To then check this we make sure when n is divisible by all numbers from 1 to 20 and the answer has no remainder.
I have added an extra bit of code so that instead of it saying all the answers it says true if it has no remainder and false if it does.

"""

20 - 2 x 2 x 5
19 - 19
18 - 2 x 3 x 3
17 - 17 
#16 - 2 x 2 x 2 x 2
#15 - 3 x 5
14 - 7 x 2
#12 - 2 x 3 x 2
11 - 11
#10 - 2 x 5
#9 - 3 x 3
#8 - 2 x 2 x 2
#7 - 7
#6 - 3 x 2
#5 - 5
#4 - 2 x 2
#3 - 3
#2 - 2

n = 20*19*18*17*14*11*13

does_divide = True

print("my number", n)


for i in range(1, 20):
    print(i, n % i == 0)
    if n % i != 0:
        does_divide = False
        
print(does_divide)

#
    


