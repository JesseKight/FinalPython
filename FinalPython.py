import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

mnist = fetch_openml('mnist_784')
print(mnist)


temp = pd.read_csv('C:/Users/jesse/Documents/GitHub/FinalPython/data/phone.csv')


training =  temp.iloc[-205:]
print("training:")
print(training)

testing = temp.iloc[:-200]
print("testing:")
print(testing)