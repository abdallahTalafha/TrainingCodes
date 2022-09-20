from difflib import ndiff
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random


#x = random.normal(loc=50, scale=5, size=1000)
y = random.binomial(n=100,p=0.5,size =1000)
#w = random.poisson(lam=2, size=10)
#q = random.uniform(low=2.0,high=4.0,size=(20,50))
#r = random.logistic(loc=50, scale=5, size=1000)
print(y)
#sns.distplot(x,hist=False,label='normal')
#sns.distplot(y,hist=False,label='binomial')
#sns.distplot(r,hist=False,label='logistic')
#sns.distplot(q,hist=False,label='logistic')
plt.show()
