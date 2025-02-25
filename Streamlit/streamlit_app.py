import streamlit as st
#import folium
#from streamlit_folium import st_folium
#from pyproj import Geod
#import pandas as pd
#import numpy as np
#import pickle
#import joblib
#import cloudpickle
#import streamlit.components.v1 as components
import requests
from PIL import Image
from io import BytesIO
#import sklearn
#import lime


from page_intro import page_intro
from page_presentation import presentation
from page_localisation import localisation
from page_prediction import prediction
from page_visualisation import visualisation
from page_pretraitement import pretraitement
from page_modelisation1 import modelisation1
from page_modelisation2 import modelisation2
from page_conclusion import conclusion

def main():
    # Sidebar
    pages = {
        "Presentation":page_intro,
        "Presentation des données": presentation,
        "Visualisation géographique des données": localisation,
        "Visualisation des données": visualisation,
        "Prétraitement des données": pretraitement,
        "Modélisation 1 - prédiction variable continue": modelisation1,
        "Modélisation 2 - prédiction variable discrète": modelisation2,
        "Prédiction à l'aide du modèle " : prediction,
        "Conclusion et prespective": conclusion
    }

    # Barre latérale avec des boutons radio pour chaque page
    selected_page = st.sidebar.radio("Choisis une page", list(pages.keys()))

    # Appeler la fonction correspondant à la page sélectionnée
    pages[selected_page]()

    st.sidebar.markdown("""
        Auteurs : 
        * Anne DUBOIS 
        * Christelle TESSIER <a href="https://www.linkedin.com/in/christelle-tessier-368899196" target="_blank">
            <img src="data:image/png;base64,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" alt="LinkedIn" width="30" height="30">
          </a>
        * Hao LA
        """, unsafe_allow_html=True)
    
    image_url = "https://s3-eu-west-1.amazonaws.com/tpd/logos/5defb89bc1213200011e72d5/0x0.png"
    #st.image(image_url, width=None) # Affiche l'image à sa taille originale pour obtenir les dimensions.

    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    original_width, original_height = img.size

    # Calculer la nouvelle largeur (20% de la largeur originale)
    new_width = int(original_width * 0.20)

    st.sidebar.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="{image_url}" width="{new_width}">
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()