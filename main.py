import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('./data/Mall_Customers.csv')
df = data.drop(['CustomerID', 'Gender', 'Age'], axis=1)

X = df.values.astype(float)

scaler = StandardScaler()
X = scaler.fit_transform(X)

pca = PCA(n_components=2)
X = pca.fit_transform(X)

# elbow method
# wcss = []
# for k in range(1, 11):
#     kmeans_model = KMeans(n_clusters=k, init='k-means++', random_state=0)
#     kmeans_model.fit(X)
#     wcss.append(kmeans_model.inertia_)
#
#
# plt.plot(range(1, 11), wcss)
# plt.title('K-Means Elbow Method')
# plt.xlabel('Number of clusters')
# plt.xticks([i for i in range(11)])
# plt.ylabel('WCSS')
# plt.show()

kmeans_model = KMeans(n_clusters=5, init='k-means++', random_state=0)
kmeans_model.fit(X)
df['cluster'] = kmeans_model.labels_
pd.set_option('display.max_columns', None)
print(df.groupby('cluster').mean())

clusters = (0, 1, 2, 3, 4)
colors = ('r', 'y', 'g', 'b', 'c')
# кластеры
for cl, color in zip(clusters, colors):
    plt.scatter(X[df['cluster'] == cl, 0], X[df['cluster'] == cl, 1],
                s=50, c=color, label='Cluster ' + str(cl))
# центроиды
plt.scatter(kmeans_model.cluster_centers_[:, 0],
            kmeans_model.cluster_centers_[:, 1],
            s=100, c='black', marker='x', label='Centroid')
plt.title('Clusters')
plt.xlabel('Principal component 1')
plt.ylabel('Principal component 2')
plt.legend()
plt.show()