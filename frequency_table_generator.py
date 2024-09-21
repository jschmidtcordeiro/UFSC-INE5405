import pandas as pd

# Load the CSV file with encoding handling
file_path = 'output/filtered_ufsc.csv'

try:
    # Try loading the file with the correct encoding
    df = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    # If UTF-8 fails, fall back to ISO-8859-1
    df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Drop the 'name' column if it exists
if 'name' in df.columns:
    df = df.drop(columns=['name'])

# Generate frequency tables for each column and save them to a CSV file
for column in df.columns:
    frequency_table = df[column].value_counts().reset_index()  # Convert Series to DataFrame
    frequency_table.columns = [column, 'count']  # Rename columns
    output_path = f'/home/lucas/UFSC-INE5405/output/frequency_{column}.csv'
    
    # Save the frequency table to CSV
    frequency_table.to_csv(output_path, index=False)

    print(f"Frequency table for '{column}' saved to {output_path}.")
