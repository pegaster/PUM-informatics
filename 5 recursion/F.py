def reverse_sample():
    num = int(input())
    if num != 0:
        reverse_sample()
        print(f' {num}', end='')

if __name__ == "__main__":
    reverse_sample()
    print('')