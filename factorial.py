def factorial(n):
    if(n<1):
        return 1
    else:
        return n*factorial(n-1)
def fibonacci(n):
    if(n<=1):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
facto=factorial(5) 
print(facto)
fibo=fibonacci(5)
print(fibo)