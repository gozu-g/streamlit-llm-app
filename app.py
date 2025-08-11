import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

def llm_response(system_message, input_message):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_message),
    ]

    result = llm(messages)
    return result.content

load_dotenv()

st.title("LLMを使った専門家への質問アプリ")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["プログラムの専門家", "経営の専門家"]
)

input_message = st.text_input(label="LLMに質問してください")

system_message = {}
if st.button("実行"):
    if selected_item == "プログラムの専門家":
        # プログラムの専門家としての処理
        st.write("プログラムの専門家モードで実行します。")
        system_message = "あなたはプログラムの専門家です"
    elif selected_item == "経営の専門家":
        # 経営の専門家としての処理
        st.write("経営の専門家モードで実行します。")
        system_message = "あなたは経営の専門家です"

    result = llm_response(system_message, input_message)

    st.write("LLMの応答:")
    st.write(result)

