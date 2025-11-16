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

# Metricas Principais
st.subheader("Metricas gerais")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Média dos preços", f"{df['PrecoVenda'].mean():.2f}")
col2.metric("Menor preço", f"{df['PrecoVenda'].min():.2f}")
col3.metric("Maior preço", f"{df['PrecoVenda'].max():.2f}")
col4.metric("Desvio padrão", f"{df['PrecoVenda'].std():.2f}")

st.markdown("---")

#Principais informações sobre Preço venda

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
   grafico_hist = px.histogram(
            df,
            x='PrecoVenda',
            nbins=30,
            title="Distribuição de Preços",
            labels={'PrecoVenda': 'Preços', 'count': ''}
   )
   grafico_hist.update_layout(title_x=0.1)
   st.plotly_chart(grafico_hist, use_container_width=True)

with col_graf2:
   grafico_box = px.box(
            df,
            x='PrecoVenda',
            title='Distribuição de Preços'
   )
   grafico_hist.update_layout(title_x=0.1)
   st.plotly_chart(grafico_box, use_container_width=True)
