# https://school.programmers.co.kr/learn/courses/30/lessons/87390


def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(max(divmod(i, n)) + 1)
    return answer


if __name__ == "__main__":
    print(solution(3, 2, 5))
    print(solution(4, 7, 14))
    print(solution(4, 0, 5))


# def solution(n, left, right):
#     return [max(divmod(i, n)) + 1 for i in range(left, right + 1)]


# def solution(n, left, right):
#     answer = []
#     A = []
#     for i in range(n):
#         for j in range(n):
#             if i-j >= 0:
#                 A.append(i+1)
#             else:
#                 A.append(j+1)
#
#     # print(A)
#     answer = A[left:right+1]
#     return answer

# def solution(n, left, right):
#     answer = []
#     A = [[0] * n for i in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i-j >= 0:
#                 A[i][j] = i+1
#             else:
#                 A[i][j] = j+1
#
#     for i in range(n):
#         print(A[i])
#     return answer
#

#
# if __name__=="__main__":
#     print(solution(3, 2, 5))
#     print(solution(4, 7, 14))

