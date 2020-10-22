N = int(input())
l = input().split()
equal = input()

count = 0
for i in range(N):
    if l[i] == equal:
        count += 1

print(count)