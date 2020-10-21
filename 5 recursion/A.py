def num_sum(num, sumOfNum=0):
    if num == 0:
        return sumOfNum
    else:
        sumOfNum += num % 10
        num = num // 10
        return num_sum(num, sumOfNum=sumOfNum)

if __name__ == "__main__":
    print(num_sum(int(input())))