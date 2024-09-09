import torch

x=torch.rand(224,224,3)
x[0,0,0]=0.089 
x_permute=x.permute(2,0,1)
print(x.size())
print(x_permute.size())
print(x_permute[0,0,0])
z=torch.arange(1.,10.)
z=z.reshape(1,3,3)
print(z)
print(z[0,2,2])
print(z[0,:,2])
