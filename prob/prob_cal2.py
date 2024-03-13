import json
import math
import random
from scipy.special import comb
from scipy.stats import binom
from tqdm import tqdm


def coin_toss(n,m):
    txt = f"コイントスを{n}回行って{m}回以上表が出る"
    ans = -math.log10(1-binom.cdf(m-1,n,0.5))
    return txt, ans


def make_dice_roll_dp(n):
    # dpテーブルの初期化（今回は確率を保存）
    dp = [[0.0] * (n*6+1) for _ in range(n+1)]
    dp[0][0] = 1.0  # サイコロを0回振った時の「確率」は1
    
    # DPで確率を計算
    for i in tqdm(range(1, n+1)):
        for j in range(i, i*6+1):
            for k in range(1, 7):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k] * (1/6)  # 各遷移に1/6の確率を乗じる
    return dp


def dice_roll(n,m,dp):
    # 合計がm以上になる確率を計算
    total_probability = sum(dp[n][m:])
    
    # 確率を計算
    txt = f"サイコロを{n}回振って、合計が{m}以上になる"
    ans = - math.log10(total_probability)
    return txt, ans




# クイズデータのリスト
quizzes = []
# コイントスの問題を追加
for i in range(20):
    for j in range(i):
        txt, ans = coin_toss(i+1,j+1)
        quizzes.append({"question": f"{txt}確率は何分の１ですか？",
            "answer": ans})
    
# ダイスロールの問題を追加
dp = make_dice_roll_dp(500)
for i in [3,5,10,20,100,200,300,500]:
    for r in range(35,60,5):
        txt, ans = dice_roll(i,int(i*r/10),dp)
        quizzes.append({"question": f"{txt}確率は何分の１ですか？",
            "answer": ans})



# JSONファイルに保存
with open('prob_cal2.json', 'w') as f:
    json.dump(quizzes, f, ensure_ascii=False, indent=4)

# ファイルのパスを表示
print("prob_cal2.json")
