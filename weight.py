from collections import Counter
from statistics import median
import pandas as pd

f=pd.read_csv('D:\MRUDULA KORE\MRUDULA\Python\Classes\Data_CSV\SOCR-HeightWeight.csv')
weight=f['Weight(Pounds)'].tolist()

#MEAN

n=len(weight)
sum=0

for i in weight:
    sum=sum+i

mean=sum/n

print('Value of MEAN is :')
print(mean)

#MEDIAN

weight.sort()

if n % 2==0:
    median1=weight[n//2]
    median2=weight[(n//2)-1]
    median=(median1+median2)/2
else:
    median=weight[n//2]    

print('Value of MEDIAN is :')
print(median)    

#MODE

a=Counter(weight)
occurence=0
mode=0

for i in a.items():
    if i[1]>occurence:
        occurence=i[1]
        mode=i[0]

print('Value of MODE is :')
print(mode)
