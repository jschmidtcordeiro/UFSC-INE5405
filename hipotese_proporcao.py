import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

# 1. Ler o arquivo CSV
file_path = "output/filtered_ufsc.csv" 
data = pd.read_csv(file_path)

# 2. Processar a coluna "JORNADA_DE_TRABALHO"
# Verificar os valores únicos para identificar as categorias
print("Valores únicos na coluna JORNADA_DE_TRABALHO:")
print(data['JORNADA_DE_TRABALHO'].unique())

# Criar uma variável binária: 1 para "40 HORAS SEMANAIS", 0 para outras jornadas
data['JORNADA_40H'] = data['JORNADA_DE_TRABALHO'].str.contains("40 HORAS", na=False).astype(int)

# 3. Contar os casos para as proporções
total_servidores = len(data)
servidores_40h = data['JORNADA_40H'].sum()
servidores_outros = total_servidores - servidores_40h

# Exibir as contagens
print(f"\nTotal de servidores: {total_servidores}")
print(f"Servidores com 40 horas semanais: {servidores_40h}")
print(f"Servidores com outras jornadas: {servidores_outros}")

# 4. Teste Z para proporções
# Proporção esperada para "outras jornadas"
prop_outros = servidores_outros / total_servidores
count = servidores_40h  # Número de sucessos (servidores com 40h)
nobs = total_servidores  # Tamanho total da amostra

# Realizar o teste unilateral (alternative='larger')
stat, p_value = proportions_ztest(count, nobs, prop_outros, alternative='larger')

# 5. Resultados do teste
alpha = 0.05
print(f"\nEstatística do teste Z: {stat}")
print(f"P-valor: {p_value}")

if p_value < alpha:
    print("Rejeitamos H0: A proporção de servidores com 40 horas semanais é maior do que a de outras jornadas.")
else:
    print("Falha em rejeitar H0: Não há evidência suficiente para concluir que a proporção de servidores com 40 horas semanais é maior.")
