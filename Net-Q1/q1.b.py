def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = fac(num)
    print(f"The factorial of {num} is {result}")
