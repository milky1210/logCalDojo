import json
import math
import random
from scipy.special import comb
from scipy.stats import binom
from tqdm import tqdm


def exam(r1,n,r2):
    txt = f"{n}問の試験で、正答率{int(r1*100)}%以上で、合格のとき、正答率{int(r2*100)}%の生徒が合格する"
    min_correct_answers = int(r1 * n)
    prob_passing = 1 - binom.cdf(min_correct_answers - 1, n, r2)
    try:
        ans = - math.log10(prob_passing)
    except:
        ans = None
    return txt, ans

# クイズデータのリスト
quizzes = []
# 試験合格率の問題を追加
for r1 in [0.5, 0.6, 0.7, 0.8, 0.9]:
    for r2 in [r1, r1-0.1, r1-0.2, r1-0.3, r1-0.05]:
        for n in [10, 20, 30, 50, 100, 500, 1000]:
            txt, ans = exam(r1, n, r2)
            if ans is None:
                continue
            quizzes.append({"question": f"{txt}確率は何分の１ですか？",
                "answer": ans})
    



# JSONファイルに保存
with open('prob_cal3.json', 'w') as f:
    json.dump(quizzes, f, ensure_ascii=False, indent=4)

# ファイルのパスを表示
print("prob_cal3.json")
