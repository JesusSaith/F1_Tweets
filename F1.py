import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.markdown("<h1 style='text-align: center; color: white;'>F1 TWEETS</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Meneses Conde Jesús Saith</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>zs19004877@estudiantes.uv.mx</h3>", unsafe_allow_html=True)

st.sidebar.image("form.png")

DATA_URL = ('F1_tweets.csv')
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

def filter_data_by_user(name):
    data['user_name'].fillna(value='', inplace=True)
    filtered_data_user = data[data['user_name'].str.upper().str.contains(name)]
    return filtered_data_user

def filter_data_by_location(location):
    filtered_data_location = data[data['user_location'] == location]
    return filtered_data_location

data = load_data(5000)

sidebar = st.sidebar

if st.sidebar.checkbox('Mostrar todos los Tweets'):
    st.subheader('Todos los Tweets')
    st.write(data)

userName = st.sidebar.text_input('User Name:')
btnBuscar = st.sidebar.button('Buscar User Name')

if (btnBuscar):
    data_user = filter_data_by_user(userName.upper())
    count_row = data_user.shape[0]  
    st.write(f"Total de Usuarios: {count_row}")
    st.write(data_user)

select_location = st.sidebar.selectbox("Seleccionar Locacion", data['user_location'].unique())
btnFilterbyLocation = st.sidebar.button('Locacion')

if (btnFilterbyLocation):
    filterbyloca = filter_data_by_location(select_location)
    count_row = filterbyloca.shape[0]  
    st.write(f"Total de Locaciones : {count_row}")

    st.dataframe(filterbyloca)

st.markdown("<h4 style='text-align: center; color: white;'>Este Histograma muestra desde que dispositivos son posteados los tweets y con que frecuencia</h4>", unsafe_allow_html=True)
followers = data['source']
fig, ax = plt.subplots()
ax.hist(followers, bins=4, range=(0, 3), color="red", ec="black")
ax.set_xlabel('Dispositivos')
ax.set_ylabel('Frecuencia')
ax.set_title('Histograma de los dispositivos donde se mandan los tweets ')

st.pyplot(fig)

columnas = ['Follow', 'Friends']
columna_seleccionada = st.sidebar.multiselect('Selecciona el tipo de datos de usuario', columnas)
userfollow = data['user_followers'].sum()
userfriends = data['user_friends'].sum()

if columna_seleccionada:
    st.markdown("<h4 style='text-align: center; color: white;'>Muestra el Total de seguidores y amigos en comun que tienen todos los usuarios</h4>", unsafe_allow_html=True)
    df = pd.DataFrame({
    'Usuario': ['Follow', 'Friends'],
    'Total': [userfollow, userfriends]
    })
    fig = px.bar(df, x='Usuario', y='Total')
    st.plotly_chart(fig, use_container_width=True)



follow=data['user_followers']
friends=data['user_name']
fav=data['user_favourites']
dis=data['source']


st.markdown("<h4 style='text-align: center; color: white;'>Muestra el Total de followers que tiene los usuarios ademas de mostrar que dipositivos usas esos usuairios</h4>", unsafe_allow_html=True)
fig_perf_work=px.scatter(data,
                         x=friends,
                         y=follow,
                         size=fav,
                         color=dis,
                         title="grafica scatter ",
                         labels=dict(Date="Fecha de Tweet", 
                                     source="Dispositivo", favo="Favoritos"),
                         template="plotly_white")
fig_perf_work.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_perf_work)







