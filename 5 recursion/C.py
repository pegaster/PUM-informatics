def factorial(n, result=1):
    if n == 0:
        return result
    return factorial(n - 1, result * n)

if __name__ == "__main__":
    print(factorial(int(input())))