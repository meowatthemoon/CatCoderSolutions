import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt



# Load data from a CSV file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

# Perform PCA to reduce the data to 2 dimensions
def perform_pca(data):
    # Drop non-numeric columns if any
    numeric_data = data.select_dtypes(include=[float, int])
    
    # Initialize PCA with 2 components
    pca = PCA(n_components=2)
    
    # Fit and transform the data
    pca_data = pca.fit_transform(numeric_data)
    
    # Return the transformed data as a DataFrame
    return pd.DataFrame(pca_data, columns = ['PC1', 'PC2'])

# Plot the 2D PCA results as a scatter plot
def plot_pca(pca_data):
    plt.figure(figsize=(10, 7))
    plt.scatter(pca_data['PC1'], pca_data['PC2'], c='blue', alpha=0.6, edgecolors='k', s=50)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('2D PCA Projection')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # read csv file
    file_path = "data.csv"
    data = load_data(file_path)
    
    if data is not None:
        # perform pca with 2 dimensions
        pca_data = perform_pca(data)

        # output is the std of the two dimensions rounded to two decimals
        stds = [round(np.std(pca_data[col]), 2) for col in ['PC1', 'PC2']]
        print(stds)

        # plot 
        plot_pca(pca_data)# metapoint
