import json
import random
import math
# 問題を生成してJSONファイルに保存
quizzes = []

for _ in range(30000): # 100問生成しますが、この数は変更可能です
    p1, p2 = random.random(), random.random()
    answer = p1 * 9
    a = p2 * 9
    if (answer > a + 2.3):
        question = f"{int(10**a):,} × {int(10**(answer-a)):,}=？"
        answer = math.log10(int(10**a) * int(10**(answer-a)))
    elif (a > answer + 2.3):
        question = f"{int(10**a):,} ÷ {int(10**(a-answer)):,}=？"
        answer = math.log10(int(10**a)/int(10**(a-answer)))
    else:
        continue
    quizzes.append({"question": question, "answer": answer})

# quizzes.jsonとして保存
with open('times_div.json', 'w') as file:
    json.dump(quizzes, file, indent=4, ensure_ascii=False)

print("times_div.jsonを保存しました。")

