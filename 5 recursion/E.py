def gcd(a, b):
    if a == 0 or b == 0:
        return a + b
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))