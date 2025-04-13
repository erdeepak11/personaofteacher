import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define your system prompt
system_prompt = """
Tum ek AI teacher ho jo Hindi mein jawab deta hai jaise Hitesh Choudhary sir bolte hain...
"""

# Streamlit UI
st.set_page_config(page_title="Hitesh AI Bot", page_icon="🤖")
st.title("🧠 Hitesh AI Teacher Bot")

user_input = st.text_input("Apna sawaal poochhiye:")

if user_input:
    with st.spinner("Soch rahe hain..."):
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        st.markdown("### 📣 Jawaab:")
        st.write(reply)
