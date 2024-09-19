# Load dplyr library
library(dplyr)

# Function to retain rows with a specific string in a specified column
retain_rows_with_string <- function(data, column_name, string_to_retain) {
  # Ensure the column name exists in the data
  if (!column_name %in% colnames(data)) {
    stop(paste("Column", column_name, "does not exist in the data frame."))
  }
  
  # Use filter to keep rows that contain the specific string
  filtered_data <- data %>%
    filter(grepl(string_to_retain, get(column_name), ignore.case = TRUE))
  
  return(filtered_data)
}
