logbook_test_1 = ["BG", "CA", "FI", "OK"]  # output : 8

logbook_test_2 = ["CA"]  # output : 2

logbook_test_3 = ["BG", "CA"]  # output : 6

logbook_test_4 = ["II", "ZW", "CI", "DT", "IM", "II", "TR", "XO", "AL"]  # output : 25

logbook_test_5 = ["CC"]  # output : 0

logbook_test_6 = ["ML", "UI", "RQ", "DQ", "KA", "SO", "SF", "DL", "YV", "KL"]  # expected o/p : 20, original o/p : 24


def solution(logbook):
    l = []
    min_value = 1
    max_value = 1
    expand_list = []

    for i in logbook:
        l1 = []
        if ord(i[0]) != ord(i[1]):
            l1.append(ord(i[0]))
            l1.append(ord(i[1]))

        if len(l1) == 0:
            l.append([1, 1])
        else:
            l.append([min(l1), max(l1)])

    for i in logbook:
        if ord(i[0]) != ord(i[1]):
            expand_list.append(ord(i[0]))
            expand_list.append(ord(i[1]))

    if len(expand_list) == 0:
        expand_list.append(1)
        expand_list.append(1)

    else:
        min_value = min(expand_list)
        max_value = max(expand_list)

    for k in l:
        if min_value in k:
            max_value = k[1]

    res = min_distance(l, min_value, max_value)

    return res


def min_distance(l, min_v, max_v):
    for i in l:
        if min_v < i[0] and max_v < i[1] and i[0] < max_v:
            max_v = i[1]
            min_distance(l, min_v, max_v)

    return abs(min_v - max_v)


print(solution(logbook_test_1))

print(solution(logbook_test_2))

print(solution(logbook_test_3))

print(solution(logbook_test_4))

print(solution(logbook_test_5))

print(solution(logbook_test_6))
