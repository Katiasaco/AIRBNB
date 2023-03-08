#-----------------------------LIBRERIAS-----------------------------
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import plotly_express as px
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import matplotlib.pyplot as plt
import requests
import os 
import streamlit.components.v1 as components
from unicodedata import name
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from PIL import Image
# mapas interactivos
import folium
from folium.plugins import FastMarkerCluster
import geopandas as gpd
from branca.colormap import LinearColormap


#-----------------leer datos--------------------------
df = pd.read_csv (r'C:\Users\katia\.vscode\examplecode\MODULO_2\20-Trabajo Módulo 2\datos\airbnb_anuncios.csv')
st.set_page_config(page_title="AIRBNB - MADRID")


#------------------------SIDEBAR------------------------ 
st.sidebar.title("El tiempo en Madrid")
st.sidebar.write(f'<iframe src="https://www.accuweather.com/en/madrid/94103/weather-forecast/347629" width="" height="600" style="overflow:auto"></iframe>', unsafe_allow_html=True)
url = "https://www.accuweather.com/en/madrid/94103/weather-forecast/347629"
st.sidebar.markdown("[Accuweather](%s)" % url)

#INTRODUCCION ------------

st.title(("AIRBNB EN MADRID"))
st.image(('https://i.likibu.com/destinations/espagne/communaute-de-madrid/madrid-cover.jpg'))



user_name = st.text_input('¿Quieres una alerta de apartamentos disponibles?')
button_press = st.button("Enviar")
if button_press: 
    print(st.header('Gracias por registrarte '+ user_name +' te enviaremos la información tan pronto la recibamos.'))


#----------------------DIVISION DE COLUMNAS ------------------------------------------

st.title('¿Dónde debería alojarme en el airbnb?')
st.write ('La Latina, Chueca,Barrio de las Letras (Huertas),Malasaña,Salamanca, Lavapiés.'
'Madrid es la animada capital española que nunca duerme. A la sombra de la sierra de Guadarrama, en el centro geográfico del país, es un destino cambiante que cuenta con barrios medievales y zonas modernas y chic donde se concentra la actividad económica y de negocios. Las principales atracciones son bonitas viñetas del Barroco, desde la Puerta del Sol hasta el gran Palacio Real, residencia oficial del rey de España pese a no vivir en él. Además de todo esto, puedes seguir los pasos de Cervantes en el Barrio de las Letras y darlo todo por la noche entre sangrías y vinos tintos en Huertas. Pero aún hay más: la capital presume del Triángulo de los Museos, una zona de efervescencia cultural, y ofrece la posibilidad de hacer visitas a las bonitas ciudades de Toledo y Segovia.')
st.write('Aquí tenemos una guía de donde alojarse en Madrid, PLAY VIDEO!')
st.video('https://www.youtube.com/watch?v=e500ssKFYbE')
st.write('Este video es de Youtube')

col1, col2 = st.columns(2)
with col1:
    st.title('')
    def load_lottieurl(url: str):
        r = requests.get (url)
        if r.status_code !=200:
            return None
        return r.json()

    lottie_url_lupa = 'https://assets3.lottiefiles.com/private_files/lf30_eqXMaz.json'
    lottie_lupa = load_lottieurl(lottie_url_lupa)

    st_lottie(lottie_lupa, key='Lupa')



#------------------------------ DIFERENTES PARTES ---------------------
tabs = st.tabs(['PREPROCESAMIENTO','INFORMACIÓN GENERAL','BARRIOS DE MADRID','HABITACIONES', 'DISPONIBILIDAD', ' ECONOMÍA'])      
        
tab_plots = tabs[0]

with tab_plots:

    st.title('Realizaremos el preprocesamiento de los datos antes de hacer el análisis de los mismos.')
    st.write('Leemos el csv')
    foto1=Image.open('1.png')
    st.image(foto1)


    st.write('Vemos si existen duplicados.')
    foto2=Image.open('2.png')
    st.image(foto2)  


    st.write('Vemos el sumatorio de las columnas con datos null.')
    foto3=Image.open('3.png')
    st.image(foto3)  


    st.write('Eliminamos las columnas que tienen demasiados datos null.')
    foto4=Image.open('4.png')
    st.image(foto4)  


    st.write('Vemos el conteo de valores que tenemos en la columna neighbourhood_group.')
    foto5=Image.open('5.png')
    st.image(foto5)  


    st.write('Vemos el número de valores que tiene el array y del tipo que son.')
    foto6=Image.open('6.png')
    st.image(foto6)  


    st.write('Eliminamos los valores null de la columna review_per_month y comprobamos que da 0.')
    foto7=Image.open('7.png')
    st.image(foto7)  


    st.write('Vemos los valores que tenemos con las estadísticas descriptivas de la base de datos.')
    foto8=Image.open('8.png')
    st.image(foto8)  


    st.write('Mostramos los valores corregidos sin valores null y listos para utilizarlos en el analisis.')
    foto9=Image.open('9.png')
    st.image(foto9)  


tab_plots = tabs[1]

with tab_plots:

    st.title('INFORMACIÓN GENERAL')
    st.write('Gráfico de escala de calor donde se muestran los datos globales del dataset.')
    corr = df.corr(method='kendall')
    plt.figure(figsize=(15,8))
    sns.heatmap(corr, annot=True)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()


tab_plots = tabs[2]

with tab_plots:

    st.write('Representación grafica de los grupos de barrios y su importancia.')
    sns.countplot(x= df['neighbourhood_group'])
    fig = plt.gcf()
    fig.set_size_inches(20,5)
    plt.xticks (fontsize=4, rotation=25)
    plt.title('GRUPO DE BARRIOS')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()



    st.write('Los barrios más exclusivos de Madrid se encuentran en la parte central de la ciudad, alrededor del Paseo de la Castellana. Destacan los barrios históricos como Palacio, Salamanca, Chamberí y los Jerónimos, donde podemos encontrar grandes pisos señoriales en edificios perfectamente rehabilitados.')
    foto10=Image.open('barrios.jpg')
    st.image(foto10) 


    st.write('Aqui podemos observar los grupos de barrios que tenemos en Madrid')
    plt.figure(figsize=(10,6))
    sns.scatterplot(x=df.longitude,y=df.latitude,hue=df.neighbourhood_group)
    plt.ioff()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

tab_plots = tabs[3]

with tab_plots:
    sns.countplot(x =df['room_type'], palette="plasma")
    fig = plt.gcf()
    fig.set_size_inches(10,10)
    plt.title('TIPO DE HABITACIÓN Y SU CANTIDAD')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    st.write('Aqui podemos observar el tipo de habitación que encontramos en Madrid')
    plt.figure(figsize=(10,6))
    sns.scatterplot(x=df['longitude'],y=df['latitude'],hue=df.room_type)
    plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

tab_plots = tabs[4]

with tab_plots:

    plt.figure(figsize=(10,10))
    ax = sns.boxplot(data=df, x='neighbourhood_group',y='availability_365',palette='plasma')
    plt.xticks (fontsize=4, rotation=25)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    st.write('Disponibilidad por tipo de habitación.')
    sns.relplot(data = df, x = 'room_type', y = 'price', hue = 'availability_365')
    plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()


    st.write('Disponibilidad por zona')
    plt.figure(figsize=(10,6))
    sns.scatterplot(x=df['longitude'],y=df['latitude'],hue=df.availability_365)
    plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()


tab_plots = tabs [5]

with tab_plots:

    col1, col2 = st.columns(2)
    with col1:

        st.write('En referencia a la economía de Madrid, vamos a ver un gráfico donde nos muestran los alquileres y ventas de apartamentos.')
        foto11=Image.open('alquiler-venta.jpg')
        st.image(foto11)


    with col2:
        st.write('Podemos ver los diferentes precios que tenemos en Madrid')
        df[['price']].value_counts().head(10).plot.pie()
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    col1, col2 = st.columns(2)
    with col1:

        st.write('Vamos a mostrar unos gráficos generales de los diferentes países en los que trabajan con Airbnb.')
        foto12=Image.open('eco_paises.jpg')
        st.image(foto12)
        st.write('El país')

    