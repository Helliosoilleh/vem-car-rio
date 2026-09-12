import streamlit as st
import datetime
import pandas as pd
import os

st.set_page_config(page_title="VEM CAR RIO", page_icon="🚗", layout="centered")

# ESTILO LARANJA METÁLICO E PRETO
st.markdown("""
<style>
   .stApp { background-color: #0E0E0E; }
    h1, h2, h3, p, label { color: white!important; }
   .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 19px!important;
        font-weight: bold;
        background: linear-gradient(90deg, #FF6F00, #FF8C00);
        color: white;
        border-radius: 15px;
        border: none;
        box-shadow: 0px 4px 15px rgba(255,111,0,0.4);
    }
    div[data-testid="stTabs"] button { color: white!important; }
    div[data-testid="stTabs"] button[aria-selected="true"] {
        background: #FF6F00;
        color: white!important;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# FUNÇÕES PARA SALVAR PRA SEMPRE
def salvar_passageiro(dados):
    arquivo = "passageiros.csv"
    df = pd.DataFrame([dados])
    if os.path.exists(arquivo):
        df_antigo = pd.read_csv(arquivo)
        df = pd.concat([df_antigo, df], ignore_index=True)
    df.to_csv(arquivo, index=False)

def salvar_motorista(dados):
    arquivo = "motoristas.csv"
    df = pd.DataFrame([dados])
    if os.path.exists(arquivo):
        df_antigo = pd.read_csv(arquivo)
        df = pd.concat([df_antigo, df], ignore_index=True)
    df.to_csv(arquivo, index=False)

def carregar_passageiros():
    if os.path.exists("passageiros.csv"):
        return pd.read_csv("passageiros.csv").to_dict('records')
    return []

def carregar_motoristas():
    if os.path.exists("motoristas.csv"):
        return pd.read_csv("motoristas.csv").to_dict('records')
    return []

st.markdown("<h1 style='text-align:center; color:#FF6F00!important;'>🚗 VEM CAR RIO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#FF8C00!important;'>v5.0 - NÃO APAGA MAIS 💎</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Central: (21) 99824-1550</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚕 PASSAGEIRO", "🚗 MOTORISTA", "📋 CORRIDAS"])

with tab1:
    st.subheader("🙋‍♀️ Pedir Carona")
    nome_p = st.text_input("Seu Nome", key="nome_p", placeholder="Ex: Maria")
    c1, c2 = st.columns(2)
    with c1: origem = st.text_input("De onde?", placeholder="Madureira")
    with c2: destino = st.text_input("Para onde?", placeholder="Copacabana")
    whats_p = st.text_input("Seu WhatsApp", key="whats_p", placeholder="21998241550")
    valor_desejado = st.text_input("Quanto quer pagar?", placeholder="Ex: R$ 25")

    if st.button("🚨 PEDIR VEM CAR AGORA", key="btn_p"):
        if nome_p and origem and destino and whats_p:
            dados = {
                "nome": nome_p, "origem": origem, "destino": destino,
                "whats": whats_p, "valor": valor_desejado,
                "hora": datetime.datetime.now().strftime("%H:%M - %d/%m")
            }
            salvar_passageiro(dados)
            st.balloons()
            st.success(f"✅ {nome_p}, salvo pra sempre! {origem} → {destino}")
            st.markdown(f"👉 [CHAMAR CENTRAL NO ZAP](https://wa.me/5521998241550?text=Oi!%20Sou%20{nome_p}%20quero%20ir%20de%20{origem}%20para%20{destino}%20por%20{valor_desejado})")
        else:
            st.warning("Preenche tudo!")

with tab2:
    st.subheader("🚗 Ser Motorista")
    nome_m = st.text_input("Seu Nome", key="nome_m", placeholder="João")
    modelo_cor = st.text_input("Modelo / Cor", key="modelo_m", placeholder="Onix Preto")
    c3, c4 = st.columns(2)
    with c3: placa = st.text_input("Placa", key="placa_m", placeholder="ABC1D23")
    with c4: valor = st.text_input("Valor da corrida", key="valor_m", placeholder="Ex: R$ 30")
    whats_m = st.text_input("Seu WhatsApp", key="whats_m", placeholder="21999999999")
    nota = st.slider("Sua avaliação", 1, 5, 5)

    if st.button("✅ CADASTRAR COMO MOTORISTA", key="btn_m"):
        if nome_m and modelo_cor and placa and whats_m:
            dados = {
                "nome": nome_m, "modelo": modelo_cor, "placa": placa,
                "whats": whats_m, "valor": valor, "nota": nota,
                "hora": datetime.datetime.now().strftime("%H:%M - %d/%m")
            }
            salvar_motorista(dados)
            st.success(f"✅ Motorista {nome_m} salvo pra sempre! ⭐ {nota} estrelas")
        else:
            st.warning("Preenche tudo!")

with tab3:
    passageiros = carregar_passageiros()
    motoristas = carregar_motoristas()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"🚕 Passageiros ({len(passageiros)})")
        if not passageiros:
            st.info("Nenhum ainda")
        for p in reversed(passageiros):
            st.markdown(f"""<div style="background:#1F1F1F;padding:12px;border-radius:12px;margin:8px 0;border-left:5px solid #FF6F00;color:white">
            <b>{p.get('nome','')}</b> - {p.get('valor','')}<br>📍 {p.get('origem','')} → {p.get('destino','')}<br>🕐 {p.get('hora','')}<br>
            <a href="https://wa.me/55{p.get('whats','')}?text=Oi%20{p.get('nome','')}!%20Vi%20seu%20pedido%20no%20VEM%20CAR%20RIO" target="_blank" style="color:#FF8C00">Chamar no Zap</a></div>""", unsafe_allow_html=True)
    with col2:
        st.subheader(f"🚗 Motoristas ({len(motoristas)})")
        if not motoristas:
            st.info("Nenhum ainda")
        for m in reversed(motoristas):
            estrelas = "⭐" * int(m.get('nota',5))
            st.markdown(f"""<div style="background:#1F1F1F;padding:12px;border-radius:12px;margin:8px 0;border-left:5px solid #FF8C00;color:white">
            <b>{m.get('nome','')}</b> {estrelas}<br>🚗 {m.get('modelo','')} - {m.get('placa','')}<br>💰 {m.get('valor','')} - 🕐 {m.get('hora','')}<br>
            <a href="https://wa.me/55{m.get('whats','')}?text=Oi%20{m.get('nome','')}!%20Vi%20voce%20no%20VEM%20CAR%20RIO" target="_blank" style="color:#FF8C00">Chamar no Zap</a></div>""", unsafe_allow_html=True)

st.markdown("---")
st.caption("🧡 v5.0 - Agora salva pra sempre! Pode divulgar seu link!")
