import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Data prepration

dataset=pd.read_csv('drug200.csv')
#A
dataset_1st_10_roes=dataset.head(10)
print(dataset_1st_10_roes)
#B
dataset_last_10_roes=dataset.tail(10)
print(dataset_last_10_roes)
#c
rows,col=dataset.shape
print(rows)
print(col)
#D
columns=dataset.columns
print(columns)

#E
last_col=dataset.columns[-1]
print(last_col)
#F
col_4th=dataset.columns[4]
print(col_4th)
#G
Gf= dataset['Sex'].unique()
print(len(Gf))
#H
#idxmax() return name of column with max frequency 
xa=dataset['Sex'].value_counts().idxmax()
print(xa)

#i

numerical_values=dataset.select_dtypes(include=['int','float']).columns
for i in numerical_values:
    #.mean() returns the mean
     print('column' ,i )
     print('Mean',dataset[i].mean())  
     #.std returns standard deviation
     
     print('standard deviation' , dataset[i].std())  
     #.quantile() returns percentile   
     print('q0' , dataset[i].quantile(0.25))  
     print('q1' , dataset[i].quantile(0.5))  
     print('q2' , dataset[i].quantile(0.65)) 
     print('-------------------------------------') 
     
   
#2 a)
var1=dataset[dataset['Age']>60]
print(var1)
#2 b)
var2=dataset[dataset['Drug'].str.startswith('y')]
print(var2 , var2.count() )

#2 c)
dataset.describe()

#2 D)
dataset['Age'] = dataset['Age'].astype('object')
dataset['Na_to_K'] = dataset['Na_to_K'].astype('object')
dataset.dtypes


#2 E) 
db_ordered_by_age=dataset.groupby(['Age','Na_to_K'])
print(db_ordered_by_age.first())


#2 F)
print(dataset.isnull().any())

#2 G)
dataset.fillna(dataset.mean(),inplace=True)

#2 H)
duplicate = dataset.duplicated(keep=False).sum()
print(duplicate)

#2 i) 

bins = pd.cut(dataset['Age'], 6)
bin_counts = bins.value_counts()
print("bin counts", bin_counts)

#2 j)
temp = dataset.isna().sum(axis=1)==2
print(temp[temp].index)

#2 K)
                
max_age_index=dataset['Age'].max()
print(dataset[dataset.Age == dataset.Age.max()]  )        

#2 L)
plt.boxplot(dataset['Age'])
plt.title('Boxplot of Age')
plt.show()

#2 M)

plt.hist(dataset['Age'])
plt.title('Histogram of Age')
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#2 n)
plt.scatter(dataset['Age'], dataset['Drug'])
plt.title('Scatterplot of Age vs Drug')
plt.xlabel("Age")
plt.ylabel("Drug")
plt.show()

