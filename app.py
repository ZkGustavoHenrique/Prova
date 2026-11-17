import pandas as pd


df = pd.read_csv("dados_transporte_bh.csv", sep=";")
df.columns = df.columns.str.strip()
df["LINHA"] = df["LINHA"].astype(str).str.strip()
df = df[~df["PC"].isin([0, 3])]
viagens = df.groupby("LINHA").size().reset_index(name="viagens")

fig_empilhado = px.bar(
dados_empilhado,
x="Bairro",
y="Valor",
color="Dimensao",
barmode="stack",
title="Composição do IQVU por Dimensão — Ano 2016 (Barras Empilhadas)",
template="plotly_dark"
)