# https://school.programmers.co.kr/learn/courses/30/lessons/135807

def solution(arrayA, arrayB):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # 배열에서 가장 작은 숫자의 약수 구하기
    D1 = [i for i in range(arrayA[0], 1, -1) if arrayA[0] % i == 0]
    D2 = [i for i in range(arrayB[0], 1, -1) if arrayB[0] % i == 0]

    # 배열의 모든 숫자에 대해서 나눌 수 있는지, 못 나누는지 검사
    max_a = 0
    for num in D1:
        for i in range(len(arrayA)):
            if arrayA[i] % num == 0 and arrayB[i] % num != 0:
                continue
            else:
                break
        else:
            # break 없이 루프가 종료된 경우 실행
            max_a = num
            break

    max_b = 0
    for num in D2:
        for i in range(len(arrayA)):
            if arrayB[i] % num == 0 and arrayA[i] % num != 0:
                continue
            else:
                break
        else:
            max_b = num
            break

    return max(max_a, max_b)


if __name__=="__main__":
    print(solution([10, 17], [5, 20]))  # 0
    print(solution([10, 20], [5, 17]))  # 10
    print(solution([14, 35, 119], [18, 30, 102]))  # 7


"""
def solution(arrayA, arrayB):
    # 배열에서 가장 작은 숫자의 약수 구하기
    D1 = [i for i in range(arrayA[0], 1, -1) if arrayA[0] % i == 0]
    D2 = [i for i in range(arrayB[0], 1, -1) if arrayB[0] % i == 0]

    # 배열의 모든 숫자에 대해서 나눌 수 있는지, 못 나누는지 검사
    max_a = 0
    for num in D1:
        for i in range(len(arrayA)):
            if arrayA[i] % num == 0 and arrayB[i] % num != 0:
                continue
            else:
                break
        else:
            # break 없이 루프가 종료된 경우 실행
            max_a = num
            break

    max_b = 0
    for num in D2:
        for i in range(len(arrayA)):
            if arrayB[i] % num == 0 and arrayA[i] % num != 0:
                continue
            else:
                break
        else:
            max_b = num
            break

    return max(max_a, max_b)
"""
