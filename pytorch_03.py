import numpy as np
import torch

array=np.arange(1.0,8.0)
tensor=torch.from_numpy(array)
array=array+1
print(array)
print(tensor)