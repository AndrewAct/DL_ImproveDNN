# Lectures in this course 
# I'm a lazy student, so a lot of contents might be omitted.
## This is the lecture contens of Week 1 ##


########## MODULE 1 ##########
## Setting up Your ML Application ##

## Applying ML is  interactive ##
## Layers ##
## Units ##
## Learning rate ##
## Activation  function ##

## Train/dev/test sets ##

## Mismatched train/test distribution ##
## Tips: make sure dev and test come from same distribution ##
# Bias Variance Trade-off #
# Underfitting and Overfitting #
# High bias: train error is large, result in underfitting
# High variance: train eror not close to dev error 


## Basic Recipe of ML ##
# If high bias: try bigger network & longer period 
# If hiigh variance: try more data and regularization 


########## MODULE 2 ##########
## Regularizing Your Neural Network ##

## 1/12/2020 ##

## Regularization ##
# Logistic regression #

# Frobenius norm
# AKA Euclidean Norm
# Square root  of sum of absolute square 

# Wikipedia: https://en.wikipedia.org/wiki/Logistic_regression
# Logistic Regression measures the relationship between categorical variable and one or more other independent variables 

# Why regularization reduces overfitting #

# Overfitting means the model works well on training set but bad on test set 
# SOurce: https://www.datacamp.com/community/tutorials/towards-preventing-overfitting-regularization

# This method penalize when weight is too large 
# If regularize become very large
# The parameter become very small 
# Z[l] = W[l]* a[l-1] + b[l] will be relatively small  

# Drop ouut Regularization #

# "A single model can be used to simulate having a large number of different network architectures by randomly dropping out nodes during training. "
# Source: https://machinelearningmastery.com/dropout-for-regularizing-deep-neural-networks/


