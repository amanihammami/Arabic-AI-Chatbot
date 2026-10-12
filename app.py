import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API keys from the .env file
load_dotenv()

# Set up page configurations with Arabic titles
st.set_page_config(page_title="مساعد الذكاء الاصطناعي", page_icon="🤖")
st.title("🤖 روبوت الدردشة الذكي الخاص بي")
st.caption("روبوت دردشة بسيط يعمل بواسطة OpenAI و Streamlit مخصص للغة العربية.")

# Fetch key securely from environment variable set by load_dotenv()
api_key = os.getenv("")

# Initialize the OpenAI client securely
if api_key:
    client = OpenAI(api_key=api_key)
else:
    st.error("مفتاح API الخاص بـ OpenAI مفقود! يرجى إضافة 'OPENAI_API_KEY' إلى ملف .env الخاص بك.")
    st.stop()

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "مرحباً! كيف يمكنني مساعدتك اليوم؟"}
    ]

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input field (Placeholder text translated to Arabic)
if user_input := st.chat_input("اكتب رسالتك هنا..."):
    # Append user message to history and display it
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generate assistant response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # Create the messages payload, adding a system prompt to enforce Arabic responses
            messages_payload = [
                {
                    "role": "system", 
                    "content": "You are a helpful assistant. You must always respond in clear, natural, and grammatically correct Arabic, matching the user's dialect if appropriate."
                }
            ]
            # Append the rest of the conversation history
            for m in st.session_state.messages:
                messages_payload.append({"role": m["role"], "content": m["content"]})

            # Stream the response from the LLM
            stream = client.chat.completions.create(
                model="gpt-4o-mini", # Efficient and affordable model
                messages=messages_payload,
                stream=True,
            )
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"خطأ في الاتصال بالذكاء الاصطناعي: {e}")
            full_response = "عذراً، أواجه مشكلة في الاتصال بالخدمة حالياً."
            response_placeholder.markdown(full_response)

    # Append assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
