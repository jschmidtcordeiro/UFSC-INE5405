# Read both CSV files
# data1 <- read.csv("output/cadastro_filtered_file.csv", header = TRUE, sep = ",", fileEncoding = "latin1")
# data2 <- read.csv("output/remuneracao_filtered_file.csv", header = TRUE, sep = ",", fileEncoding = "latin1")
data1 <- read.csv("202405_Servidores_SIAPE/202405_Cadastro.csv", header = TRUE, sep = ";", fileEncoding = "latin1")
data2 <- read.csv("202405_Servidores_SIAPE/202405_Remuneracao.csv", header = TRUE, sep = ";", fileEncoding = "latin1")

# Assuming the column to merge on is called 'ID' in both data frames (replace with actual column name)
combined_data <- merge(data1, data2, by.x = "NOME", by.y = "NOME")  # Replace 'ID' with the actual column names

# Write the result to a new CSV file
write.csv(combined_data, "output/combined_result.csv", row.names = FALSE)

print("Combined CSV created: output/combined_result.csv")
