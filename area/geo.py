import geopandas as gpd
import json
import math

# JSONファイルからiso3コードと日本語の国名のマッピングを読み込む
with open('iso3_to_jpname.json', 'r', encoding='utf-8') as file:
    iso3_to_jpname = json.load(file)

# データセットのロード
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# CRSをMollweide投影に変換
world_moll = world.to_crs('+proj=moll +lon_0=0')

# 各国の面積を計算（単位は平方キロメートル）
world_moll['area'] = world_moll['geometry'].area

# iso_a3コードを使って日本語の国名に変換
world_moll['name_jp'] = world_moll['iso_a3'].map(iso3_to_jpname)



quizzes = []
for index, row in world_moll.iterrows():
    answer = math.log10(row['area'])
    question = f"{row['name_jp']}は何m^2ですか?"
    quizzes.append({"question": question, "answer": answer})
with open('geo_v1.json', 'w') as file:
    json.dump(quizzes, file, indent=4, ensure_ascii=False)

print("quizzes.jsonを保存しました。")
