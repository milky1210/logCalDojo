import json
import math
import time

current_year = time.localtime().tm_year
def log_to_prefixed_string(val, mode=0):
    # 大きな値の接頭語
    prefixes_big = {
        math.log10(60*60*24*365)+8: '億年',
        math.log10(60*60*24*365)+4: '万年',
        math.log10(60*60*24*365): '年',
        math.log10(60*60*24): '日',
        math.log10(60*60): '時間',
        math.log10(60): '分',
        0: '秒'
    }
    for exp, prefix in prefixes_big.items():
        if val >= exp:
            number = 10**(val - exp)
            if number<10:
                return f"{number:.2g}{prefix}"
            else:
                return f"{int(number)}{prefix}"
    return f"{int(10**(val - exp))}"

dict1 = {
    "アポロ11号の月面着陸": (current_year - 1969),
    "ベルリンの壁崩壊": (current_year - 1989),
    "アメリカ独立宣言": (current_year - 1776),
    "マグナカルタの発布": (current_year - 1215),
    "コロンブスの新大陸発見": (current_year - 1492),
    "最初のオリンピック開催": (current_year + 776),
    "秦始皇帝による中国統一": (current_year + 221),
    "エジプトピラミッドの建設": (current_year + 3000),
    "最終氷河期の終了": (current_year + 9600),
    "農業の始まり": (current_year + 9000),
    "人が石器を使い始めた日": 25000000,
    "人が火を初めて使った日": 300000,
    "ネアンデルタール人の出現": 400000,
    "人類の祖先が二足歩行を始めたの": 500 * 10000,
    "恐竜の絶滅(第三紀絶滅イベント)": 6600 * 10000,
    "最初のペンギンの誕生": 3500 * 10000,
    "最初の多細胞生物の誕生": 6 * 10000 * 10000,
    "白亜期のはじまり": 1 * 10000 * 10000,
    "カンブリア大爆発": 5.4 * 10000 * 10000,
    "最初の陸上植物の誕生(デボン紀)": 4 * 10000 * 10000,
    "太陽の誕生": 46 * 10000 * 10000,
    "地球の形成": 45 * 10000 * 10000,
    "地球最初の生物の誕生": 38 * 10000 * 10000,
    "ビッグバン": 137 * 10000 * 10000,
}




# クイズデータのリスト
quizzes = []
for key in dict1.keys():
    ans = math.log10(dict1[key]) + math.log10(60 * 60 * 24 * 365)
    quiz = {"question": f"{key}は何秒前ですか？",
        "answer": ans,
        "explanation": f"{key}は{log_to_prefixed_string(ans)}前です。"}
    quizzes.append(quiz)


# JSONファイルに保存
with open('time_knowledge2.json', 'w') as f:
    json.dump(quizzes, f, ensure_ascii=False, indent=4)

# ファイルのパスを表示
print("time_knowledge2.json")
