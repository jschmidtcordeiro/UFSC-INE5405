# Function to create a new file with only the selected headers
select_headers <- function(file_path, headers_to_select, output_file_path) {
  data <- read.csv(file_path, header = TRUE, sep = ",", fileEncoding = "latin1")
  headers <- colnames(data)
  
  # Check if selected headers exist in the original headers
  valid_headers <- headers_to_select[headers_to_select %in% headers]
  
  # Create a new data frame with only the selected headers
  if (length(valid_headers) > 0) {
    new_data <- data[, valid_headers, drop = FALSE]
    write.csv(new_data, output_file_path, row.names = FALSE, fileEncoding = "latin1")
    cat("Filtered CSV created:", output_file_path, "\n")
  } else {
    cat("None of the selected headers were found in the original file.\n")
  }
}