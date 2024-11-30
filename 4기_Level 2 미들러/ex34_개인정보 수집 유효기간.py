# https://school.programmers.co.kr/learn/courses/30/lessons/150370?language=python3

def solution(today, terms, privacies):
    # 날짜를 일(day) 기준으로 변환하는 함수
    def date_to_days(date):
        year, month, day = map(int, date.split('.'))
        return year * 12 * 28 + month * 28 + day

    # 오늘 날짜를 일(day) 기준으로 변환
    today_days = date_to_days(today)

    # 약관 종류와 유효기간을 딕셔너리로 저장
    terms_dict = {}
    for term in terms:
        term_type, duration = term.split()
        terms_dict[term_type] = int(duration) * 28  # 달(month) → 일(day) 변환

    # 파기해야 할 개인정보 번호를 저장할 리스트
    result = []

    # 개인정보 처리
    for idx, privacy in enumerate(privacies):
        date, term_type = privacy.split()
        start_days = date_to_days(date)  # 개인정보 수집 날짜를 일(day)로 변환
        expiry_days = start_days + terms_dict[term_type]  # 유효기간 적용

        # 오늘 날짜를 기준으로 유효기간을 초과한 경우 파기 대상
        if expiry_days <= today_days:
            result.append(idx + 1)  # 번호는 1부터 시작

    # 결과 반환
    return result



if __name__ == '__main__':
    print(solution("2022.05.19", ["A 6", "B 12", "C 3"],
                   ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))  # [1, 3]
    print(solution("2020.01.01", ["Z 3", "D 5"],
                   ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))  # [1, 4, 5]
