# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def date_to_days(date):
    date = list(map(int, date.split('.')))
    days = date[0] * 12 * 28 + date[1] * 28 + date[2]
    return days


def solution(today, terms, privacies):
    todays = date_to_days(today)

    term_to_month = {}
    for t in terms:
        t0, t1 = t.split()
        term_to_month[t0] = int(t1)

    answer = []
    for i, privacy in enumerate(privacies):
        date, term = privacy.split(' ')
        days = date_to_days(date)
        period = 28 * term_to_month[term]
        exp_days = days + period

        if todays >= exp_days:
            answer.append(i+1)

    return answer