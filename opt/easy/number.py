import json
import random

# 問題を生成してJSONファイルに保存
quizzes = []

for _ in range(3000): # 100問生成しますが、この数は変更可能です
    p = random.random()
    val = p * 3
    formatted_val = 10**val
    question = f"問題文: {formatted_val}は何桁ですか？"
    answer = val
    quizzes.append({"question": question, "answer": answer})

# quizzes.jsonとして保存
with open('tmp.json', 'w') as file:
    json.dump(quizzes, file, indent=4, ensure_ascii=False)

print("quizzes.jsonを保存しました。")

