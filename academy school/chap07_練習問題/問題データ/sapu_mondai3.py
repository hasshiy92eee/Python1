def calc_total_average(scores):
    j_language = scores.get('国語', 0)
    m_score = scores.get('数学', 0)
    en_score = scores.get('英語', 0)

    total_score = j_language + m_score + en_score

    h_score = total_score / 3

    return h_score


scores = {
    '国語': 87, '数学': 86, '英語': 70, '理科': 73, '社会': 80
}

average = calc_total_average(scores)

print(f"国語・数学・英語の平均点は {average:.2f} 点です。")
