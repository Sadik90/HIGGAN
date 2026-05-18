#coding 
#autograd for calculating the gradient of the loss function
#optim for optimization algorithms

import torch
x = torch.randn(3, requires_grad=True)
print(x)