import json
import math

dict = {
    "ns": 1e-9,
    "us": 1e-6,
    "ms": 1e-3,
    "分": 60,
    "時間": 60 * 60,
    "日": 60*60*24,
    "年": 60*60*24*365,
}


# クイズデータのリスト
quizzes = []
for key in dict.keys():
    if dict[key]>1:
        quiz = {"question": f"1{key}は何秒ですか？",
            "answer": math.log10(dict[key])}
    else:
        quiz = {"question": f"1秒は何{key}ですか？",
            "answer": -math.log10(dict[key])}
    quizzes.append(quiz)

# JSONファイルに保存
with open('time_knowledge1.json', 'w') as f:
    json.dump(quizzes, f, ensure_ascii=False, indent=4)

# ファイルのパスを表示
print("time_knowledge1.json")
