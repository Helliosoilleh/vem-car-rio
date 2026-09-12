import streamlit as st
import datetime

st.set_page_config(page_title="VEM CAR RIO", page_icon="🚗", layout="centered")

st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        height: 55px;
        font-size: 18px !important;
        font-weight: bold;
        background-color: #FFD700;
        color: black;
        border-radius: 12px;
        border: 2px solid black;
        margin-top: 10px;
    }
    h1 { font-size: 28px !important; text-align: center; }
</style>
""", unsafe_allow_html=True)

if 'passageiros' not in st.session_state:
    st.session_state.passageiros = []
if 'motoristas' not in st.session_state:
    st.session_state.motoristas = []

st.markdown("# 🚗 VEM CAR RIO v3.0")
st.markdown("<p style='text-align:center'>Passageiro ou Motorista? Vem! 💛</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚕 PASSAGEIRO", "🚗 MOTORISTA", "📋 CORRIDAS"])

with tab1:
    st.subheader("🙋‍♀️ Cadastrar Passageiro")
    nome_p = st.text_input("Seu Nome", key="nome_p", placeholder="Ex: Maria")
    origem = st.text_input("De onde você está?", key="origem_p", placeholder="Ex: Madureira")
    destino = st.text_input("Para onde vai?", key="destino_p", placeholder="Ex: Copacabana")
    whats_p = st.text_input("Seu WhatsApp", key="whats_p", placeholder="Ex: 21998241550")

    if st.button("🚨 PEDIR VEM CAR AGORA", key="btn_p"):
        if nome_p and origem and destino and whats_p:
            st.session_state.passageiros.append({
                "nome": nome_p,
                "origem": origem,
                "destino": destino,
                "whats": whats_p,
                "hora": datetime.datetime.now().strftime("%H:%M")
            })
            st.markdown('<audio autoplay><source src="https://www.soundjay.com/transportation/car-horn-01.mp3"></audio>', unsafe_allow_html=True)
            st.balloons()
            st.success(f"✅ {nome_p}, seu pedido foi feito! {origem} -> {destino}")
            st.markdown(f"👉 [FALAR COM A CENTRAL NO WHATSAPP](https://wa.me/5521998241550?text=Oi!%20Sou%20{nome_p}%20e%20quero%20carona%20de%20{origem}%20para%20{destino}%20-%20meu%20zap%20{whats_p})")
        else:
            st.warning("Preenche tudo, amor!")

with tab2:
    st.subheader("🚗 Cadastrar Motorista")
    nome_m = st.text_input("Seu Nome", key="nome_m", placeholder="Ex: João")
    modelo_cor = st.text_input("Modelo do Carro / Cor", key="modelo_m", placeholder="Ex: Onix Preto")
    placa = st.text_input("Placa", key="placa_m", placeholder="Ex: ABC1D23")
    whats_m = st.text_input("Seu WhatsApp", key="whats_m", placeholder="Ex: 21999999999")

    if st.button("✅ QUERO SER MOTORISTA VEM CAR", key="btn_m"):
        if nome_m and modelo_cor and placa and whats_m:
            st.session_state.motoristas.append({
                "nome": nome_m,
                "modelo": modelo_cor,
                "placa": placa,
                "whats": whats_m,
                "hora": datetime.datetime.now().strftime("%H:%M")
            })
            st.success(f"✅ Bem-vindo, motorista {nome_m}! Carro {modelo_cor} cadastrado!")
            st.toast(f"Motorista {nome_m} cadastrado! 🗣️ VEM CAR RIO!")
        else:
            st.warning("Preenche tudo!")

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"🚕 Passageiros ({len(st.session_state.passageiros)})")
        if not st.session_state.passageiros:
            st.info("Nenhum passageiro ainda")
        else:
            for p in reversed(st.session_state.passageiros):
                st.markdown(f"""<div style="background:#FFF9C4;padding:10px;border-radius:10px;margin:6px 0;border-left:5px solid #FFD700">
                <b>{p['nome']}</b><br>📍 {p['origem']} → {p['destino']}<br>📱 {p['whats']} - 🕐 {p['hora']}<br>
                <a href="https://wa.me/55{p['whats']}?text=Oi%20{p['nome']},%20vi%20seu%20pedido%20no%20VEM%20CAR%20RIO!" target="_blank">Chamar no Zap</a>
                </div>""", unsafe_allow_html=True)
    with col2:
        st.subheader(f"🚗 Motoristas ({len(st.session_state.motoristas)})")
        if not st.session_state.motoristas:
            st.info("Nenhum motorista ainda")
        else:
            for m in reversed(st.session_state.motoristas):
                st.markdown(f"""<div style="background:#E3F2FD;padding:10px;border-radius:10px;margin:6px 0;border-left:5px solid #2196F3">
                <b>{m['nome']}</b><br>🚗 {m['modelo']} - {m['placa']}<br>📱 {m['whats']} - 🕐 {m['hora']}<br>
                <a href="https://wa.me/55{m['whats']}?text=Oi%20{m['nome']},%20vi%20voce%20no%20VEM%20CAR%20RIO!" target="_blank">Chamar no Zap</a>
                </div>""", unsafe_allow_html=True)

    if st.button("🔊 TESTAR GRITINHO"):
        st.markdown('<audio autoplay><source src="https://www.soundjay.com/transportation/car-horn-01.mp3"></audio>', unsafe_allow_html=True)
        st.toast("VEM CAR RIOOO! 🗣️")

st.caption("📱 v3.0 - Funciona no celular! | Central: (21) 99824-1550")
