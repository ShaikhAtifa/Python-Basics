# Multiple of 5 or not 
num = int(input("enter number: "))  
if num % 5 == 0:  
print("multiple of 5")  
else:  
print("NOT a multiple of 5") 

2. Odd or Even :
num = int(input("enter number: "))  
 
if num % 2 == 0:  
    print("Even") 
else:  
    print("Odd") 
 
 
 #---------------------------------------------------------
#(Loops) 
 
#1. Multiplication table of n:
n= int(input("enter n: "))  
i = 1  
 
while i <= 10:  
      print(i * n)  
       i += 1 

#2. Odd nums from 1 to 10, using continue :
i = 0  
 
while(i < 10):  
i += 1  
if(i % 2 == 0):  
continue;  
print(i)  
  
#3. Count vowels :
for ch in word:  
    if (ch == 'a' or ch == 'a' or ch == 'a' or ch == 'a' or ch == 'a'):  
        count += 1  
 
print(f"vowel count = {count}") 
 
#4. Sum of first n Natural numbers 
 
num = int(input("enter number: "))  
 
if num % 2 == 0:  
    print("Even") 
else:  
    print("Odd") 
n = int(input("enter n: "))  
i = 1  
 
while i <= 10:  
      print(i * n)  
       i += 1 
#---------------------------------------------------
 #(Functions) 
1. Factorial of N 
# Factorial of N  
n = int(input("enter n: "))  
fact = 1  
for i in range (1, n+1):  
fact *= i  
print("factorial = ", fact) 
2. Largest of 3 numbers 
def get_largest (a, b, c):  
if (a > b and a > c): 
return a 
elif b > c: 
return b 
else: 
return c 
print (get_largest (3, 10, 5)) 
