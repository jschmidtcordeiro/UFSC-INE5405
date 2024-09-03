# Install ggplot2 (if not already installed)
install.packages("ggplot2")

# Load the ggplot2 package
library(ggplot2)

# Create a sample plot
data <- data.frame(x = c(1, 2, 3, 4, 5), y = c(2, 4, 6, 8, 10))

ggplot(data, aes(x = x, y = y)) +
  geom_point(color = "blue") +
  ggtitle("Scatter Plot with ggplot2") +
  xlab("X-axis") +
  ylab("Y-axis")