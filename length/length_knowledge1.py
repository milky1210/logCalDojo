import json
import math
log_dict ={1:0, 2:0.3, 3:0.4771, 4:0.6, 5:0.7, 6:0.777, 7:0.845, 8:0.9, 9:0.955,10:1, 20: 1.3, 30:1.4771}
def log_to_prefixed_string(val, mode=0):
    if(mode==0):
        # 大きな値の接頭語
        prefixes_big = {
            20: '垓',
            16: '京',
            12: '兆',
            8: '億',
            4: '万',
            0: ''
        }
    else:
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


dict = {
    "Å": 1e-10,
    "nm": 1e-9,       # ナノメートル
    "um": 1e-6,       # マイクロメートル
    "mm": 1e-3,       # ミリメートル
    "cm": 1e-2,       # センチメートル
    "km": 1000,       # キロメートル
    "インチ": 0.0254, # メートル
    "フィート": 0.3048, # メートル
    "ヤード": 0.9144,  # メートル
    "マイル": 1609.34, # メートル
    "天文単位(AU)": 1.496e+11, # メートル
    "光年": 9.461e15, # メートル
}


# クイズデータのリスト
quizzes = []
for key in dict.keys():
    if dict[key]>1:
        quiz = {"question": f"1{key}は何mですか？",
            "answer": math.log10(dict[key]),
            "explanation": f"1{key}は{log_to_prefixed_string(math.log10(dict[key]),mode=1)}mです。"}
    else:
        quiz = {"question": f"1mは何{key}ですか？",
            "answer": -math.log10(dict[key]),
            "explanation": f"1mは{log_to_prefixed_string(-math.log10(dict[key]),mode=0)}{key}"}
            
    quizzes.append(quiz)

# tan系を暗記
for theta in [1,2,3,5,10,20,30]:
    quiz = {
        "question": f"tan{theta}は何分の一ですか？",
        "answer": math.log10(1/math.tan(math.radians(theta))),
        "explanation": f"tan{theta}は{1/math.tan(math.radians(theta))}です。¥n180/{theta}*πで近似できるので、2.25-{log_dict[theta]}+0.5で大まかに推論できます。"
    }
    quizzes.append(quiz)




# JSONファイルに保存
with open('length_knowledge1.json', 'w') as f:
    json.dump(quizzes, f, ensure_ascii=False, indent=4)

# ファイルのパスを表示
print("length_knowledge1.json")
