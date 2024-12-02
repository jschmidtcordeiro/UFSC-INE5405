import pandas as pd
import numpy as np
from scipy import stats

def load_data(file_path):
    try:
        return pd.read_csv(file_path, encoding='utf-8')
    except UnicodeDecodeError:
        return pd.read_csv(file_path, encoding='ISO-8859-1')

def calculate_statistics(series):
    """Calculate basic statistical measures for a numeric series"""
    stats_dict = {
        'Mean': np.mean(series),
        'Median': np.median(series),
        'Mode': stats.mode(series)[0],
        'Variance': np.var(series),
        'Standard Deviation': np.std(series),
        'Range': series.max() - series.min(),
        'Coefficient of Variation': (np.std(series) / np.mean(series)) * 100,
        'Minimum': series.min(),
        'Maximum': series.max(),
        'Q1': np.percentile(series, 25),
        'Q3': np.percentile(series, 75),
        'IQR': np.percentile(series, 75) - np.percentile(series, 25)
    }
    return stats_dict

def main():
    # Load the data
    file_path = 'output/filtered_ufsc.csv'
    df = load_data(file_path)
    
    # Convert salary column to numeric, replacing comma with dot
    df['REMUNERACAO_BASICA_BRUTA'] = df['REMUNERACAO_BASICA_BRUTA'].str.replace(',', '.').astype(float)
    
    # Calculate statistics for salary
    salary_stats = calculate_statistics(df['REMUNERACAO_BASICA_BRUTA'])
    
    # Print results
    print("\n=== Statistical Analysis of Basic Gross Remuneration ===")
    print("\nCentral Tendency Measures:")
    print(f"Mean: R$ {salary_stats['Mean']:.2f}")
    print(f"Median: R$ {salary_stats['Median']:.2f}")
    print(f"Mode: R$ {salary_stats['Mode']:.2f}")
    
    print("\nDispersion Measures:")
    print(f"Variance: {salary_stats['Variance']:.2f}")
    print(f"Standard Deviation: R$ {salary_stats['Standard Deviation']:.2f}")
    print(f"Range: R$ {salary_stats['Range']:.2f}")
    print(f"Coefficient of Variation: {salary_stats['Coefficient of Variation']:.2f}%")
    
    print("\nPosition Measures:")
    print(f"Minimum: R$ {salary_stats['Minimum']:.2f}")
    print(f"Maximum: R$ {salary_stats['Maximum']:.2f}")
    print(f"First Quartile (Q1): R$ {salary_stats['Q1']:.2f}")
    print(f"Third Quartile (Q3): R$ {salary_stats['Q3']:.2f}")
    print(f"Interquartile Range (IQR): R$ {salary_stats['IQR']:.2f}")

if __name__ == "__main__":
    main()
