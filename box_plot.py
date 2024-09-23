import pandas as pd

import plotly.express as px

# Load the filtered data from the CSV file
filtered_data = pd.read_csv('./output/filtered_ufsc.csv')

# Convert the 'DATA_INGRESSO_CARGOFUNCAO' column to datetime
filtered_data['DATA_INGRESSO_CARGOFUNCAO'] = pd.to_datetime(filtered_data['DATA_INGRESSO_CARGOFUNCAO'])

# Replace the comma with a dot in the 'REMUNERACAO_BASICA_BRUTA' column
filtered_data['REMUNERACAO_BASICA_BRUTA'] = filtered_data['REMUNERACAO_BASICA_BRUTA'].str.replace(',', '.')

# Convert the 'REMUNERACAO_BASICA_BRUTA' column to numeric
filtered_data['REMUNERACAO_BASICA_BRUTA'] = pd.to_numeric(filtered_data['REMUNERACAO_BASICA_BRUTA'])

# Extract the year from the 'DATA_INGRESSO_CARGOFUNCAO' column
filtered_data['YEAR'] = filtered_data['DATA_INGRESSO_CARGOFUNCAO'].dt.year

# Sort the data by the 'YEAR' column in ascending order
filtered_data = filtered_data.sort_values('YEAR')

# Group the data by 'YEAR' and calculate the mean of 'REMUNERACAO_BASICA_BRUTA'
grouped_data = filtered_data.groupby('YEAR')['REMUNERACAO_BASICA_BRUTA'].mean().reset_index()

# Create the plot using Plotly
fig = px.bar(grouped_data, x='YEAR', y='REMUNERACAO_BASICA_BRUTA')

# Show the plot
fig.show()
