##Analysis of Assembly Statistics
##Noah A. Legall

## 1. read in the data.
MI_assemb_stats <- read.csv("transposed_report.csv",header = TRUE)

# Let's summarize all the data we got first:
summary(MI_assemb_stats)

# There seems to be a clear outlier, 09_4305_S4_L001.contigs. let's drop this row
MI_assemb_stats <- MI_assemb_stats[MI_assemb_stats$Assembly != "09_4305_S4_L001.contigs",]
summary(MI_assemb_stats)

# I feel more confident because now all the genome lengths vary between 4.2 - 4.4 million bp
# This value is about the size of the M. bovis genome.

## 2. verify, what is the distribution of the statistics QUAST outputs? Do they make sense

# Visualize how the histograms compare to released numbers of M. bovis genome assembly statisitics.
# these are the comparable thiings from (Branger et al., 2017)

# Values from genome announcement paper
total_length <- 4296059 
total_contigs <- 146
largest_contigs <- 237066
gc_content <- 65.54
n50 <- 98742

hist(MI_assemb_stats$Total.length, main = "", xlab = "Total Length (bp)",breaks = 50)
abline(v=total_length,col="red")
hist(MI_assemb_stats$N50, main = "", xlab = "N50", breaks = 50)
abline(v=n50,col="red")
hist(MI_assemb_stats$X..contigs, main = "", xlab = "No. of contigs",breaks = 50) 
abline(v=total_contigs,col="red")
hist(MI_assemb_stats$Largest.contig, main = "", xlab = "Largest contig",breaks = 50)
abline(v=largest_contigs,col="red")
hist(MI_assemb_stats$GC...., main = "", xlab = "GC content (%)",breaks = 25)
abline(v=gc_content,col="red")


