import json
import math
def log_to_prefixed_string(val):
    # 大きな値の接頭語
    prefixes_big = {
        18: '兆k',
        14: '億k',
        10: '万k',
        6: 'k',
        4: '万',
        0: ''
    }
    
    # 小さな値の接頭語
    prefixes_small = {
        -4: 'c',
        -6: 'm',
        -12: 'μ',
        -18: 'n',
        -24: 'p',
        -30: 'f',
        -36: 'a',
        -42: 'z',
        -48: 'y'
    }

    for exp, prefix in prefixes_big.items():
        if val >= exp:
            return f"{int(10**(val - exp))}{prefix}"
    
    for exp, prefix in prefixes_small.items():
        if val < 0 and val >= exp:
            return f"{int(10**(val - exp))}{prefix}"
    return f"{int(10**(val - exp))}"
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
        quiz_list.append({"question": f"{name}は何m^2ですか?", "answer": area_log, "explanation": f"約{log_to_prefixed_string(area_log)}m^2なので、{area_log:.2f}となります。"})


# 辞書のリストをJSONファイルに保存
output_path = "area_knowledge2.json"
with open(output_path, 'w', encoding='utf-8') as outfile:
    json.dump(quiz_list, outfile, ensure_ascii=False, indent=4)
