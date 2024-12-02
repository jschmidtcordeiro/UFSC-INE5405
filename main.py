import pandas as pd
import numpy as np
from scipy import stats

def carregar_dados(caminho_arquivo):
    try:
        return pd.read_csv(caminho_arquivo, encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv(caminho_arquivo, encoding='ISO-8859-1')

def calcular_estatisticas(serie):
    """Calcular medidas estatísticas básicas para uma série numérica"""
    estatisticas_dict = {
        'Média': np.mean(serie),
        'Mediana': np.median(serie),
        'Moda': stats.mode(serie)[0],
        'Variância': np.var(serie),
        'Desvio Padrão': np.std(serie),
        'Amplitude': serie.max() - serie.min(),
        'Coeficiente de Variação': (np.std(serie) / np.mean(serie)) * 100,
        'Mínimo': serie.min(),
        'Máximo': serie.max(),
        'Q1': np.percentile(serie, 25),
        'Q3': np.percentile(serie, 75),
        'IQR': np.percentile(serie, 75) - np.percentile(serie, 25)
    }
    return estatisticas_dict

def print_estatisticas(estatisticas):
    # Imprimir resultados
    print("\n=== Análise Estatística da Remuneração Apos Deduções ===")
    print("\nMedidas de Tendência Central:")
    print(f"Média: R$ {estatisticas['Média']:.2f}")
    print(f"Mediana: R$ {estatisticas['Mediana']:.2f}")
    print(f"Moda: R$ {estatisticas['Moda']:.2f}")
    
    print("\nMedidas de Dispersão:")
    print(f"Variância: {estatisticas['Variância']:.2f}")
    print(f"Desvio Padrão: R$ {estatisticas['Desvio Padrão']:.2f}")
    print(f"Amplitude: R$ {estatisticas['Amplitude']:.2f}")
    print(f"Coeficiente de Variação: {estatisticas['Coeficiente de Variação']:.2f}%")
    
    print("\nMedidas de Posição:")
    print(f"Mínimo: R$ {estatisticas['Mínimo']:.2f}")
    print(f"Máximo: R$ {estatisticas['Máximo']:.2f}")
    print(f"Primeiro Quartil (Q1): R$ {estatisticas['Q1']:.2f}")
    print(f"Terceiro Quartil (Q3): R$ {estatisticas['Q3']:.2f}")
    print(f"Intervalo Interquartil (IQR): R$ {estatisticas['IQR']:.2f}")

def calcular_estatisticas_datas(serie):
    """Calcular medidas estatísticas básicas para uma série de datas"""
    # Converter strings de data para datetime
    datas = pd.to_datetime(serie, format='%d/%m/%Y')
    
    # Calcular a data mais recente e mais antiga
    data_min = datas.min()
    data_max = datas.max()
    
    # Calcular a amplitude em dias
    amplitude_dias = (data_max - data_min).days
    
    # Calcular quartis
    q1 = datas.quantile(0.25)
    mediana = datas.quantile(0.50)
    q3 = datas.quantile(0.75)
    iqr = (q3 - q1).days
    
    # Calcular média
    media = datas.mean()
    
    # Calcular moda
    moda = datas.mode()[0]
    
    estatisticas_dict = {
        'Data mais antiga': data_min,
        'Data mais recente': data_max,
        'Amplitude (dias)': amplitude_dias,
        'Média': media,
        'Mediana': mediana,
        'Moda': moda,
        'Q1': q1,
        'Q3': q3,
        'IQR (dias)': iqr
    }
    return estatisticas_dict

def print_estatisticas_datas(estatisticas):
    print("\n=== Análise Estatística das Datas de Ingresso ===")
    print(f"\nData mais antiga: {estatisticas['Data mais antiga'].strftime('%d/%m/%Y')}")
    print(f"Data mais recente: {estatisticas['Data mais recente'].strftime('%d/%m/%Y')}")
    print(f"Amplitude: {estatisticas['Amplitude (dias)']} dias")
    print(f"\nMédia: {estatisticas['Média'].strftime('%d/%m/%Y')}")
    print(f"Mediana: {estatisticas['Mediana'].strftime('%d/%m/%Y')}")
    print(f"Moda: {estatisticas['Moda'].strftime('%d/%m/%Y')}")
    print(f"\nPrimeiro Quartil (Q1): {estatisticas['Q1'].strftime('%d/%m/%Y')}")
    print(f"Terceiro Quartil (Q3): {estatisticas['Q3'].strftime('%d/%m/%Y')}")
    print(f"Intervalo Interquartil (IQR): {estatisticas['IQR (dias)']} dias")

def calcular_estatisticas_qualitativas(serie):
    """Calcular medidas estatísticas para uma série qualitativa"""
    # Calcular frequências absolutas
    freq_absoluta = serie.value_counts()
    
    # Calcular frequências relativas (percentuais)
    freq_relativa = serie.value_counts(normalize=True) * 100
    
    # Calcular a moda
    moda = serie.mode()[0]
    
    # Número total de categorias
    num_categorias = len(freq_absoluta)
    
    # Criar dicionário com as estatísticas
    estatisticas_dict = {
        'Frequência Absoluta': freq_absoluta,
        'Frequência Relativa': freq_relativa,
        'Moda': moda,
        'Número de Categorias': num_categorias,
        'Total de Observações': len(serie)
    }
    return estatisticas_dict

def print_estatisticas_qualitativas(estatisticas, nome_variavel):
    print(f"\n=== Análise Estatística de {nome_variavel} ===")
    print(f"\nNúmero total de observações: {estatisticas['Total de Observações']}")
    print(f"Número de categorias diferentes: {estatisticas['Número de Categorias']}")
    print(f"Categoria mais frequente (Moda): {estatisticas['Moda']}")
    
    print("\nDistribuição de Frequências:")
    print("\nCategoria | Frequência Absoluta | Frequência Relativa (%)")
    print("-" * 60)
    
    # Combinar frequências absolutas e relativas para impressão
    freq_abs = estatisticas['Frequência Absoluta']
    freq_rel = estatisticas['Frequência Relativa']
    
    for categoria in freq_abs.index:
        print(f"{categoria[:30]:<30} | {freq_abs[categoria]:^18} | {freq_rel[categoria]:>18.2f}")

def main():
    # Carregar os dados
    caminho_arquivo = 'output/filtered_ufsc.csv'
    df = carregar_dados(caminho_arquivo)

    # # Análise dos salários bruto
    # coluna_salario = 'REMUNERACAO_BRUTA'
    # df[coluna_salario] = df[coluna_salario].str.replace(',', '.').astype(float)
    # estatisticas = calcular_estatisticas(df[coluna_salario])
    # print_estatisticas(estatisticas)

    # # Análise dos salários
    # coluna_salario = 'REMUNERACAO_APOS_DEDUCOES'
    # df[coluna_salario] = df[coluna_salario].str.replace(',', '.').astype(float)
    # estatisticas = calcular_estatisticas(df[coluna_salario])
    # print_estatisticas(estatisticas)
    
    # # Análise das datas de ingresso
    # coluna_data = 'DATA_INGRESSO_ORGAO'
    # estatisticas_datas = calcular_estatisticas_datas(df[coluna_data])
    # print_estatisticas_datas(estatisticas_datas)

    # Análise dos cargos
    coluna_cargo = 'DESCRICAO_CARGO'
    estatisticas_cargos = calcular_estatisticas_qualitativas(df[coluna_cargo])
    print_estatisticas_qualitativas(estatisticas_cargos, "Descrição dos Cargos")

if __name__ == "__main__":
    main()
