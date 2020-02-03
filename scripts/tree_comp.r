library(ape)
tree1 <-read.nexus(file="accesory_genome.nexus")
tree2 <-read.nexus(file="core_genome.nexus")

association <- cbind(tree1$tip.label, tree1$tip.label)
#tree1 and tree2 should have exact same tips/taxa

tre1 <- ladderize(tree1,FALSE)
tre2 <- ladderize(tree2,FALSE)

cophyloplot(tre1, tre2, assoc = association, length.line = 4, space = 400, gap = 1, show.tip.label = FALSE)
