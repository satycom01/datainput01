from cgitb import text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('DataScience TEST')

#"""
# My first Streamlit app

## How it works?

###This site is made by Streamlit command.

## How to run?

#streamlit run my-first-stream-app.py

#```python
#import streamlit as st
#```

#"""

#st.write('DataFrame')

# st.write('Display Image')
# img = Image.open('satycom.jpg')
# st.image(img, caption='Satycom', use_column_width=True)

#チェックボックスで表示させる
# if st.checkbox('Show Image'):
#     img = Image.open('satycom.jpg')
#     st.image(img, caption='Satycom', use_column_width=True)

#セレクトボックスで表示させる
# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11))
# )
# 'あなたが好きな数字は', option, 'です'

#テキストで表示させる
#sidebarを入力すると簡潔にメニューバーができる
#st.write('Interactive Text')

# text = st.sidebar.text_input('あなたの趣味を教えてください')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# '趣味:', text
# 'コンディション:', condition

#column作成
# st.write('Interactive Widgets')

# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')

# if button:
#     right_column.write('ここは右カラムです')

# expander = st.expander('問い合わせ')
# expander.write('問い合わせ内容を書く')

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

#st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)

#st.table(df.style.highlight_max(axis=0))

#バーグラフ作成　or line_chart etc
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.bar_chart(df)

#緯度のマップ作成　
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
#     )
# df
# st.map(df)

