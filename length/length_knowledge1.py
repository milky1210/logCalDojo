import json
import math

length = {
    "nm": 1e-9,       # ナノメートル
    "um": 1e-6,       # マイクロメートル
    "mm": 1e-3,       # ミリメートル
    "cm": 1e-2,       # センチメートル
    "km": 1000,       # キロメートル
    "インチ": 0.0254, # メートル
    "フィート": 0.3048, # メートル
    "ヤード": 0.9144,  # メートル
    "マイル": 1609.34, # メートル
    "天文単位(AU)": 1.496e+11, # メートル
    "光年": 9.461e15, # メートル
}


# クイズデータのリスト
quizzes = []
for key in length.keys():
    if length[key]>1:
        quiz = {"question": f"1{key}は何mですか？",
            "answer": math.log10(length[key])}
    else:
        quiz = {"question": f"1mは何{key}ですか？",
            "answer": -math.log10(length[key])}
    quizzes.append(quiz)

# JSONファイルに保存
with open('length_knowledge1.json', 'w') as f:
    json.dump(quizzes, f, ensure_ascii=False, indent=4)

# ファイルのパスを表示
print("length_knowledge1.json")
