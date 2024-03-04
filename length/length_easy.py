import json
import math

length = {
    "バスケットボールコートの長さ": 28.65,
    "エッフェル塔の高さ": 300,
    "富士山の高さ": 3776,
    "マリアナ海溝の最深部": 10994,
    "ナイル川の長さ": 6650 * 1000,
    "アマゾン川の長さ": 7050 * 1000,
    "中国の万里の長城": 21196 * 1000,
    "エベレストの高さ": 8848,
    "大西洋を横断する最短距離": 3700 * 1000, # メートル
    "地球の赤道の周囲長": 40075 * 1000,
    "地球の直径": 12742 * 1000,
}

# クイズデータのリスト
quizzes = []
for key in length.keys():
    quiz = {"question": f"{key}は何mですか？",
            "answer": math.log10(length[key])}
    quizzes.append(quiz)

# JSONファイルに保存
with open('length_easy_quizzes.json', 'w') as f:
    json.dump(quizzes, f, ensure_ascii=False, indent=4)

# ファイルのパスを表示
print("length_easy_quizzes.json")
