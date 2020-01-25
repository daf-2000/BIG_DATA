
# coding: utf-8

# In[32]:

#EX_1
import numpy as np
a = np.array([[1,6], [2,8], [3,11], [3,10], [1,7]])
mean_a = np.mean(a, axis=0)
print(mean_a)
#EX_2
print("###")
a_centered = a - mean_a
print(a_centered)
#EX_3
print("###")
print(a_centered[0:,0] @ a_centered[0:,1] / 4)
#EX_4
print("###")
print(np.cov(a.T))


# In[ ]:



