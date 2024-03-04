import json
import math

file_path = 'set2.txt'

# ファイルを開いて内容を読み込む
with open(file_path, 'r') as file:
    lines = file.readlines()

# 辞書のリストを作成
quiz_list = []
for line in lines:
    # ラインを分割して名前と面積を取得
    parts = line.split()
    if len(parts) >= 2:
        name = " ".join(parts[:-1])  # 最後の要素以外を名前として結合
        try:
            # 面積を常用対数に変換
            area_log = math.log10(float(parts[-1])) + 6.0
        except ValueError:
            # 面積が数値でない場合はスキップ
            continue
        quiz_list.append({"question": f"{name}は何m^2ですか?", "answer": area_log})


# 辞書のリストをJSONファイルに保存
output_path = "area_easy.json"
with open(output_path, 'w', encoding='utf-8') as outfile:
    json.dump(quiz_list, outfile, ensure_ascii=False, indent=4)
