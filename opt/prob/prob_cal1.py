import json
import math
import random
from scipy.special import comb


def coin_toss(n):
    txt = f"コイントスを{n}回行ってすべて表が出る"
    ans = n * math.log10(2)
    return txt, ans

def dice_roll(n):
    txt = f"サイコロを{n}回振ってすべて1が出る"
    ans = n * math.log10(6)
    return txt, ans

def lottery(n):
    txt = f"1%の抽選を{n*100}回行ってあたりが出ない"
    ans = n * math.log10(math.e)
    return txt, ans


def coupon(m,n):
    txt = f"{m}種類の商品が等確率で出るくじを{n}本買って、コンプリートできない"
    # m商品が等確率で出るくじをn本買ってコンプリートできる確率(total_prob)を求める
    total_prob = 0
    for k in range(m):
        # 包除原理を使用
        prob_k = comb(m, k) * ((-1) ** k) * ((m - k) / m) ** n
        total_prob += prob_k
    # 否定なので、1から引く
    ans = - math.log10(1-total_prob)
    return txt, ans


# クイズデータのリスト
quizzes = []
# コイントスの問題を追加
for i in range(10):
    txt, ans = coin_toss(i+1)
    quizzes.append({"question": f"{txt}確率は何分の１ですか？",
        "answer": ans,
        "explanation": f"2の{i+1}乗分の１なので、0.3*{i+1}で推論できます。"
        })
    
# ダイスロールの問題を追加
for i in range(10):
    txt, ans = dice_roll(i+1)
    quizzes.append({"question": f"{txt}確率は何分の１ですか？",
        "answer": ans,
        "explanation": f"6の{i+1}乗分の１なので、0.777*{i+1}で推論できます。"
        })

# 抽選の問題
for i in range(10):
    txt, ans = lottery(i+1)
    quizzes.append({"question": f"{txt}確率は何分の１ですか？",
        "answer": ans,
        "explanation": f"およそeの{i+1}乗分の１なので、0.4343*{i+1}で推論できます。"
        })

# クーポン問題
for mi in [5,10,20]:
    for r in [1.5,2,3,5,10]:
        txt, ans = coupon(mi,int(mi*r))
        quizzes.append({"question": f"{txt}確率は何分の１ですか？",
        "answer": ans,
        "explanation": f"むずかしいですが、それぞれの商品で、1-e^({mi*r}/{mi})の確率で手に入り、互いに独立と仮定すると、ある程度推測できますが、その確率よりも気持ちコンプリートしずらいです。"
        })


# JSONファイルに保存
with open('prob_cal1.json', 'w') as f:
    json.dump(quizzes, f, ensure_ascii=False, indent=4)

# ファイルのパスを表示
print("prob_cal1.json")
