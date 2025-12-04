import numpy as np

data = [10,20,30,40,50,60,70,80,90,100]

q1 = np.quantile(data, 0.25)
q2 = np.quantile(data, 0.50)
q3 = np.quantile(data, 0.75)

print("Données :", data)
print("Q1 =", q1)
print("Q2 =", q2)
print("Q3 =", q3)
