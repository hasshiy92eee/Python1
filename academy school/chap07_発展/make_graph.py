import matplotlib
import matplotlib.pyplot as plt

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

labels = [] # x軸の見出し
values = [] # 各値　=> y
for k, v in pref_count_sorted:
    labels.append(k)
    values.append(v)
    
#matplotlib.use('Agg')   #グラフィック環境ではない 
plt.rcParams['font.family'] = 'MyricaM M'
plt.xticks(rotation=60)
plt.title('各都道府県別図書館利用人数(2021年7月)')
plt.bar(range(0, len(pref_count_sorted)),
        values,
         tick_label=labels)

plt.savefig('graph.png')
plt.show() #グラフ表示
