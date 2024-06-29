import json
import math
def log_to_prefixed_string(val):
    # 大きな値の接頭語
    prefixes_big = {
        20: '垓',
        16: '京',
        12: '兆',
        8: '億',
        4: '万',
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

dict = {
    "年末ジャンボの一等が一発で当たる":  2000 * 10000,
    "黒ひげ危機一発が飛び出す": 100 / 7.7,
    "クローバーが4つ葉になる": 10000,
    "麻雀で上がった時(鳳凰卓)、役満になる": 1442983 / 1239, 
    "麻雀で役に天和がつく": 4250305029168216000 / 12859078207678,
    "52枚のトランプでロイヤルストレートフラッシュが一発で揃う": 2598960 / 4,
    "54枚のトランプでロイヤルストレートフラッシュが一発で揃う": 3162510 / (4*(1 + 5 + 5 + 10)),
    "正規分布からのサンプルがμ+σ以上となる": 1 / (1 - 0.8413), # 約15.87%
    "正規分布からのサンプルがμ+1.5σ以上となる": 1 / (1 - 0.9332), # 約6.68%
    "正規分布からのサンプルがμ+2σ以上となる": 1 / (1 - 0.9772), # 約2.28%
    "正規分布からのサンプルがμ+3σ以上となる": 1 / (1 - 0.9987), # 約0.13%
    "正規分布からのサンプルがμ+4σ以上となる": 1 / (1 - 0.999936657516334), # 約0.0063%
    "1/1000の確率が1000回でない(≒1/e)": math.e
}


# クイズデータのリスト
quizzes = []
for key in dict.keys():
    ans = math.log10(dict[key])
    quiz = {"question": f"{key}確率は何分の１ですか？",
        "answer": ans,
        "explanation": f"{key}確率は約{log_to_prefixed_string(ans)}分の１です。"
        }
    quizzes.append(quiz)

# JSONファイルに保存
with open('prob_knowledge2.json', 'w') as f:
    json.dump(quizzes, f, ensure_ascii=False, indent=4)

# ファイルのパスを表示
print("prob_knowledge2.json")
