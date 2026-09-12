import streamlit as st
import datetime

st.set_page_config(page_title="VEM CAR RIO", page_icon="🚗", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #0E0E0E; }
    h1, h2, h3, p, label { color: white !important; }
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 19px !important;
        font-weight: bold;
        background: linear-gradient(90deg, #FF6F00, #FF8C00);
        color: white;
        border-radius: 15px;
        border: none;
        box-shadow: 0px 4px 15px rgba(255,111,0,0.4);
    }
    div[data-testid="stTabs"] button { color: white !important; }
    div[data-testid="stTabs"] button[aria-selected="true"] {
        background: #FF6F00;
        color: white !important;
        border-radius: 10px;
    }
    input { border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)

if 'passageiros' not in st.session_state:
    st.session_state.passageiros = []
if 'motoristas' not in st.session_state:
    st.session_state.motoristas = []

st.markdown("<h1 style='text-align:center; color:#FF6F00 !important;'>🚗 VEM CAR RIO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#FF8C00 !important;'>LARANJA METÁLICO E PRETO 💎</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center'>Central: (21) 99824-1550</p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🚕 PASSAGEIRO", "🚗 MOTORISTA", "📋 CORRIDAS"])

with tab1:
    st.subheader("🙋‍♀️ Pedir Carona")
    nome_p = st.text_input("Seu Nome", key="nome_p", placeholder="Ex: Maria")
    c1, c2 = st.columns(2)
    with c1: origem = st.text_input("De onde?", placeholder="Madureira")
    with c2: destino = st.text_input("Para onde?", placeholder="Copacabana")
    whats_p = st.text_input("Seu WhatsApp", key="whats_p", placeholder="21998241550")
    valor_desejado = st.text_input("Quanto quer pagar? (opcional)", placeholder="Ex: R$ 25")

    if st.button("🚨 PEDIR VEM CAR AGORA", key="btn_p"):
        if nome_p and origem and destino and whats_p:
            st.session_state.passageiros.append({
                "nome": nome_p, "origem": origem, "destino": destino,
                "whats": whats_p, "valor": valor_desejado,
                "hora": datetime.datetime.now().strftime("%H:%M")
            })
            st.balloons()
            st.success(f"✅ {nome_p}, pedido feito! {origem} → {destino}")
            st.markdown(f"👉 [CHAMAR CENTRAL NO ZAP](https://wa.me/5521998241550?text=Oi!%20Sou%20{nome_p}%20quero%20ir%20de%20{origem}%20para%20{destino}%20por%20{valor_desejado}%20Meu%20zap:%20{whats_p})")
        else:
            st.warning("Preenche nome, origem, destino e zap!")

with tab2:
    st.subheader("🚗 Ser Motorista")
    nome_m = st.text_input("Seu Nome", key="nome_m", placeholder="João")
    modelo_cor = st.text_input("Modelo / Cor", key="modelo_m", placeholder="Onix Preto")
    c3, c4 = st.columns(2)
    with c3: placa = st.text_input("Placa", key="placa_m", placeholder="ABC1D23")
    with c4: valor = st.text_input("Valor da corrida", key="valor_m", placeholder="Ex: R$ 30")
    whats_m = st.text_input("Seu WhatsApp", key="whats_m", placeholder="21999999999")
    nota = st.slider("Sua avaliação inicial", 1, 5, 5)

    if st.button("✅ CADASTRAR COMO MOTORISTA", key="btn_m"):
        if nome_m and modelo_cor and placa and whats_m:
            st.session_state.motoristas.append({
                "nome": nome_m, "modelo": modelo_cor, "placa": placa,
                "whats": whats_m, "valor": valor, "nota": nota,
                "hora": datetime.datetime.now().strftime("%H:%M")
            })
            st.success(f"✅ Motorista {nome_m} cadastrado! Carro {modelo_cor} por {valor} - ⭐ {nota} estrelas")
        else:
            st.warning("Preenche tudo!")

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"🚕 Passageiros ({len(st.session_state.passageiros)})")
        for p in reversed(st.session_state.passageiros):
            # CORREÇÃO AQUI - usa .get pra não quebrar com dados antigos
            p_nome = p.get('nome', 'Passageiro')
            p_valor = p.get('valor', '')
            p_origem = p.get('origem', '')
            p_destino = p.get('destino', '')
            p_hora = p.get('hora', '')
            p_whats = p.get('whats', '')
            st.markdown(f"""<div style="background:#1F1F1F;padding:12px;border-radius:12px;margin:8px 0;border-left:5px solid #FF6F00;color:white">
            <b>{p_nome}</b> - {p_valor}<br>📍 {p_origem} → {p_destino}<br>🕐 {p_hora} | 📱 {p_whats}<br>
            <a href="https://wa.me/55{p_whats}?text=Oi%20{p_nome}!%20Vi%20seu%20pedido%20no%20VEM%20CAR%20RIO" target="_blank" style="color:#FF8C00">Chamar no Zap</a></div>""", unsafe_allow_html=True)
    with col2:
        st.subheader(f"🚗 Motoristas ({len(st.session_state.motoristas)})")
        for m in reversed(st.session_state.motoristas):
            m_nota = m.get('nota', 5)
            estrelas = "⭐" * int(m_nota)
            m_nome = m.get('nome', 'Motorista')
            m_modelo = m.get('modelo', '')
            m_placa = m.get('placa', '')
            m_valor = m.get('valor', '')
            m_hora = m.get('hora', '')
            m_whats = m.get('whats', '')
            st.markdown(f"""<div style="background:#1F1F1F;padding:12px;border-radius:12px;margin:8px 0;border-left:5px solid #FF8C00;color:white">
            <b>{m_nome}</b> {estrelas}<br>🚗 {m_modelo} - {m_placa}<br>💰 {m_valor} - 🕐 {m_hora}<br>📱 {m_whats}<br>
            <a href="https://wa.me/55{m_whats}?text=Oi%20{m_nome}!%20Vi%20voce%20no%20VEM%20CAR%20RIO" target="_blank" style="color:#FF8C00">Chamar no Zap</a></div>""", unsafe_allow_html=True)

st.markdown("---")
st.caption("🧡 v4.1 Corrigida - VEM CAR RIO - Feito por você!")
