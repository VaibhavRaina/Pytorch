import torch
torch.manual_seed(0)
x=torch.rand(3,4)
print(x)
torch.manual_seed(0)
y=torch.rand(3,4)
print(y)
print(x==y)
