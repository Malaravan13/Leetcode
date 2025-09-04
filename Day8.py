#palindrome
n=int(input())
s=str(n)[::-1]
t=str(n)
if(t==s):
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")
    
#gcd
import math

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print(f"GCD of {n1} and {n2} is {math.gcd(n1, n2)}")