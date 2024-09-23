import pandas as pd

# Load the CSV file
df = pd.read_csv('output/filtered_ufsc.csv', sep=',')  # Adjust the sep if needed

# Convert 'REMUNERACAO_BASICA_BRUTA' to numeric, removing any commas
df['REMUNERACAO_BASICA_BRUTA'] = df['REMUNERACAO_BASICA_BRUTA'].str.replace('.', '').str.replace(',', '.').astype(float)

# Convert 'REMUNERACAO_APOS_DEDUCOES' to numeric, removing any commas
df['REMUNERACAO_APOS_DEDUCOES'] = df['REMUNERACAO_APOS_DEDUCOES'].str.replace('.', '').str.replace(',', '.').astype(float)

df['DEDUCOES'] = abs(df['REMUNERACAO_BASICA_BRUTA'] - df['REMUNERACAO_APOS_DEDUCOES'])

# Group by 'DESCRICAO_CARGO' and calculate the average
average_salary = df.groupby('DESCRICAO_CARGO')['DEDUCOES'].mean().reset_index()

average_salary.to_csv('output/average_deductions.csv', index=False)

# Print the results
print(average_salary)
