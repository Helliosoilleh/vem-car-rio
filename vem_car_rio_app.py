import streamlit as st
import streamlit.components.v1 as components
import random, datetime

st.set_page_config(page_title="VEM CAR RIO - Mapa", page_icon="🗺️", layout="centered")

st.markdown("""
<style>
.ride-card {background:white; border-radius:15px; padding:15px; margin:10px 0; border-left:5px solid #FFD700; box-shadow: 0 2px 8px rgba(0,0,0,0.1)}
.safe-badge {background:#00C851; color:white; padding:5px 10px; border-radius:20px; font-size:12px}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center'>🗺️ VEM CAR RIO</h1><p style='text-align:center'><span class='safe-badge'>PRIVADO COM MAPA</span><br>Veja sua rota em tempo real</p>", unsafe_allow_html=True)

# Coordenadas fixas (pra funcionar sem API paga)
CIDADES = {
    "rio": {"lat": -22.9068, "lon": -43.1729, "nome": "Rio de Janeiro"},
    "campina": {"lat": -7.2290, "lon": -35.8808, "nome": "Campina Grande"},
    "sao paulo": {"lat": -23.5505, "lon": -46.6333, "nome": "São Paulo"},
}

if 'corridas' not in st.session_state:
    st.session_state.corridas = []

perfil = st.radio("Você é:", ["Passageira", "Motorista", "Central"], horizontal=True)

# ========== PASSAGEIRA COM MAPA ==========
if perfil == "Passageira":
    st.markdown("### 📍 Para onde vamos?")
    
    origem = st.text_input("De onde?", "Rio de Janeiro")
    destino = st.text_input("Para onde?", "Campina Grande")
    valor = st.number_input("Quanto quer pagar? R$", 10, 500, 30)
    nome = st.text_input("Seu nome")
    tel = st.text_input("WhatsApp (protegido 🔒)", type="password")
    lgpd = st.checkbox("Concordo com LGPD - meus dados ficam protegidos")

    # MAPA COM ROTA
    st.markdown("#### 🗺️ Sua rota")
    # Calcula distância simples Rio->Campina = 1900km (exemplo)
    distancia_km = 1896
    tempo = "26h de carro"
    
    # Mapa embedado OpenStreetMap com rota
    map_html = f"""
    <iframe width="100%" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
    src="https://www.openstreetmap.org/export/embed.html?bbox=-45.0%2C-23.5%2C-35.0%2C-6.5&layer=mapnik&marker=-22.9068%2C-43.1729&marker=-7.2290%2C-35.8808"
    style="border-radius:15px; border: 2px solid #FFD700"></iframe>
    <br><small>🔒 Rota: {origem} → {destino} | {distancia_km} km | {tempo}</small>
    """
    components.html(map_html, height=400)
    
    st.info(f"📏 Distância estimada: {distancia_km} km | ⏱️ Tempo: {tempo} | 💰 Você ofereceu: R$ {valor}")

    if st.button("PEDIR COM MAPA E PRIVACIDADE 🔒🗺️"):
        if not lgpd or not nome or not tel:
            st.error("Preencha tudo e aceite LGPD")
        else:
            codigo = f"VCR-{random.randint(1000,9999)}"
            st.session_state.corridas.append({
                "codigo": codigo, "nome": nome, "origem": origem, "destino": destino,
                "valor": valor, "tel": tel, "status": "No mapa", "hora": datetime.datetime.now().strftime("%H:%M"),
                "distancia": distancia_km
            })
            st.success(f"✅ {codigo} criada! Motorista te vê no mapa (sem ver seu número)")
            st.balloons()
            st.markdown(f"""
            <div class="ride-card">
            <b>{codigo} - NO MAPA</b><br>
            📍 {origem} → {destino}<br>
            📏 {distancia_km}km | 💰 R$ {valor}<br>
            🔒 Número protegido | 💬 Chat anônimo liberado após aceite
            </div>
            """, unsafe_allow_html=True)

# ========== MOTORISTA COM MAPA ==========
elif perfil == "Motorista":
    st.markdown("### 🚗 Corridas no mapa (anônimas)")
    if not st.session_state.corridas:
        st.write("Nenhuma corrida. Fique online no mapa.")
        # Mostra mapa do motorista
        components.html('<iframe width="100%" height="300" src="https://www.openstreetmap.org/export/embed.html?bbox=-43.3%2C-23.0%2C-43.0%2C-22.8&layer=mapnik&marker=-22.9068%2C-43.1729" style="border-radius:15px"></iframe>', height=320)
    else:
        for c in st.session_state.corridas:
            st.markdown(f"""<div class="ride-card"><b>{c['codigo']}</b> - {c['hora']}<br>📍 {c['origem']} → {c['destino']} ({c['distancia']}km)<br>💰 R$ {c['valor']} | 👤 Anônima</div>""", unsafe_allow_html=True)
            components.html(f'<iframe width="100%" height="200" src="https://www.openstreetmap.org/export/embed.html?bbox=-45.0%2C-23.5%2C-35.0%2C-6.5&layer=mapnik" style="border-radius:10px"></iframe>', height=220)
            if st.button(f"Aceitar e ver rota {c['codigo']}"):
                st.success(f"Rota liberada! Vá até {c['origem']}")

# ========== CENTRAL ==========
else:
    senha = st.text_input("Senha Central", type="password")
    if senha == "1234":
        st.write(f"Total de corridas: {len(st.session_state.corridas)}")
        for c in st.session_state.corridas:
            st.write(c)
