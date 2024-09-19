source("functions/get-headers.R")
source("functions/select-headers.R")
source("functions/retain-rows-with-string.R")

# Example usage
# Path to your file
# file_path <- "202405_Servidores_SIAPE/202405_Cadastro.csv"
file_path <- "output/combined_result.csv"

# Path for the new file
output_file_path <- "output/combined_result.csv"

# List of headers to select (adjust this list as needed)
headers_to_select <- c(
  "NOME",
  "TIPO_VINCULO",
  "DESCRICAO_CARGO",
  # "UORG_LOTACAO",
  # "ORG_LOTACAO",
  "UORG_EXERCICIO",
  "ORG_EXERCICIO",
  "SITUACAO_VINCULO",
  "JORNADA_DE_TRABALHO",
  "DATA_INGRESSO_CARGOFUNCAO",
  "DATA_INGRESSO_ORGAO",
  "REMUNERAÃ.Ã.O.BÃ.SICA.BRUTA..R..",
  "REMUNERAÃ.Ã.O.APÃ.S.DEDUÃ.Ã.ES.OBRIGATÃ.RIAS..R..",
  "TOTAL.DE.VERBAS.INDENIZATÃ.RIAS..R....."
)  # Replace with your actual headers

# Create a new file with only the selected headers
# select_headers(file_path, headers_to_select, output_file_path)

# Get and display headers
# headers <- get_headers(file_path)

data <- read.csv(file_path, header = TRUE, sep = ",", fileEncoding = "latin1")

# Remove rows where "specific_string" appears in the "column_name"
cleaned_data <- retain_rows_with_string(data, "ORG_EXERCICIO", "Universidade Federal de Santa Catarina")

# Write the filtered data back to a CSV file
write.csv(cleaned_data, "output/filtered_ufsc.csv", row.names = FALSE, fileEncoding = "latin1")

print("Filtered CSV created: filtered_result.csv")