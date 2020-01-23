#### 1/20/20 ####
## This is the lecture contens of Week 2 ##


########## MODULE 1 ##########
### Optimization Algorithms ###

## Mini Batch Gradient Descent ##
# Batch Vs Mini-Batch Gradienct Descent #
# Vectorization allows you to efficiently compute on m examples

## Mini-Batch (AKA baby-batching?)

# Steps: #
# 1. Gradient descent use X{t}, Y{t}
# 2. Forward propagation on X{t}
# 3. Compute cost 
# 4. Backpropagation to compute gradients 

#### Epoch: pass through traning set ####


### Understanding Mini-batch Gradient Descent ###
# In graph, mini-batch gradient descent is noisier than batch gradient descent 

# Choose the size of mini-batch ##
# - If mini-batch size = m: Batch gradient descent 
# - If mini-batch size = 1:: stochastic gradient descent 
# - In practice: something in between 

# Batch gradient descent: too long per iteration 
# Stochastic gradient descent: lose speed-up from vectorization 
# In between: Fastest learning & vectoization & make prediction without processing so long 

## Strategy:
 # - If small traning set: batch 
 # - Typical mini-batch size: 
 # Make sure batch size matches CPU/GPU memory
 
 #### 1/21/20 ####

# Exponentially Weighted Averages #
# Example: Weather in London #
# Vt = 0.9* V(t-1) + 0.1*theta(t)

#  Or expressed in thsi form: V(t) = beta*V(t-1) + (1-beta)*theta(t)
# Vt as approximately average over 1/(1-beta)* temperature

# Understand Exponential Wighted Averages #
# V(t) = beta*V(t-1) + (1-beta)*theta(t)
# (1 - epsilon)^(1/epsilon) = 1/e

# Bias Correction #
# V(t)/(1- beta^t)

# Gradient Descent with Momentum #
# On iteration t
# Compute dW, db on mini batch 

# v[dW] = beta*v[dW] + (1-beta)*dW
# v[db] = beta*v[db] + (1-beta)*db 
# W = W - av[dW], b = b - alpha*v[db]

# Note: alpha is the learning rate 

# RMSprop #
# Slow down or speed up leanring 
# S[dW] = beta* S[dW]+ (1- beta)* dW^2
# S[db] = beta*S[db] + (1-beta)* db^2
 # Ensure the algorithm is not dividing zero! 

# Adam Optimization #
   # Adaptivie Moment Estimation
 # Initizlize V[dW] = 0, S[dW] = 0, V[ab] = 0
 # On iteration t:
 # COmpute dW, db
 # V[dW] = beta*V[dW] + (1-beta) *dW
 # S[dW] = beta* S[dW]+ (1- beta)* dW^2
 # S[db] = beta*S[db] + (1-beta)* db^2
  # Correct Bias
# V[dW]= V[dW]/(1-beta)

# Learning rate Decay #

# The Problem of Local Optima #
# Saddle point and local optimum 
# Plateu 
