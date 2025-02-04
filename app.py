import streamlit as st
from bot_ask import ask  

# Configuration de la page
st.set_page_config(
    page_title="Le Roi Béhanzin",
    page_icon="👑",
    layout="centered"
)

# Appliquer un style personnalisé
st.markdown(""" 
    <style>
        body {
            background-color: #f2e8d3; /* Fond beige clair évoquant la terre */
        }
        .stTextArea textarea {
            border: 2px solid #f2c277; /* Bordure assortie aux couleurs royales */
            border-radius: 10px;
            font-size: 16px;
            padding: 10px;
        }
        .stButton button {
            background-color: #f2c277; /* Couleur dorée royale */
            color: white;
            border-radius: 5px;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #e5a960; /* Couleur plus foncée au survol */
        }
        .response-box {
            background-color: #e5a960; /* Couleur chaude et royale de la bulle */
            padding: 15px;
            border-radius: 10px;
            color: black;
            font-size: 16px;
            margin: 10px 0;
        }
        .user-box {
            background-color: #ffffff; /* Couleur claire de la bulle utilisateur */
            padding: 15px;
            border-radius: 10px;
            color: black;
            font-size: 16px;
            margin: 10px 0;
        }
        
        /* Style pour le bouton "Dénoncer" en bas à droite */
        .denoncer-button {
            position: fixed ;
            bottom: 45px;
            right: 10%;
            background-color: #f2c277; /* Couleur dorée du bouton */
            color: white;
            padding: 10px 25px;
            font-size: 16px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
        }
        .denoncer-button:hover {
            background-color: #e5a960; /* Couleur dorée au survol */
        }
    </style>
""", unsafe_allow_html=True)

# Titre de l'application
st.title("La Voix du Roi Béhanzin 👑")

# Message d'accueil
st.subheader("👋 Bienvenue, je suis le roi Béhanzin !")
st.markdown("""
    Je suis là pour t'écouter, t'informer sur les événements marquants de mon règne et te guider 
    dans la compréhension de l'histoire de notre peuple et de notre résistance face à la colonisation.  
    Si tu cherches des conseils, ou si tu veux connaître des détails sur mon règne, n'hésite pas à me le faire savoir. 🤝
""")

# Entrée utilisateur
user_input = st.text_area(
    "Posez votre question ici 👇",
    placeholder="Exemple : Quelle a été la stratégie qui t'a permis de résister à l'invasion ?"
)

# Bouton pour envoyer la question
if st.button("Envoyer"):
    if user_input.strip():
        with st.spinner("Le roi Béhanzin est en train de répondre..."):
            response = ask(user_input)
        st.markdown('<div class="user-box">' + user_input + '</div>', unsafe_allow_html=True)
        st.markdown('<div class="response-box">' + response + '</div>', unsafe_allow_html=True)
    else:
        st.warning("Veuillez entrer une question avant d'envoyer.")

# Ajout d'une note de confidentialité
st.markdown("""
    ---
    🔒 **Confidentialité garantie :** Toutes vos interactions avec moi, le roi Béhanzin, restent strictement confidentielles.
""")

# Bouton "Dénoncer" en bas à droite (adapté pour l'inspiration historique)
st.markdown("""
    <a href="https://https://ghinel.vercel.app/" target="_blank">
        <button class="denoncer-button">Découvrir Ghinel</button>
    </a>
""", unsafe_allow_html=True)
