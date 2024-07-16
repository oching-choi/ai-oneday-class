import streamlit as st
import time
import os
from openai import OpenAI

client = OpenAI(api_key=st.secrets["API_KEY"])

# 코드스니펫 - 제목
st.title('홍보봇 🤖')

# 코드스니펫 - 입력
keyword = st.text_input("키워드.")

# 코드스니펫 - 버튼
if st.button('생성 :fire:'):
    with st.spinner('생성 중입니다.'):
        chat_completion = client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": keyword + " 에 대한 150자 이내의 홍보 문구를 작성해줘.",
            }],
            model="gpt-4o",
        )
        chat_result = chat_completion.choices[0].message.content

        response = client.images.generate(
            model="dall-e-3",
            prompt=keyword + "에 대한 2000년대 만화 스타일의 그림을 그려줘",
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        st.write(chat_result)
        st.image(image_url)
