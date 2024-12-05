import pandas as pd
from scipy.stats import pearsonr
import datetime as dt

# 1. Ler o arquivo CSV
file_path = "output/filtered_ufsc.csv"
data = pd.read_csv(file_path)

# 2. Preprocessamento
# Remover possíveis caracteres indesejados nas colunas numéricas
data['REMUNERACAO_APOS_DEDUCOES'] = data['REMUNERACAO_APOS_DEDUCOES'].str.replace(',', '.').astype(float)

# Converter a data de ingresso para um formato numérico (número de dias desde uma data de referência)
data['DATA_INGRESSO_ORGAO'] = pd.to_datetime(data['DATA_INGRESSO_ORGAO'], format='%d/%m/%Y', errors='coerce')
data['DIAS_INGRESSO'] = (data['DATA_INGRESSO_ORGAO'] - pd.Timestamp('1900-01-01')).dt.days

# Remover valores inválidos
data = data.dropna(subset=['DIAS_INGRESSO', 'REMUNERACAO_APOS_DEDUCOES'])

# 3. Verificar os dados
print("\nAmostra dos dados utilizados:")
print(data[['DATA_INGRESSO_ORGAO', 'DIAS_INGRESSO', 'REMUNERACAO_APOS_DEDUCOES']].head())

# 4. Testar a relação entre as variáveis (correlação de Pearson)
correlation, p_value = pearsonr(data['DIAS_INGRESSO'], data['REMUNERACAO_APOS_DEDUCOES'])

# 5. Exibir os resultados
print(f"\nCoeficiente de correlação de Pearson: {correlation}")
print(f"P-valor: {p_value}")

# Interpretar os resultados
alpha = 0.05
if p_value < alpha:
    if correlation < 0:
        print("Rejeitamos H0: Existe uma correlação negativa significativa entre a data de ingresso e a remuneração após deduções.")
    else:
        print("Rejeitamos H0: Existe uma correlação positiva significativa entre a data de ingresso e a remuneração após deduções.")
else:
    print("Falha em rejeitar H0: Não há evidência suficiente para concluir que existe uma correlação significativa.")
