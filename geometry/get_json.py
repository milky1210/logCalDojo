import requests
from bs4 import BeautifulSoup
import json

URL = "https://ja.wikipedia.org/wiki/ISO_3166-1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

# 表を取得
table = soup.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")[1:]  # ヘッダーを除外

country_codes = {}


for row in rows:
    columns = row.findAll("td")
    try:
        # 日本語名を含む<a>タグを正確に取得
        country_name_jp = columns[0].find_all("a")[1].text.strip()
        alpha_3 = columns[3].text.strip()
        country_codes[alpha_3] = country_name_jp
    except (IndexError, AttributeError):
        # 列が足りない行や<a>タグが存在しない行をスキップ
        continue



# 辞書データをJSONファイルとして保存
with open('iso3_to_jpname.json', 'w', encoding='utf-8') as file:
    json.dump(country_codes, file, ensure_ascii=False, indent=4)

