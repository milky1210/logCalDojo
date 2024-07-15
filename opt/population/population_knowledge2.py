import json
import math

population = {
    "東京都の人口(2024年時点)": 1396 * 10000,
    "日本の人口(2024年時点)": 1.251 * 10000 * 10000,
    "2000年生まれの日本人の人数": 119.0547 * 10000,
    "2010年生まれの日本人の人数": 107 * 10000,
    "2020年生まれの日本人の人数": 840835,
    "世界の人口(2024年時点)": 79.51 * 10000 * 10000	

}
def log_to_prefixed_string(val, mode=0):
    # 大きな値の接頭語
    prefixes_big = {
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
# クイズデータのリスト
quizzes = []
for key in population.keys():
    answer = math.log10(population[key])
    quiz = {"question": f"{key}は何人ですか？",
            "answer": answer,
            "explanation": f"{key}は{log_to_prefixed_string(answer)}人です。"}
    quizzes.append(quiz)

# JSONファイルに保存
with open('population_knowledge2.json', 'w') as f:
    json.dump(quizzes, f, ensure_ascii=False, indent=4)

# ファイルのパスを表示
print("population_knowledge2.json")
