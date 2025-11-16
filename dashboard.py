import pandas as pd
import streamlit as st
import plotly.express as px

# Importando dados
df = pd.read_csv('./casas_final.csv')

# Configuração da página
st.set_page_config(
    page_title='Preços das casas',
    page_icon='🏠',
    layout='wide'
)

# Condeudo principal
st.title("Influência no preço das casas")
st.markdown("Dashboard feito para desafio técnico da Cati Jr, Analisando fatores que influenciam no preço das casas")
