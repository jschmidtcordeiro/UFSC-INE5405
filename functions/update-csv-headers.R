update_csv_headers <- function(file_path, header_updates) {
  # Read the CSV file
  data <- read.csv(file_path, stringsAsFactors = FALSE, fileEncoding = "latin1")
  
  # Get the current column names
  current_headers <- colnames(data)
  
  # Replace current headers with new ones based on the header_updates list
  updated_headers <- sapply(current_headers, function(header) {
    if (header %in% names(header_updates)) {
      return(header_updates[[header]])
    } else {
      return(header)  # Keep the header if it's not in the update list
    }
  })
  
  # Apply the updated headers
  colnames(data) <- updated_headers
  
  # Write the updated CSV back to the file
  write.csv(data, file_path, row.names = FALSE, fileEncoding = "latin1")
  
  message("Headers updated successfully!")
}

# Example usage
# header_updates <- c("old_header1" = "new_header1", "old_header2" = "new_header2")
# update_csv_headers("path/to/file.csv", header_updates)
