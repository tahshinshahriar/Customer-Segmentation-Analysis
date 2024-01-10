# Mall Customer Segmentation Analysis

This project performs customer segmentation analysis using the 'Mall Customer Segmentation Data' obtained from Kaggle. The dataset comprises features such as 'Customer ID,' 'Gender,' 'Age,' 'Annual Income,' and 'Spending Score (1-100).' The primary goal is to group similar customers based on features like age, annual income, spending score, and gender using clustering techniques.

## Getting Started

To replicate or explore the analysis, follow the steps below:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/mall-customer-segmentation.git
   cd mall-customer-segmentation
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook:**
   Open and run the `mall_customer_segmentation.ipynb` notebook using Jupyter or any compatible notebook environment.

4. **Explore the Results:**
   View the visualizations and insights generated from the clustering analysis.

## Project Structure

- `mall_customer_segmentation.ipynb`: Jupyter Notebook containing the analysis and code.
- `Data.csv`: Dataset used for customer segmentation.
- `requirements.txt`: List of Python dependencies.

## Methods

1. **Data Preprocessing:**
   - Initial exploratory data analysis includes printing the first 10 rows and summarizing the dataset.
   - One-hot encoding is applied to the 'Gender' column, creating binary columns 'Gender_Female' and 'Gender_Male.'
   - Missing values in columns 'Age,' 'Annual Income,' and 'Spending Score' are addressed, with outliers identified using boxplots.

2. **Feature Selection and Scaling:**
   - Selected columns with missing values are 'Age,' 'Annual Income,' and 'Spending Score.'
   - Missing values are filled with mean or median based on the presence of outliers.
   - Features for clustering include 'Age,' 'Annual Income,' 'Spending Score,' 'Gender_Female,' and 'Gender_Male.'
   - StandardScaler is used to scale the selected features.

3. **Clustering Analysis:**
   - The Elbow Method is employed to determine the optimal number of clusters for KMeans.
   - Within-Cluster-Sum-of-Squares (WCSS) is calculated for cluster numbers ranging from 1 to 10.
   - The 'elbow point' in the WCSS plot identifies the optimal number of clusters (4 clusters).

4. **Results:**
   - The optimal number of clusters (4) is printed, and cluster labels are assigned using the KMeans algorithm.
   - Visualizations provide insights into the characteristics of each cluster based on selected features.

## Conclusions

The clustering analysis successfully identifies distinct customer segments, offering valuable insights into customer behavior and preferences. This repository includes the code, dataset, and visualizations for comprehensive understanding and further exploration.

Feel free to fork, modify, and enhance the analysis based on your requirements!
