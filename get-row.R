# Load the CSV file
data <- read.csv("output/combined_result.csv", header = TRUE, sep = ",", fileEncoding = "latin1")

# Ensure the first column is of character type
data[, 1] <- as.character(data[, 1])

# Filter rows where the first column contains the name "JERUSA", handling NA values
filtered_data <- data[!is.na(data[, 1]) & data[, 1] == "JERUSA MARCHI", ]

# Check if any rows are found
if (nrow(filtered_data) > 0) {
  # Print the result in a nice format using knitr::kable
  library(knitr)
  cat("Row(s) with 'JERUSA' in the first column:\n")
  print(kable(filtered_data, format = "markdown"))
} else {
  cat("'JERUSA' not found in the first column.\n")
}