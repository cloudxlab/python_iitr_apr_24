def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b

def fact(n):
    if n <= 0: return 1;
    return n*fact(n-1);

if __name__ == "__main__":
    print("testing: ", fact(10))
