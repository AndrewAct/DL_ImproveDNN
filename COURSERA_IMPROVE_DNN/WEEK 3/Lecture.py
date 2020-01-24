#### 1/23/20 ####
## This is the lecture contens of Week 3 ##


########## MODULE 1 ##########
## Hyperparameter Tuning ##

# Hyperparameter Tuning #
# layers
# Hidden units 

## Coarse to fine 

# Use an Appropriate Scale to Pick #
# make sure (1-beta) is not zero


# Hyperparameters Tuning in Practice: Pandas Vs. Caviar #

########## MODULE 2 ##########
## Batch Normalization ##

# Given some intermediate value in NN 

# Fitting Batch Norm into a Neural Network #

# Implement Gradient Descent #
# for t = 1... (num of mini batches)
# Compute forward prop on X
# Use back prop to compute dW[i], db[i], dbeta[i], df[i]

# Why does Batch Norm Wok ? #

# Cavier shift 
# Why this is a problem with NN?

# Each mini-batch isw scaled by the mean/variance computed on just that mini-batch 
# This adds some noise to the valuesa z[l] within thay minibatch 
# So, similar to dropout, it adds some noise to each hidden layer's activations 
# This has a slight regularization effect 

# Batch Norm at Test Time  #
# µ = 1/m* ∑Z[i]
# sigma^2 = 1/m * ∑(z[i]-µ)^2
# Z[i]= (z[i]- µ)/(sigma^2+ ∂)^2

########## MODULE 3 ##########
# Softmax Regression #

# Softmax layer #

# Training a Softmax Classifier #

# Loss function #


########## MODULE 4 ##########
## ML Framework ##

# DL Frameworks #
# Criteria #
# Ease of programming 
# Running speed 
# Truly open 

# Tensorflow #
# Ex: cost function 
# J(w) = w^2 - 10*w + 25

import numpy as np 
import tensorflow as tf 

coefficient = np.array([[1.], [-10.], [25.]])
w = tf.Variable(0, dtype = tf.float32)
x = tf.placeholder(tf.float32, [3,1])
# cost = tf.add(tf.add(W**2, tf.multiply(-10., w)), 25)

cost = w^2 - 10*w + 25
cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]
train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

init = tf.global_variable_initializer()
session = tf.Session()
session.run(init)
print(session.run(w))

session>run(train)
print(session.run(w))

for i in range(1000):
