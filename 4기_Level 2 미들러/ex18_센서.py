# https://www.acmicpc.net/problem/2212
import sys
input = sys.stdin.readline

n = int(input())    # 센서의 개수
k = int(input())    # 집중국의 개수
sensors = list(map(int, input().split()))   # n개의 센서의 좌표

sensors.sort()  # 센서 좌표 오름차순 정렬

# 각 센서 사이의 구간 길이 구하기
distances = [sensors[i] - sensors[i-1] for i in range(1, n)]

# 거리 차이 정렬
distances.sort(reverse=True)

# 가장 큰 거리 차이 K-1개 제거하고 나머지 거리의 합을 구함
min_length_sum = sum(distances[k - 1:])

print(min_length_sum)