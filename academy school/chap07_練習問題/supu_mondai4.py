# import zipfile
# import re
#
# # ZIPファイルのパス
# zip_file_path = 'data.zip'
#
# # 抽出するログレベル
# log_levels = ['WARNING', 'ERROR']
#
# # 正規表現パターン
# pattern = r'\d{4}-\d{2}-\d{2} 22:\d{2}:\d{2},\d{3} - (\w+):'
#
# # ZIPファイルを読み込みモードでオープン
# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     # ZIPファイル内のapp.logを読み込み
#     with zip_ref.open('app.log', 'r') as log_file:
#         # ログファイルの内容を1行ずつ読み込み
#         for line in log_file:
#             # バイト列を文字列に変換
#             line = line.decode('utf-8')
#             # 正規表現パターンにマッチするかチェック
#             match = re.match(pattern, line)
#             if match:
#                 # ログレベルを取得
#                 log_level = match.group(1)
#                 # ログレベルが指定されたものであれば出力
#                 if log_level in log_levels:
#                     print(line.strip())


import re

logs = []
with open('data/app.log', 'r', encoding='UTF-8') as f:
    for line in f:
        logs.append(line.rstrip('\n'))

pattern = '2022-06[0-9]{2} 22:..:..'
list22 = []
for line in logs:
    result = re.match(pattern, line)
    if result:
        list22.append(line)

list_ans = []
for line in list22:
    if 'WARNING' in line:
        list_ans.append(line)
    if 'ERROR' in line:
        list_ans.append(line)

for line in list_ans:
    print(line)
