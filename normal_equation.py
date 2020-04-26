import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#using normal equation

def linear_regression(x,y):
    x=np.c_[np.ones(n),x]
    theta=np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(x),x)),np.transpose(x)),y)
    print(theta)

rng=np.random.default_rng()
training_input=rng.integers(-5,5,size=(500,2))
training_output=training_input[:,0]+training[:,1]+2*rng.standard_normal(500)
#linear_regression(training_input,training_output)
