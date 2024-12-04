import pandas as pd
from scipy.stats import ttest_ind

# 1. Ler o arquivo CSV
file_path = "output/filtered_ufsc.csv"
data = pd.read_csv(file_path)

# 2. Preprocessamento
data['REMUNERACAO_BASICA_BRUTA'] = data['REMUNERACAO_BASICA_BRUTA'].str.replace(
    ',', '.').astype(float)
data['REMUNERACAO_APOS_DEDUCOES'] = data['REMUNERACAO_APOS_DEDUCOES'].str.replace(
    ',', '.').astype(float)

# Verificar se há valores inválidos, como zero, e tratar os casos
print("\nVerificando valores inválidos (zero ou NaN):")
# Remuneração bruta igual a zero
print(data[data['REMUNERACAO_BASICA_BRUTA'] == 0])
# Remuneração após deduções igual a zero
print(data[data['REMUNERACAO_APOS_DEDUCOES'] == 0])

# Remover linhas onde a remuneração básica ou a remuneração após deduções é zero
data = data[(data['REMUNERACAO_BASICA_BRUTA'] > 0) &
            (data['REMUNERACAO_APOS_DEDUCOES'] > 0)]

# Calcular o percentual de deduções
data['PERCENTUAL_DE_DUCOES'] = ((data['REMUNERACAO_BASICA_BRUTA'] - data['REMUNERACAO_APOS_DEDUCOES']) /
                                data['REMUNERACAO_BASICA_BRUTA']) * 100

# 3. Determinar o percentil 75 da remuneração básica bruta
percentile_75 = data['REMUNERACAO_BASICA_BRUTA'].quantile(0.75)

# Separar os grupos
grupo_acima = data[data['REMUNERACAO_BASICA_BRUTA']
                   > percentile_75]['PERCENTUAL_DE_DUCOES']
grupo_abaixo = data[data['REMUNERACAO_BASICA_BRUTA']
                    <= percentile_75]['PERCENTUAL_DE_DUCOES']

# 4. Tratar valores NaN ou inválidos
grupo_acima = grupo_acima.dropna()
grupo_abaixo = grupo_abaixo.dropna()

# Verificar se os grupos têm valores suficientes para o teste
print("\nGrupo acima do percentil 75:")
print(grupo_acima.describe())

print("\nGrupo abaixo do percentil 75:")
print(grupo_abaixo.describe())

# 5. Teste T para duas amostras independentes
if len(grupo_acima) > 1 and len(grupo_abaixo) > 1:
    # Teste T para duas amostras independentes
    stat, p_value = ttest_ind(
        grupo_acima, grupo_abaixo, alternative='greater', equal_var=False)

    # 6. Interpretar os resultados
    alpha = 0.05
    print(f"\nEstatística do teste: {stat}")
    print(f"P-valor: {p_value}")

    if p_value < alpha:
        print("Rejeitamos H0: A média do percentual de deduções é maior para servidores com remuneração bruta acima do percentil 75.")
    else:
        print("Falha em rejeitar H0: Não há evidência suficiente para afirmar que a média do percentual de deduções é maior para servidores com remuneração bruta acima do percentil 75.")
else:
    print("\nErro: Um ou ambos os grupos têm valores insuficientes para realizar o teste.")
