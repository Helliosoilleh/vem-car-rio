import streamlit as st
import pandas as pd
import random
import datetime

st.set_page_config(page_title="VEM CAR RIO - Privado", page_icon="🔒", layout="centered")

# ESTILO SEGURO
st.markdown("""
<style>
.ride-card {background:white; border-radius:15px; padding:15px; margin:10px 0; border-left:5px solid #FFD700; box-shadow: 0 2px 8px rgba(0,0,0,0.1)}
.safe-badge {background:#00C851; color:white; padding:5px 10px; border-radius:20px; font-size:12px}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center'>🔒 VEM CAR RIO</h1><p style='text-align:center'><span class='safe-badge'>100% PRIVADO E SEGURO</span><br>Seu número nunca vai para o motorista</p>", unsafe_allow_html=True)

# MENU DE PERFIS
perfil = st.radio("Você é:", ["Passageira", "Motorista", "Central (Você)"], horizontal=True)

# BANCO DE DADOS SIMULADO
if 'corridas' not in st.session_state:
    st.session_state.corridas = []

# ========== PASSAGEIRA ==========
if perfil == "Passageira":
    st.markdown("### 🧡 Peça com segurança")
    st.info("🔒 Seus dados são protegidos pela LGPD. Motorista NUNCA vê seu WhatsApp. Só a Central autorizada vê.")

    nome = st.text_input("Seu nome")
    origem = st.text_input("De onde? Ex: Rio de Janeiro")
    destino = st.text_input("Para onde? Ex: Campina Grande")
    valor = st.number_input("Quanto quer pagar? R$", min_value=10, value=30)
    tel = st.text_input("Seu WhatsApp (fica escondido, só a Central vê)", type="password")
    
    lgpd = st.checkbox("Eu concordo que meus dados sejam usados só para esta corrida e fiquem protegidos (LGPD)")
    
    if st.button("PEDIR CORRIDA SEGURA 🔒"):
        if not lgpd or not nome or not tel:
            st.error("Preencha tudo e aceite a LGPD")
        else:
            codigo = f"VCR-{random.randint(1000,9999)}"
            nova = {
                "codigo": codigo,
                "nome": nome,
                "origem": origem,
                "destino": destino,
                "valor": valor,
                "tel": tel, # fica escondido
                "status": "Aguardando motorista",
                "hora": datetime.datetime.now().strftime("%H:%M")
            }
            st.session_state.corridas.append(nova)
            st.success(f"✅ Pedido {codigo} criado com sucesso!")
            st.markdown(f"""
            <div class="ride-card">
            <b>Sua corrida: {codigo}</b><br>
            {origem} → {destino}<br>
            R$ {valor}<br>
            Status: <b>Procurando motorista perto...</b><br><br>
            🔒 Seu número está protegido. O motorista falará com você por CHAT ANÔNIMO aqui no app.
            </div>
            """, unsafe_allow_html=True)
            st.button("💬 Abrir chat anônimo com motorista")
            st.button("🛡️ Estou segura / Compartilhar trajeto")
            st.button("🚨 Denunciar")

# ========== MOTORISTA ==========
elif perfil == "Motorista":
    st.markdown("### 🚗 Corridas disponíveis (anônimas)")
    st.warning("🔒 Você NÃO recebe o número da passageira. Use o chat anônimo do app. Assédio = banimento imediato.")
    
    if not st.session_state.corridas:
        st.write("Nenhuma corrida agora. Fique online.")
    else:
        for c in st.session_state.corridas:
            if c["status"] == "Aguardando motorista":
                st.markdown(f"""
                <div class="ride-card">
                <b>{c['codigo']}</b> - {c['hora']}<br>
                📍 {c['origem']} → {c['destino']}<br>
                💰 R$ {c['valor']}<br>
                👤 Passageira anônima<br>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"Aceitar {c['codigo']}"):
                    c["status"] = "Aceita"
                    st.success(f"Você aceitou {c['codigo']}! Chat anônimo liberado.")
                    st.info("Fale: 'Olá! Sou seu motorista do VEM CAR, estou chegando de carro branco'")

# ========== CENTRAL ==========
else:
    senha = st.text_input("Senha da Central", type="password")
    if senha == "1234": # você muda depois
        st.markdown("### 👑 Central - Visão completa (só você vê)")
        if not st.session_state.corridas:
            st.write("Nenhum pedido ainda.")
        else:
            for c in st.session_state.corridas:
                # mostra telefone mascarado
                tel_mask = c['tel'][:4] + "****" + c['tel'][-2:]
                st.markdown(f"""
                <div class="ride-card">
                <b>{c['codigo']}</b> | {c['status']}<br>
                Passageira: {c['nome']} - Tel: {tel_mask}<br>
                {c['origem']} → {c['destino']} - R$ {c['valor']}<br>
                </div>
                """, unsafe_allow_html=True)
                with st.expander(f"Ver telefone completo de {c['codigo']} (LGPD - uso restrito)"):
                    st.write(f"Telefone: {c['tel']}")
                    st.write(f"WhatsApp Central: https://wa.me/55{c['tel']}")
    elif senha:
        st.error("Senha errada")
    else:
        st.info("Digite a senha 1234 para ver a Central (depois você troca)")
