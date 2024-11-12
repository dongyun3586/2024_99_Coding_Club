# https://www.acmicpc.net/problem/2847

n = int(input())  # 레벨의 수
arr = [int(input()) for _ in range(n)]
total = 0

for i in range(n - 1, 0, -1):
    if arr[i] <= arr[i - 1]:
        decrease = arr[i - 1] - arr[i] + 1
        total += decrease
        arr[i - 1] -= decrease

print(total)

