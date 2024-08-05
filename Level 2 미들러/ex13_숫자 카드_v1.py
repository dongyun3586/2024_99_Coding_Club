# https://www.acmicpc.net/problem/10815

n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))

# 숫자카드1과 숫자카드2를 오름차순 정렬함. 이때 숫자카드2는 초기의 index 위치값도 함께 저장.
nums1 = sorted(nums1)
nums2 = sorted([(num, idx) for idx, num in enumerate(nums2)])

answer = [0] * len(nums2)   # 숫자카드2 크기의 0으로 채워진 list

# 숫자카드1과 숫자카드2를 작은 숫자부터 살펴보는데, 둘 중 하나라도 더이상 숫자가 없으면 종료
i, j = 0, 0
while i < len(nums1) and j < len(nums2):
    # 숫자카드1의 j번째 요소가 숫자카드1의 i번째 요소와 같으면: answer의 j번째 값을 1로 변경
    if nums2[j][0] == nums1[i]:
        answer[nums2[j][1]] = 1
        i, j = i + 1, j + 1
    elif nums2[j][0] < nums1[i]:    # 숫자카드2의 j번째 숫자가 숫자카드1의 i번재 숫자코다 작으면 j값 증가
        j += 1
    else:
        i += 1

print(' '.join(map(str, answer)))   # answer 리스트를 하나의 문자열로 출력