# 제목 : 개인정보 수집 유효기간

def solution(today, terms, privacies):
    today_split = today.split(".")
    today_days = (int(today_split[0]) * 12 + int(today_split[1])) * 28 + int(today_split[2])

    terms_dict = {}

    for term in terms:
        term_type, term_months = term.split(" ")
        terms_dict[term_type] = int(term_months) * 28

    answer = []

    for index, privacy in enumerate(privacies, start=1):
        privacy_date, privacy_type = privacy.split(" ")
        privacy_date_split = privacy_date.split(".")

        if (int(privacy_date_split[0]) * 12 + int(privacy_date_split[1])) * 28 + int(
                privacy_date_split[2]) + terms_dict[privacy_type] <= today_days:
            answer.append(index)

    answer.sort()
    return answer
