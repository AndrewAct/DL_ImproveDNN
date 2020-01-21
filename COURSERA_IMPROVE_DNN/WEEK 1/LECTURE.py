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

## Understand Dropout ##
# Shrink weight 
# USually applied in CV 


## Other Regularization Method ##
# Data Augmentation 

# Early Stopping 
# Stop at a point where neural network doing the best iteration 
# Find the W and b to get the minimized J(W,b)
# Try not to overfitting

########## MODULE 3 ##########
## Normalizing Training Sets ##


## Why Normalize inputs? ##
# Make plot more symmetric 


# Vanishing/ Exploding Gradients #
# Linear Activation Function 

# If weight greater than 1: Increase exponentially 
# If weight smaller than 1: Decrease exponentially 


## Weight Initialization for Deep Networks ##
## Single neuron example
# W[l] = np.random.rand(shape) * np.sqrt(2/n[l-1])

# Xavier initialization  

## 1/20/20 ##
# Numerical Apporiximation of Gradients #
# The idea is nt so difficult 
# Just like derivatibve
# So omitted here

# Gradient Checking #
# Take dW[1], db[1]... and reshape into a big vector 

# Gradient Checking Implementation Notes #
# - Do not use in training - only to debug 
# - If algorithm fails grad check, look at components to try to identify bug
# - Remember regularization 
# - Does not work with drop out
# - Run at random initialization; perhaps again after some training 
