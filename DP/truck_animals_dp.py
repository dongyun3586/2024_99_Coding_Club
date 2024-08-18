def choose_animals(animals, capacity):
    n = len(animals)    # 동물의 개수
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]   # DP 테이블 정의 및 초기화
    # dp[i][w]는 첫 번째 동물부터 i번째 동물까지 고려했을 때, 트럭 용량 w에 대해 얻을 수 있는 최대 선호도를 저장

    # 동물들의 무게와 선호도 분리
    weights = [animal[1] for animal in animals]     # 동물들의 무게 리스트
    values = [animal[2] for animal in animals]      # 동물들의 선호도 리스트

    # DP 테이블 채우기: dp[i][w]를 채워나감
    for i in range(1, n + 1):               # i는 현재 고려 중인 동물의 인덱스
        for w in range(1, capacity + 1):    # w는 현재 고려 중인 트럭의 용량
            if weights[i - 1] <= w:         # 현재 동물의 무게가 현재 트럭 용량 w보다 작거나 같은지 확인
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
                # (이전 상태를 유지하는 것)과 (현재 동물의 무게만큼 용량을 차감하고 최대 선호도에 현재 동물의 선호도를 더해주는 것) 중 최대값 선택
            else:
                dp[i][w] = dp[i - 1][w]     # 동물을 선택하지 않는 경우(이전 상태를 유지)

    # 최대 선호도: 최종적으로 dp[n][capacity]에는 트럭의 최대 적재 용량에서 얻을 수 있는 최대 선호도가 저장된다.
    max_value = dp[n][capacity]

    # 선택된 동물들 찾기: 선택된 동물들을 역추적(backtracking)하여 찾는다.
    w = capacity            # 현재 남은 트럭의 용량
    selected_animals = []   # 선택된 동물들의 이름을 저장할 리스트
    for i in range(n, 0, -1):           # i를 n(전체 동물의 수)부터 1까지 감소시키며, DP 테이블을 역순으로 탐색
        # dp[i][w]는 i번째 동물까지 고려했을 때, 용량이 w인 트럭에 담을 수 있는 최대 선호도를 의미함.
        if dp[i][w] != dp[i - 1][w]:    # 현재 동물 i가 선택되었다면, dp[i][w]와 dp[i-1][w]는 다르다.
            selected_animals.append(animals[i - 1][0])  # 동물 이름 추가
            w -= weights[i - 1]

    return max_value, selected_animals


# 동물 데이터 [이름, 무게, 선호도]
animals = [['호랑이', 2, 1], ['사자', 2, 1], ['얼룩말', 2, 1], ['물소', 3, 4],
           ['하마', 4, 3], ['기린', 5, 5], ['코끼리', 6, 6]]

# 트럭의 최대 적재 용량
truck_payload_limit = 19

# 동물 데이터를 이용한 문제 해결
preference_sum, selected_animals = choose_animals(animals, truck_payload_limit)
print('선호도 합: ', preference_sum)
print('선택된 동물들: ', selected_animals)
