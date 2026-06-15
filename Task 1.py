# Python Programming Internship - Task 1

# 1. Sum of Two Numbers
print("Question 1: Sum of Two Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

# 2. Odd or Even Checker
print("\nQuestion 2: Odd or Even")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# 3. Factorial Calculation
print("\nQuestion 3: Factorial")
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact =fact * i
print("Factorial =", fact)

# 4. Fibonacci Sequence
print("\nQuestion 4: Fibonacci Series")
n = int(input("Enter number of terms: "))
a=0
b=1
for i in range(n):
    print(" ",a, end ='' '' )
    c=a+b
    a=b
    b=c
   

# 5. String Reverse
print("\nQuestion 5: Reverse String")
text = input("Enter a string: ")
print("Reversed String =", text[::-1])

# 6. Palindrome Check
print("\nQuestion 6: Palindrome Check")
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 7. Leap Year Check
print("\nQuestion 7: Leap Year")
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# 8. Armstrong Number
print("\nQuestion 8: Armstrong Number")
num = int(input("Enter a number: "))
power = len(str(num))
total = 0

for digit in str(num):
    total = total + int(digit) ** power

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")