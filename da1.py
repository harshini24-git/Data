import numpy as np
import pandas as pd
import os
import seaborn as sns
from matplotlib import pyplot as plt
import math
data = pd.read_csv(r'C:\Users\18574\Desktop\data\DataAnalyst.csv')
data.head()
data.info()
data.drop(columns=['Unnamed: 0'])
data. isnull().sum()
data['Job Title'].value_counts()

