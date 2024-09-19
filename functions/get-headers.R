# Function to get headers and display them
get_headers <- function(file_path) {
  # Load the CSV file (use appropriate encoding if necessary)
  data <- read.csv(file_path, header = TRUE, sep = ",", fileEncoding = "latin1")
  
  # Get the column names (headers)
  headers <- colnames(data)
  
  # Format the headers in the requested style
  formatted_headers <- paste0('"', headers, '",')
  
  # Print each header on a new line
  cat(formatted_headers, sep = "\n")
}