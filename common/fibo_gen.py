# Generator Yielding Fibonacci numbers

def fibo_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input("Enter a number: "))
    for i, f in enumerate(fibo_gen()):
        if i > n:
            break
        print(f, end=" ")
    print()

