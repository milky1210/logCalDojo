import json
import random

def log_to_prefixed_string(val):
    # 大きな値の接頭語
    prefixes_big = {
        24: 'Y',
        21: 'Z',
        18: 'E',
        15: 'P',
        12: 'T',
        9: 'G',
        6: 'M',
        3: 'K',
        0: ''
    }
    
    # 小さな値の接頭語
    prefixes_small = {
        -3: 'm',
        -6: 'μ',
        -9: 'n',
        -12: 'p',
        -15: 'f',
        -18: 'a',
        -21: 'z',
        -24: 'y'
    }

    for exp, prefix in prefixes_big.items():
        if val >= exp:
            return f"{format(10**(val - exp), '.3g')}{prefix}"
    
    for exp, prefix in prefixes_small.items():
        if val < 0 and val >= exp:
            return f"{format(10**(val - exp), '.3g')}{prefix}"
    return f"{format(10**(val - exp), '.3g')}"

# 問題を生成してJSONファイルに保存
quizzes = []

for _ in range(3000): # 100問生成しますが、この数は変更可能です
    p = random.random()
    val = p * 27
    formatted_val = log_to_prefixed_string(val)
    question = f"問題文: {formatted_val}は何桁ですか？"
    answer = val
    quizzes.append({"question": question, "answer": answer})

# quizzes.jsonとして保存
with open('tmp.json', 'w') as file:
    json.dump(quizzes, file, indent=4, ensure_ascii=False)

print("quizzes.jsonを保存しました。")

