from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
#X = [[3,5],[1,4],[1,6],[2,6],[1,5],[6,8],[6,6],[6,7],[5,6],[6,7],[7,1],[8,2],[9,1],[8,2],[9,3],[9,2],[8,3]]

v1=[3, 1, 1, 2, 1, 6, 6, 6, 5, 6, 7, 8, 9, 8, 9, 9, 8]
v2=[5, 4, 6, 6, 5, 8, 6, 7, 6, 7, 1, 2, 1, 2, 3, 2, 3]

x1 = np.array(v1)
x2 = np.array(v2)

X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
print(X)

import matplotlib.pyplot as plt
plt.plot(v1, v2, 'ro')
plt.axis([1, 9, 1, 8]) #Eje x: de 1 a 9; Eje Y: de 1 a 8
plt.show()
#Algoritmo K-Means 
K = 3 
kmeans_model = KMeans(n_clusters=K).fit(X)
for i, l in enumerate(kmeans_model.labels_):
    print("(x1,x2) -> Clase")
    print("({0},{1}) ->:{2}".format(x1[i], x2[i], l))
predicciones = kmeans_model.predict(X)
print(predicciones)
test=[[3,5]]
prediccion = kmeans_model.predict(test)
print("Prediccion {0}->{1}".format(test,prediccion))
x1 = np.array([2, 5, 8])
x2 = np.array([5, 5, 4])

X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
prediccion = kmeans_model.fit_predict(X)
print(prediccion)
print(kmeans_model.cluster_centers_)