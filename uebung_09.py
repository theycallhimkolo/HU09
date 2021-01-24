import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

data = pd.read_csv("IVVA2021_H09_Daten.csv", sep=";")
data_np = data.to_numpy()


data_only_numbers = data_np[:, 1:]


means3 = KMeans(n_clusters=3, n_init=10, max_iter=100, random_state=20210120).fit(data_only_numbers)
means4 = KMeans(n_clusters=4, n_init=10, max_iter=100, random_state=20210120).fit(data_only_numbers)
means5 = KMeans(n_clusters=5, n_init=10, max_iter=100, random_state=20210120).fit(data_only_numbers)

clustersk3 = [[], [], []]
clustersk4 = [[], [], [], []]
clustersk5 = [[], [], [], [], []]
for idx in range(len(data)):
    print(idx)
    print(len(means3.labels_))
    clustersk3[means3.labels_[idx]].append(data_only_numbers[idx])
    clustersk4[means4.labels_[idx]].append(data_only_numbers[idx])
    clustersk5[means5.labels_[idx]].append(data_only_numbers[idx])


def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return float(len(s1.intersection(s2)) / len(s1.union(s2)))

print(clustersk3)
cluster_arr = list(clustersk3)+list(clustersk4)+list(clustersk5)
cluster_arr = [[str(list(x)) for x in arr] for arr in cluster_arr]
dmatrix = []

for i in range(len(cluster_arr)):
    distances = []
    for j in range(len(cluster_arr)):
        dist = 1-jaccard_similarity(cluster_arr[i], cluster_arr[j])
        distances.append(dist)
    dmatrix.append(distances)


out = pd.DataFrame(dmatrix).to_excel("out.xlsx")

for row in dmatrix:
    print(row)






