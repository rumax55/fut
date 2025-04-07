
import streamlit as st

st.set_page_config(page_title="Bot de Apostas", layout="wide")

st.title("⚽ Bot Inteligente de Apostas em Futebol")

menu = st.sidebar.selectbox("Menu", ["Análise", "Arbitragem Odds", "Configurações"])

if menu == "Análise":
    st.header("📊 Análise dos Jogos do Dia")
    st.info("Integração com API e IA aqui.")

elif menu == "Arbitragem Odds":
    st.header("💰 Arbitragem de Odds (Surebet)")
    st.info("Scanner e alertas em tempo real aqui.")

elif menu == "Configurações":
    st.header("⚙️ Configurações")
    st.text_input("Chave Telegram")
    st.text_input("ID do Telegram")
    st.button("Salvar")
