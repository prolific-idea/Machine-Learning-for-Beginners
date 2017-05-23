# Machine Learning - Feature Selection for Classification and Forecasting

If you're completely new to ML (machine learning), try the simplified Python hackathon: [Introduction to ML](https://github.com/prolific-idea/Machine-Learning-for-Beginners/tree/master/0-Intro)

## Setup R
* R - [https://cran.r-project.org/bin/windows/base/R-3.4.0-win.exe](https://cran.r-project.org/bin/windows/base/R-3.4.0-win.exe)
* R Tools - [https://cran.r-project.org/bin/windows/Rtools/Rtools34.exe](https://cran.r-project.org/bin/windows/Rtools/Rtools34.exe)
* R Studio - [https://download1.rstudio.org/RStudio-1.0.143.exe](https://download1.rstudio.org/RStudio-1.0.143.exe)

## Hackathon
Given the below dataset, use any algorithm of your choice to:  
* Determine the relevant features 
* Determine the accuracy of your prediction

### Data Dictionary
* custID: A unique identifier for each customer  
* gender: Gender of the customer 
* state: State in the United States where the customer lives
* cardholder: Number of credit cards the customer holds  
* balance: Balance on the credit card 
* numTrans: Number of transactions to date 
* numIntlTrans: Number of international transactions to date
* creditLine: The financial services corporation, such as Visa, MasterCard, or American Express
* fraudRisk: Binary variable, 1 means customer being frauded, 0 means otherwise these are the columns

### You will require the ffg packages in your code:

* install.packages("caret", dependencies = c("Depends","Suggests"))
* install.packages("Boruta")
* install.packages("DMwR")i
* install.packages("corrplot")

### Tips
Load the ffg libraries:
* library(caret)
* library(Boruta)
* library(corrplot)

Load dataset using read.csv()

Convert categorical variables to factors.

Use binary classifier for categorical variables.

Split data into training and test sets.

Correlation analysis on training set:
```
corrdataset <- trainSet
correlationMatrix <- cor(corrdataset[,1:10])
```

Remove independent variables that are correlated.

Use Recursive Feature Eliminator from Caret Package:
```
control <- rfeControl(functions = rfFuncs,
                      method = "repeatedcv",
                      repeats = 3,
                      verbose = FALSE)
outcomeName<-'fraudRisk'
predictors<-names(trainSet)[!names(trainSet) %in% outcomeName]
Fraud_Risk_Profile <- rfe(trainSet[,predictors], trainSet[,outcomeName],
                         rfeControl = control)
```

Use Boruta Package to further assist in selection:
```
set.seed(13)
bor.model <- Boruta(fraudRisk~ ., data = trainSet, maxRuns=101, doTrace=0)
summary(bor.model)
boruta.cor.matrix <- attStats(bor.model)
important.features <- names(trainSet)[bor.model$finalDecision!="Rejected"]
important.features
boruta.cor.matrix
```

Eliminate features that algorithm has not chosen.

Specify the machine learning algorithm and run feature set through this to output accuracy.
