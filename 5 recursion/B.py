def find_max(y, m=0):
    if y == 0:
        return m
    return find_max(y // 10, y % 10 if m < y % 10 else m)

if __name__ == "__main__":
    print(find_max(int(input())))