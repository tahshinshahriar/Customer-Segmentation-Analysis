import pandas as pd
from sklearn.cluster import KMeans 
from sklearn.preprocessing import StandardScaler                           
import matplotlib.pyplot as plt
from kneed import KneeLocator
import seaborn as sns

#Load the dataset
data = pd.read_csv('Data.csv')

print(f"The first 10 rows of the dataset is \n {data.head(10)}\n")
print(f"The summary of the dataset is \n {data.describe()}\n")

#Perform one hot encoding for categorical variable Gender 
data = pd.get_dummies(data, columns=['Gender'], prefix='Gender')
#Convert the values into numericals (True, False -> 0,1)
data['Gender_Female'] = data['Gender_Female'].astype(int)
data['Gender_Male'] = data['Gender_Male'].astype(int)

print(f"The first 10 rows of the dataset is \n {data.head(10)}")
#Identify the columns with missing values
print(f"Missing Values \n {data.isnull().sum()}")

#Detect outliers in the columns with missing values
selected_columns = data.columns[1:4]
for column in selected_columns:
    sns.boxplot(x=data[column])

#Result shows that there are not outliers in any of the columns except in Annual Income
#Fill out te missing values with mean or median of the respective columns
data[selected_columns[0]].fillna(data[selected_columns[0]].mean(), inplace=True)
data[selected_columns[2]].fillna(data[selected_columns[2]].mean(), inplace=True)
data[selected_columns[1]].fillna(data[selected_columns[1]].median(), inplace=True)

print(f"Missing Values \n {data.isnull().sum()}")

#Select columns to perform clustering analysis
features = data[['Age','Annual Income (k$)', 'Spending Score (1-100)','Gender_Female', 'Gender_Male']]

#Standardize the columns so that no column dominates the other column
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

print(f"The first 10 rows of the dataset with selected features is \n {features.head(10)}\n")

#Find the WCSS value for every number of clusters ranging from 1 to 10
WCSS = []
for cluster in range(1,11):
    kmeans = KMeans(n_clusters=cluster,init='k-means++',n_init=10)
    kmeans.fit_predict(scaled_features)
    WCSS.append(kmeans.inertia_)

#Plot the values of WCSS for finding the optimal value of k
plt.plot(range(1, 11), WCSS)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.xticks(range(1, 11)) 
plt.show()
oc = KneeLocator(range(1,11), WCSS, curve="convex", direction="decreasing")
optimal_k = oc.elbow
print(f"The optimal value of K is {optimal_k}")

# Apply KMeans clustering
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', n_init=10)
cluster_labels = kmeans.fit_predict(scaled_features)









