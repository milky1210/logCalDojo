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
def log_to_japanese_string(val):
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
            if(val-exp>=3):
                return f"{format(10**(val-exp), '.4g')}{prefix}"
            else:
                return f"{format(10**(val - exp),'.3g')}{prefix}"
    return f"{format((10**(val - exp)),'.3g')}"


time_dict = {
    '年' : 7.4988,
    '日' : 4.9365,
    '時間' : 3.5563,
    '分' : 1.77815,
    '秒' : 0,
    'ms' : -3,
    'us' : -6,
    'ns' : -9
}


# 問題を生成してJSONファイルに保存
quizzes = []

for _ in range(500):
    for key1 in time_dict.keys():
        for key2 in time_dict.keys():
            if(key1==key2):
                continue
            p = random.random()
            ans = p * 10 #
            que = ans + time_dict[key2]-time_dict[key1]
            if(que<0):
                continue
            question = f" {log_to_japanese_string(que)}{key1}は何{key2}ですか？"
            answer = ans
            quizzes.append({"question": question, "answer": answer})


# quizzes.jsonとして保存
with open('time.json', 'w') as file:
    json.dump(quizzes, file, indent=4, ensure_ascii=False)

print("quizzes.jsonを保存しました。")



