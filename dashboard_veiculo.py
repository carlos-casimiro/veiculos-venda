import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')


st.header('DASHBOARD -VEICHLES')
hist_button = st.button('criar histograma')
scatter_button=st.button('criar scatter')


if hist_button:
    st.write('criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig =px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write ('criando um scatter para o conjunto de dados de anúncios de vendas de carros')
    figx = px.scatter(x='price', y='model_year')