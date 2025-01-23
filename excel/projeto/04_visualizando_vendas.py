from pathlib import Path
from datetime import date, datetime, timedelta

import streamlit as st
import pandas as pd

COMISSAO = 0.08

pasta_datasets = Path(__file__).parent.parent / "datasets"
df_vendas = pd.read_csv(
    pasta_datasets / "vendas.csv", decimal=",", sep=";", index_col=0, parse_dates=True
)
df_filiais = pd.read_csv(
    pasta_datasets / "filiais.csv", decimal=",", sep=";", index_col=0
)
df_produtos = pd.read_csv(
    pasta_datasets / "produtos.csv", decimal=",", sep=";", index_col=0
)

df_produtos = df_produtos.rename(columns={"nome": "produto"})
df_vendas = df_vendas.reset_index()

df_vendas = pd.merge(
    left=df_vendas, right=df_produtos[["preco", "produto"]], on="produto", how="left"
)

df_vendas.set_index("data", inplace=True)
df_vendas["comissao"] = df_vendas["preco"] * COMISSAO

data_default = df_vendas.index.date.max()
data_inicio = st.sidebar.date_input("Data Inicial", data_default - timedelta(days=6))
data_final = st.sidebar.date_input("Data Final", data_default)

df_vendas_cortado = df_vendas[
    (df_vendas.index.date >= data_inicio)
    & (df_vendas.index.date < data_final + timedelta(days=1))
]

st.markdown("# Números gerais")

col11, col12 = st.columns(2)
valor_vendas = f"R$ {df_vendas_cortado['preco'].sum()}"
col11.metric("Valor de vendas no período", valor_vendas)
col12.metric("Quantidade de vendas", df_vendas_cortado["preco"].count())
st.divider()

principal_filial = df_vendas_cortado["filial"].value_counts().index[0]
st.markdown(f"# Principal filial: {principal_filial}")

col21, col22 = st.columns(2)
df_vendas_filial = df_vendas_cortado[df_vendas_cortado["filial"] == principal_filial]
valor_vendas = f"R$ {df_vendas_filial['preco'].sum()}"
col21.metric("Valor de vendas no período", valor_vendas)
col22.metric(
    "Quantidade de vendas",
    df_vendas_filial["preco"].count(),
)
st.divider()

principal_vendedor = df_vendas_cortado["vendedor"].value_counts().index[0]
st.markdown(f"# Principal vendedor: {principal_vendedor}")

col31, col32 = st.columns(2)
df_vendas_vendedor = df_vendas_cortado[
    df_vendas_cortado["vendedor"] == principal_vendedor
]
valor_vendas = f"R$ {df_vendas_vendedor['preco'].sum():.2f}"
valor_comissao = f"R$ {df_vendas_vendedor['comissao'].sum():.2f}"
col31.metric("Valor de vendas no período", valor_vendas)
col32.metric("Comissão", valor_comissao)
