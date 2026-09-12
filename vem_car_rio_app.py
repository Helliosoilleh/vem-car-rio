import streamlit as st

st.set_page_config(page_title="VEM CAR RIO", page_icon="🚗", layout="centered")

st.markdown("""
<style>
    .stButton>button { background-color: #FFD700; color: #000; font-weight: bold; border-radius: 12px; width: 100%; height: 50px; border: none; }
    h1 { color: #0055A4; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🚗 VEM CAR RIO</h1><p style='text-align:center;'><i>Vem cá, Rio! Seu transporte da galera.</i></p>", unsafe_allow_html=True)

if 'corridas' not in st.session_state:
    st.session_state.corridas = []
if 'usuarios' not in st.session_state:
    st.session_state.usuarios = []

aba = st.selectbox("O que você quer fazer?", ["🧍 Quero uma carona (Passageiro)", "🚙 Quero dirigir (Motorista)", "📝 Me cadastrar"])

if aba == "📝 Me cadastrar":
    st.subheader("Cadastro VEM CAR RIO")
    nome = st.text_input("Seu nome")
    zap = st.text_input("Seu WhatsApp (com DDD)")
    tipo = st.radio("Você quer ser:", ["Passageiro", "Motorista", "Os dois"])
    if st.button("ENTRAR PRO VEM CAR RIO"):
        if nome and zap:
            st.session_state.usuarios.append({"nome": nome, "zap": zap, "tipo": tipo})
            st.success(f"Bem-vindo(a), {nome}! Você já faz parte do VEM CAR RIO! 💛💙")
            st.balloons()
        else:
            st.warning("Preenche nome e zap!")

elif aba == "🧍 Quero uma carona (Passageiro)":
    st.subheader("Pedir um VEM CAR")
    origem = st.text_input("De onde você está? Ex: Madureira")
    destino = st.text_input("Para onde vai? Ex: Copacabana")
    obs = st.text_area("Observação (opcional)")
    if st.button("🚨 CHAMAR VEM CAR AGORA"):
        if origem and destino:
            nova = {"origem": origem, "destino": destino, "obs": obs, "status": "Aguardando motorista"}
            st.session_state.corridas.append(nova)
            st.success(f"Pronto! Pedido de {origem} para {destino} enviado para os motoristas! Fica de olho no WhatsApp.")
            st.balloons()
        else:
            st.warning("Coloca de onde e para onde!")

else:
    st.subheader("Corridas pedidas pela galera")
    if not st.session_state.corridas:
        st.info("Nenhum pedido no momento. Fica online!")
    else:
        for i, c in enumerate(reversed(st.session_state.corridas)):
            st.markdown(f"**📍 {c['origem']} → {c['destino']}** | Obs: {c['obs']} | Status: {c['status']}")
            if st.button(f"Aceitar corrida {i+1} - Chamar no Zap", key=f"btn_{i}"):
                st.success("Corrida aceita! Aqui abriria o WhatsApp do passageiro.")

st.caption("VEM CAR RIO v1.0 - Criado por você e por mim 🚀")