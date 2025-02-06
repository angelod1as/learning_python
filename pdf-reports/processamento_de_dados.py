from pathlib import Path
import pandas as pd


def carregar_tabelas(
    mes_referencia,
    pasta_dados,
    arquivo_excel,
):
    caminho_dados = Path(pasta_dados / arquivo_excel)
    dados_brutos = pd.read_excel(caminho_dados)
    dados_filtrados = filtrar_dados_pelo_mes(
        dados_brutos=dados_brutos, mes_referencia=mes_referencia
    )
    tabela_vendas = gerar_numero_de_vendas(dados=dados_filtrados)
    tabela_volume = gerar_volume_de_vendas(dados=dados_filtrados)
    tabela_ticket_medio = gerar_ticket_medio(dados=dados_filtrados)
    return {
        tabela_vendas: tabela_vendas,
        tabela_volume: tabela_volume,
        tabela_ticket_medio: tabela_ticket_medio,
    }


def filtrar_dados_pelo_mes(dados_brutos, mes_referencia, coluna_data_hora="Data/Hora"):
    filtro = dados_brutos[coluna_data_hora].apply(
        lambda dt: dt.strftime("%Y-%m") == mes_referencia
    )
    dados_filtrados = dados_brutos.loc[filtro]
    if dados_filtrados.empty:
        raise ValueError(
            f"Nenhum dado encontrado para o mês {mes_referencia}. Confirme se o mês de referência está no formato YYYY-MM"
        )
    return dados_filtrados


def gerar_numero_de_vendas(
    dados,
    coluna_vendedor="Vendedor",
    coluna_Produto="Produto",
    coluna_Quantidade="Quantidade",
):
    return dados.pivot_table(
        index=coluna_vendedor,
        columns=coluna_Produto,
        values=coluna_Quantidade,
        aggfunc="sum",
        margins=True,
        margins_name="TOTAL",
    ).sort_values(by="TOTAL")


def gerar_volume_de_vendas(
    dados,
    coluna_vendedor="Vendedor",
    coluna_Produto="Produto",
    coluna_volume="Valor Venda",
):
    return dados.pivot_table(
        index=coluna_vendedor,
        columns=coluna_Produto,
        values=coluna_volume,
        aggfunc="sum",
        margins=True,
        margins_name="TOTAL",
    ).sort_values(by="TOTAL")


def gerar_ticket_medio(dados, coluna_vendedor="Vendedor", coluna_volume="Valor Venda"):
    return dados.groupby(coluna_vendedor)[[coluna_volume]].mean()
