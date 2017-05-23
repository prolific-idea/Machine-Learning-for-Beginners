rm(list=ls(all=TRUE))
#Install the caret package if not installed
#install.packages("caret", dependencies = c("Depends", "Suggests"))
#install.packages("Boruta")
#install.packages("DMwR")
#getwd()

#Loading relevant packages
library(caret)
library(dplyr)
library(Boruta)
library(DMwR)
library(corrplot)

#Loading the dataset
dataset <- read.csv("Fraud.csv")
dataset$X <-NULL
#explore the data
str(dataset) 

#convert categorical variables to factors
dataset$gender <- as.factor(dataset$gender)
dataset$state <-as.factor(dataset$state)
dataset$fraudRisk <-as.factor(dataset$fraudRisk)

###use a binary classifier for the categorical variables but first convert the dependant variable to a numerical variable 
dataset$fraudRisk <- as.numeric(as.character(dataset$fraudRisk))
dmy <- dummyVars(" ~ .", data = dataset,fullRank = F)
transformed_dataset <- data.frame(predict(dmy, newdata = dataset))
transformed_dataset$fraudRisk <-as.factor(transformed_dataset$fraudRisk)
names(transformed_dataset)[2]<-paste("Female")
names(transformed_dataset)[3]<-paste("Male")
names(transformed_dataset)[4]<-paste("NY")
names(transformed_dataset)[5]<-paste("DC")
names(transformed_dataset)[6]<-paste("AR")

#examine the data
str(transformed_dataset)

#Spliting data into two parts based : 75% and 25% you can vary this to what you want
index <- createDataPartition(transformed_dataset$fraudRisk, p=0.75, list=FALSE)
trainSet <- transformed_dataset[ index,]
testSet <- transformed_dataset[-index,]
trainSet$custID <- NULL

###correlation between the variables to checj for multicollinearity
corrdataset <- trainSet
# # # calculate correlation matrix
correlationMatrix <- cor(corrdataset[,1:10])
# # # summarize the correlation matrix
print(correlationMatrix)
##no massive correlation between the predictor variables no multicollinearity


#use wrapper methods to assist in selecting features
#Feature selection using rfe in caret
control <- rfeControl(functions = rfFuncs,
                      method = "repeatedcv",
                      repeats = 3,
                      verbose = FALSE)
outcomeName<-'fraudRisk'
predictors<-names(trainSet)[!names(trainSet) %in% outcomeName]
Fraud_Risk_Profile <- rfe(trainSet[,predictors], trainSet[,outcomeName],
                         rfeControl = control)
print(Fraud_Risk_Profile)
# plot the results
#plot(Fraud_Risk_Profile, type=c("g", "o"))

### use Boruta package to further assist feature selection 

set.seed(13)
bor.model <- Boruta(fraudRisk~ ., data = trainSet, maxRuns=101, doTrace=0)
summary(bor.model)
boruta.cor.matrix <- attStats(bor.model)
important.features <- names(trainSet)[bor.model$finalDecision!="Rejected"]
important.features
boruta.cor.matrix

## so both methods confirm that numTrans,balance,creditline,numinttrans are varibles that we should use so we use them as predictors

predictors <- c("balance", "numTrans", "creditLine", "cardholder")

#get models in Caret you can use
names(getModelInfo())

#Build your model
##Training with nnet
##fit tune for crossvalidation
##for performing cross validation and avoid overfitting of the model
fitControl <- trainControl(
  method = "repeatedcv",
  number = 10,
  repeats = 5)

model_nnet<-train(trainSet[,predictors],trainSet[,outcomeName],method='nnet',trControl=fitControl)


print(model_nnet)
plot(model_nnet)

#check for the variable importance of the nnet model 
#Checking variable importance for nnet

#Variable Importance
varImp(object=model_nnet)
plot(varImp(object= model_nnet),main="NNET - Variable Importance")
#shows numIntTrnas is very important (strongly relevant) the balance is important but only with other variables(weakly relevant)


# then predict the outcome 
#Predictions
predictions_prob <-predict(object=model_nnet,testSet[,predictors],type="prob")
predictions_raw <-predict(object=model_nnet,testSet[,predictors],type="raw")
predictions_prob <- as.data.frame(predictions_prob)
predictions_prob <- cbind(testSet$custID,predictions_prob)
names(predictions_prob)[1]<-paste("CustomerID")
names(predictions_prob)[2]<-paste("Low_Risk")
names(predictions_prob)[3]<-paste("High_Risk")
predictions_prob$Low_Risk <- (predictions_prob$Low_Risk*100)
predictions_prob$High_Risk<- (predictions_prob$High_Risk*100)
predictions_prob$Low_Risk<- round(predictions_prob$Low_Risk, digits=2)
predictions_prob$High_Risk<-round(predictions_prob$High_Risk, digits=2)
predictions_prob


#get the confusion matrix to see how well our classifier did

confusionMatrix(predictions_raw,testSet[,outcomeName])


