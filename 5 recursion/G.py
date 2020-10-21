def h(n, x=1, y=3):
    if n == 1:
        print(1, x, y)
    else:
        h(n - 1, x, 6 - x - y)
        print(n, x, y)
        h(n - 1, 6 - x - y, y)

if __name__ == "__main__":
    h(int(input()))