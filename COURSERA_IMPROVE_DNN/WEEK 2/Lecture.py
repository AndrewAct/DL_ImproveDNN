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
 