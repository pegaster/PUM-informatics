# modified Euclidean algorithm

def gcd(a, b):
    while (a != 0) and (b != 0):
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

def lcm(a, b):
    return (a * b) // gcd(a, b)

if __name__ == "__main__":
    nums = input().split()

    print(lcm(int(nums[0]), int(nums[1])))
