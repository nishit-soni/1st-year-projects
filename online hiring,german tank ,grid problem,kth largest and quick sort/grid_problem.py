#3. Consider a 101x101 grid, if you were to throw 20 darts at this grid, on an average, how close are you to the Diagonal (assume repetitions are allowed)? Write a python code with 101 x 101 generalized to nxn (where n is odd) and 20 generalized to k darts. Once you write a python script and observe the answer, write a detailed mathematical reasoning explaining your answer. Upload the python file, the latex file and the pdf file. 
import random
from math import sqrt

def average_distance_to_diagonal(n, k):#function to calculate the average distance to the diagonal
    total_distance = 0

    for i in range(k):#for loop to calculate the distance
        x = random.randint(0, n)
        y = random.randint(0, n)
        d1= abs(x - y) / sqrt(2)#distance formula
        total_distance += d1#taking minimum distance
    average_distance = total_distance / k#average distance
    return average_distance

n = int(input("Enter the value of n")) # Grid size
k = int(input("Enter the value of darts"))# Number of darts
p= int(input("Enter the value you want to repeat"))#number of times you want to repeat
average_distance = average_distance_to_diagonal(n, k)
z=0
for i in range(p):#for loop to calculate the average quality of the selected candidate
    z=z+average_distance_to_diagonal(n, k)#calculate the average distance to the diagonal
result=z/p
print("The average quality of the selected candidate is:",result)    