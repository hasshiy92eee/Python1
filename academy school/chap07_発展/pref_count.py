pref_count_dict = {}  # 辞書
with open('visitor_record.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        date, pref, num_adult, num_children = line.rstrip('\n').split(',')
        num_all = int(num_adult) + int(num_children)
        if pref in pref_count_dict:
            pref_count_dict[pref] += num_all
        else:
            pref_count_dict[pref] = num_all

pref_count_sorted = sorted(pref_count_dict.items(), key=lambda x: x[1], reverse=True)
for i in pref_count_sorted:
    print(i)
