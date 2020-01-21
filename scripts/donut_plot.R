##Donut Chart for M. bovis pangenome
library(ggplot2)

# Create data.
data <- data.frame(category=c("Core Genome", "Accessory Genome"), count=c(0.35, 0.65))

# Compute percentages
data$fraction <- data$count / sum(data$count)

# Compute the cumulative percentages (top of each rectangle)
data$ymax <- cumsum(data$fraction)

# Compute the bottom of each rectangle
data$ymin <- c(0, head(data$ymax, n=-1))

# Compute label position
data$labelPosition <- (data$ymax + data$ymin) / 2

# Compute a good label
data$label <- paste0(data$category, "\n", data$count,"%")

ggplot(data, aes(ymax=ymax, ymin=ymin, xmax=4, xmin=3, fill=category)) +
  geom_rect() +
  geom_text( x=1, aes(y=labelPosition, label=label, color=category), size=5) + # x here controls label position (inner / outer)
  scale_fill_brewer(palette=c("Accent")) +
  scale_color_brewer(palette="Accent") +
  coord_polar(theta="y") +
  xlim(c(-3, 4)) +
  theme_void() +
  theme(legend.position = "none")