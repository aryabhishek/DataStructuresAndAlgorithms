def fibo(n: int) -> int:

    if n <= 1:
        return n
    
    return fibo(n-1) + fibo(n-2)


if __name__ == "__main__":
    print(fibo(5))