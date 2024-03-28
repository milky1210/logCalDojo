import json
import math

speeds = {
    "徒歩": 1.4,
    "アマチュアのマラソンの平均速度": 2.4937,
    "プロマラソン選手の平均速度": 5.555555555,
    "一般的な街中の自転車の速度": 4.1666,
    "高校生の100m走の平均速度": 8.14995,
    "プロ短距離走選手の最高速度": 12.35,
    "一般道の車の制限速度": 16.666666666666666,
    "高速道路の制限速度": 27.7777777777,
    "新幹線の最高速度": 83.33333333,
    "ジェット旅客機の巡航速度": 250,
    "音速": 343,
    "ライフルの弾丸の速度": 850,
    "第一宇宙速度": 8000,
    "第二宇宙速度": 11194.4444,
    "第三宇宙速度": 16694.4444,
    "光速": 299792458
}
def log_to_prefixed_string(val, mode=0):
    # 大きな値の接頭語
    prefixes_big = {
        19: '京k',
        15: '兆k',
        11: '億k',
        7: '万k',
        3: 'k',
        0: ''
    }
    for exp, prefix in prefixes_big.items():
        if val >= exp:
            number = 10**(val - exp)
            if number<10:
                return f"{number:.2g}{prefix}"
            else:
                return f"{int(number)}{prefix}"
    return f"{int(10**(val - exp))}"




# クイズデータのリスト
quizzes = []
for key in speeds.keys():
    quiz = {"question": f"{key}は何m/sですか？",
            "answer": math.log10(speeds[key]),
            "explanation": f"{key}は{log_to_prefixed_string(math.log10(speeds[key]))}m/sです。"}
    quizzes.append(quiz)

# JSONファイルに保存
with open('speed_knowledge2.json', 'w') as f:
    json.dump(quizzes, f, ensure_ascii=False, indent=4)

# ファイルのパスを表示
print("speed_knowledge2.json")
