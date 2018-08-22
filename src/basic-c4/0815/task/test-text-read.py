with open("text-record.txt", encoding="utf-8") as f:
    records = {}
    list_1 = []
    dict_1 = {}
    sum_v = 0
    for line in f:
        records = line
        records = records.replace(",", ":")
        records = records.replace("\n", "")
        list_1.append(records)

records = list_1
print(records)
# dict(list_1.items())
# dict_1 = dict(list_1)

for v in records.values():   # recordsの値だけを順に取得
    sum_v += v
# 平均点を計算して結果を表示
ave_v = sum_v / len(records)
print("合計点:", sum_v)
print("平均点:", ave_v)

# 成績データの一覧と平均点との差を表示
fmt = "| {0:<7} | {1:>4} | {2:>5}"    # 7文字左寄せ、4文字右寄せ、5文字右寄せと指定
print("| 名前    | 点数 | 差")
for name, v in sorted(records.items()):
    # 平均点との差を求める
    diff_v = v - ave_v
    # 小数点以下を丸める
    diff_v = round(diff_v, 1)
    # 書式に沿って出力
    print(fmt.format(name, v, diff_v))
