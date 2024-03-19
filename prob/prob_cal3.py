import json
import math
import random
from scipy.special import comb
from scipy.stats import binom
from tqdm import tqdm


def exam(n,m):
    return 1

# クイズデータのリスト
quizzes = []
# コイントスの問題を追加
for i in range(20):
    for j in range(i):
        txt, ans = exam(i+1,j+1)
        quizzes.append({"question": f"{txt}確率は何分の１ですか？",
            "answer": ans})
    



# JSONファイルに保存
with open('prob_cal3.json', 'w') as f:
    json.dump(quizzes, f, ensure_ascii=False, indent=4)

# ファイルのパスを表示
print("prob_cal3.json")
