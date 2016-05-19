data(iris)
names(iris)

table(iris$Species)

require(ggplot2) #install.packages("ggplot2")
qplot(Petal.Width, Sepal.Width, data=iris, colour=Species, size=I(4))

#install.packages("tree")
library(tree)

# Decision tree, two variables

tree1 <- tree(Species ~ Sepal.Width + Petal.Width, data = iris)
summary(tree1)


plot(tree1)
text(tree1)

plot(iris$Petal.Width,iris$Sepal.Width,pch=19,col=as.numeric(iris$Species))
partition.tree(tree1,label="Species",add=TRUE)
legend(1.75,4.5,legend=unique(iris$Species),col=unique(as.numeric(iris$Species)),pch=19)

#decision tree, three variables

tree1 <- tree(Species ~ Sepal.Width + Petal.Length + Petal.Width, data = iris)

#but the tree implies that only petal length and width affect the classification, so

tree1 <- tree(Species ~ Petal.Length + Petal.Width, data = iris)

plot(iris$Petal.Length, iris$Petal.Width,pch=19 ,col=as.numeric(iris$Species))
partition.tree(tree1,label="Species",add=TRUE)
legend(0.25,6,legend=unique(iris$Species),col=unique(as.numeric(iris$Species)),pch=19)

# other packages: http://www.r-bloggers.com/a-brief-tour-of-the-trees-and-forests/
# Learning R: http://www.r-bloggers.com/how-to-learn-r-2/
