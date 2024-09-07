def factorial(n):
    if(n<1):
        return 1
    else:
        return n*factorial(n-1)
def fibonacci(n):
    if(n<=1):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
x=int(input())
y=int(input())
facto=factorial(x) 
print(f"factorial={facto}")
fibo=fibonacci(y)
print(f"fibonacci={fibo}")
