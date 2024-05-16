import random
from math import e

def online_hiring_problem(n):
    a=random.sample(range(1,n+1),n)#making random list of 1 to n numbers
    b=int(n/e)
    c=max(a[:b])#max valoe upto 1/e
    for i in  a[b:]:
        if i>c:#calculate greater value than c
            return i
    return a[-1]  
n=100  
#print(online_hiring_problem(n))
trails=10000
z=0
for i in range(trails):#for loop to calculate the average quality of the selected candidate
    z=z+online_hiring_problem(n)
result=z/10000
print("The average quality of the selected candidate is:",result)    
