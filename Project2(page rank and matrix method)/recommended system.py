import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = pd.read_csv('project_data.csv', header=None, skiprows=1)
G = nx.DiGraph()

for i, r in x.iterrows():
    source = str(r[0])  
    for target in r[1:]:  
        b = str(target)
        if b != 'nan' and b != source:  
            G.add_edge(source, b)

nodes = list(G.nodes())            

X=nx.to_numpy_array(G,dtype=int)#converts the graph to an adjacency matrix

for i in range(len(X)):
    for j in range(len(nodes)):
        if X[i][j]==1 and X[j][i]==0:
            X[j][i]=-1


L=[]
threshold=0.9
nodes = list(G.nodes())
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if X[i][j] == 0 and i != j:
            X1=np.delete(X, i, axis=0)
            X2=np.delete(X1, j, axis=1)
            A=np.delete(X[i,:], j)
            B=X1[:,j]
            C=np.linalg.lstsq(X2,A,rcond=None)[0]
            score=np.dot(C,B)
            X[i][j]=score
            L.append(score)
            if score>threshold:
                X[i][j]=1 
                G.add_edge(nodes[i], nodes[j])
            else:
                X[i][j]=0  

X[X == -1] = 0

#Printing the final updated matrix
print("Final Updated Matrix:")
print(X)
print("Number of edges added:")
print(len(L))
# Visualize the graph
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 12))
nx.draw(G, pos, with_labels=True, node_size=400, font_size=8, node_color='skyblue')
plt.title('Collaboration Network with Added Edges')
plt.show()

