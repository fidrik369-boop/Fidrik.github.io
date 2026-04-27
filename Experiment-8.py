Program:

Python

import pandas as på import numpy as np from sklearn.impute import SimpleImputer from scipy import stats Create dummy dataset

data(

Name': ['A', 'B', 'C', 'D', 'E'].

Age': 125, np.nan, 30, 22, 100], # 100 is outlier

Salary: 150000, 54000, np.nan, 50000, 1000000], # 1M is outlier ID': [1, 2, 3, 4, 5]

df = pd.DataFrame (data)

print("Original Data:\n", df) a. Attribute Selection (Dropping ID)

dfdf.drop(['ID'], axis=1)

#b. Handling Missing Values

imputer Simple Imputer (strategy='mean')

df [['Age', 'Salary']] imputer.fit_transform (df [['Age', 'Salary']])

c. Discretization (Binning Age)

df ['Age Bin'] = pd.cut (df ['Age'], bins 3, labels ["Young", "Mid".

d. Elimination of Outliers (Z-score)

z_scores np.abs(stats.zscore (df [['Age', 'Salary']]))

df clean df [(z_scores < 1.5).all (axis-1)) # Threshold 1.5 for this

small data

print("\nProcessed Data (No Outliers);Xn", df_clean)

Output:

Plaintext

Processed Data (No Outliers):

Name

Age Salary

Age Bin

0

A 25.0

50000.0

Young

2

C 30.0

276000.0

Young

3 D 22.0 50000.0

Young

xvil
