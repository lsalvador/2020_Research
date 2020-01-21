#import the necessary libraries
library("ggplot2") #advanced plotting
library("BBmisc") #builtin normalization function
library("factoextra") # clustering algorithms & visualization
library("dbscan") #density based clustering

#read QUAST output
assemb_stat <- read.csv("transposed_report.tsv", sep = "\t")
numeric_stats <- assemb_stat[-1]
normalized_stats <- normalize(numeric_stats, method = "standardize",range = c(0,1), margin = 2)

#boxplot creation
boxplot(assemb_stat$L50)

#density based clustering
dbscan::kNNdistplot(normalized_stats, k =  100)
abline(h = 1, lty = 2)
db <- dbscan::dbscan(normalized_stats,eps = 5, minPts = 10)
fviz_cluster(db, normalized_stats, stand = FALSE, frame = FALSE)

