import pandas as pd
import numpy as np
from scipy.stats import spearmanr

dc = pd.read_csv('dc.csv')['dc'].tolist()
pc = pd.read_csv('pr.csv')['pr'].tolist()
ec = pd.read_csv('eig.csv')['eig'].tolist()

c = [dc,pc,ec]
m = np.zeros((3,3),dtype=float)

for i in range(0,3):
	for j in range(0,3):
		m[i][j] = spearmanr(c[i],c[j])[0]

print m