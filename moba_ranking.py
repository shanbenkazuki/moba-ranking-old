import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Streamlit アプリ
st.title('キャラクター評価')

# 画像のURLとランクのリスト
images_data = [
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Moskov.webp", "rank": "S"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Bruno.webp", "rank": "A"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Jhonson.webp", "rank": "A"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Miya.webp", "rank": "B"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/X-Borg.webp", "rank": "B"},
        {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Moskov.webp", "rank": "S"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Bruno.webp", "rank": "A"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Jhonson.webp", "rank": "A"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Miya.webp", "rank": "B"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/X-Borg.webp", "rank": "B"},
        {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Moskov.webp", "rank": "S"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Bruno.webp", "rank": "A"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Jhonson.webp", "rank": "A"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Miya.webp", "rank": "B"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/X-Borg.webp", "rank": "B"},
        {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Moskov.webp", "rank": "S"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Bruno.webp", "rank": "A"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Jhonson.webp", "rank": "A"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Miya.webp", "rank": "B"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/X-Borg.webp", "rank": "B"},
        {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Moskov.webp", "rank": "S"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Bruno.webp", "rank": "A"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Jhonson.webp", "rank": "A"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/Miya.webp", "rank": "B"},
    {"url": "https://shanbenzzz.com/wp-content/uploads/2023/11/X-Borg.webp", "rank": "B"}
]
# 各ランクごとに画像を表示
for rank in ["S", "A", "B"]:
    images = [img for img in images_data if img["rank"] == rank]
    
    # 画像がある場合のみ処理
    if images:
        # ランク表示用の列と8個の画像表示用の列を作成
        # 最初の行にランクを表示
        st.write(rank)
        
        # 画像表示用の列を設定
        for i in range(0, len(images), 8):
            cols = st.columns(8)
            # 各画像を表示
            for j, img in enumerate(images[i:i+8]):
                # 画像の読み込み
                response = requests.get(img["url"])
                image = Image.open(BytesIO(response.content))
                # 列に画像を配置
                cols[j].image(image, width=100)  # widthは適宜調整