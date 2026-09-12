import streamlit as st
import datetime

st.set_page_config(page_title="VEM CAR RIO", page_icon="🚗", layout="centered")

st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 20px !important;
        font-weight: bold;
        background-color: #FFD700;
        color: black;
        border-radius: 15px;
        border: 2px solid black;
    }
    h1 { font-size: 32px !important; text-align: center; }
</style>
""", unsafe_allow_html=True)

if 'pedidos' not in st.session_state:
    st.session_state.pedidos = []

st.markdown("# 🚗 VEM CAR RIO v2.0")
st.markdown("<p style='text-align:center'>Criado por você e por mim 💛</p>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🚕 PEDIR CARONA", "📋 VER PEDIDOS"])

with tab1:
    st.subheader("Pra onde vamos?")
    origem = st.text_input("De onde você está?", placeholder="Ex: Madureira")
    destino = st.text_input("Para onde vai?", placeholder="Ex: Copacabana")
    
    if st.button("🚨 CHAMAR VEM CAR AGORA"):
        if origem and destino:
            pedido = {
                "origem": origem,
                "destino": destino,
                "hora": datetime.datetime.now().strftime("%H:%M"),
                "data": datetime.datetime.now().strftime("%d/%m")
            }
            st.session_state.pedidos.append(pedido)
            
            st.markdown("""
                <audio autoplay>
                    <source src="https://www.soundjay.com/transportation/car-horn-01.mp3" type="audio/mpeg">
                </audio>
            """, unsafe_allow_html=True)
            
            st.balloons()
            st.success(f"✅ PEDIDO FEITO! {origem} -> {destino}")
            st.markdown(f"### 🎉 MOTORISTA A CAMINHO!\n**Clique aqui e chame no WhatsApp:**\n👉 [CHAMAR NO WHATSAPP](https://wa.me/5521998241550?text=Oi!%20Quero%20carona%20de%20{origem}%20para%20{destino})")
        else:
            st.warning("Preenche os dois campos, amor!")

with tab2:
    st.subheader(f"Pedidos de hoje: {len(st.session_state.pedidos)}")
    if not st.session_state.pedidos:
        st.info("Nenhum pedido ainda. Seja o primeiro!")
    else:
        for i, p in enumerate(reversed(st.session_state.pedidos)):
            st.markdown(f"""
            <div style="background:#FFF9C4;padding:12px;border-radius:10px;margin:8px 0;border-left:5px solid #FFD700">
                <b>🚗 {p['origem']} → {p['destino']}</b><br>
                🕐 {p['hora']} - {p['data']}
            </div>
            """, unsafe_allow_html=True)
    
    if st.button("🔊 TESTAR GRITINHO - VEM CAR RIO"):
        st.markdown("""
            <audio autoplay><source src="https://www.soundjay.com/transportation/car-horn-01.mp3" type="audio/mpeg"></audio>
        """, unsafe_allow_html=True)
        st.toast("VEM CAR RIOOO! 🗣️🚗")
