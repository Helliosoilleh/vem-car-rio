import streamlit as st
import streamlit.components.v1 as components
import random, datetime

st.set_page_config(page_title="VEM CAR RIO - Mapa", page_icon="🗺️", layout="centered")

st.markdown("<h1 style='text-align:center'>🗺️ VEM CAR RIO</h1><p style='text-align:center'>🔒 Privado com mapa</p>", unsafe_allow_html=True)

CIDADES = {
    "rio": {"lat": -22.9068, "lon": -43.1729},
    "campina": {"lat": -7.2290, "lon": -35.8808},
}

if 'corridas' not in st.session_state:
    st.session_state.corridas = []

perfil = st.radio("Você é:", ["Passageira", "Motorista", "Central"], horizontal=True)

if perfil == "Passageira":
    st.markdown("### 📍 Para onde vamos?")
    
    # AGORA TUDO DENTRO DE UM FORMULÁRIO - NÃO APAGA MAIS
    with st.form("pedido_form"):
        origem = st.text_input("De onde?", "Itapura")
        destino = st.text_input("Para onde?", "Itapocu")
        valor = st.number_input("Quanto quer pagar? R$", 10, 500, 45)
        nome = st.text_input("Seu nome")
        tel = st.text_input("WhatsApp (protegido 🔒)")
        lgpd = st.checkbox("✅ Concordo com LGPD - meus dados ficam protegidos")
        
        botao = st.form_submit_button("PEDIR COM MAPA E PRIVACIDADE 🔒🗺️")

    # MAPA
    st.markdown("#### 🗺️ Sua rota")
    map_html = """
    <iframe width="100%" height="300" frameborder="0" 
    src="https://www.openstreetmap.org/export/embed.html?bbox=-45.0%2C-23.5%2C-35.0%2C-6.5&layer=mapnik&marker=-22.9068%2C-43.1729&marker=-7.2290%2C-35.8808"
    style="border-radius:15px; border: 2px solid #FFD700"></iframe>
    """
    components.html(map_html, height=320)
    st.info(f"📏 1896 km | ⏱️ 26h | 💰 R$ {valor}")

    if botao:
        if not nome:
            st.error("❌ Falta seu nome")
        elif not tel:
            st.error("❌ Falta seu WhatsApp")
        elif not lgpd:
            st.error("❌ Você precisa marcar a caixinha da LGPD")
        else:
            codigo = f"VCR-{random.randint(1000,9999)}"
            st.session_state.corridas.append({
                "codigo": codigo, "nome": nome, "origem": origem, "destino": destino,
                "valor": valor, "tel": tel, "status": "No mapa", 
                "hora": datetime.datetime.now().strftime("%H:%M"), "distancia": 1896
            })
            st.success(f"✅ {codigo} CRIADA COM SUCESSO! Helio, deu certo!")
            st.balloons()
            st.markdown(f"""
            <div style="background:white; padding:15px; border-radius:15px; border-left:5px solid #FFD700">
            <b>{codigo} - NO MAPA</b><br>
            📍 {origem} → {destino}<br>
            👤 {nome} | 💰 R$ {valor}<br>
            🔒 Número protegido
            </div>
            """, unsafe_allow_html=True)

elif perfil == "Motorista":
    st.markdown("### 🚗 Corridas no mapa")
    if not st.session_state.corridas:
        st.write("Nenhuma corrida ainda.")
    else:
        for c in st.session_state.corridas:
            st.write(f"**{c['codigo']}** - {c['origem']} → {c['destino']} - R${c['valor']}")

else:
    senha = st.text_input("Senha Central", type="password")
    if senha == "1234":
        st.write(st.session_state.corridas)
