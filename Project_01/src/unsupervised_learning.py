import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def load_data(file_path):
    """
    Load the dataset from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """
    Preprocess the data.
    """
    # Standardize the features
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    return data

def train_model(data, n_clusters):
    """
    Train the model.
    """
    # Initialize the model
    model = KMeans(n_clusters=n_clusters, random_state=42)

    # Train the model
    model.fit(data)

    return model

def evaluate_model(model, data):
    """
    Evaluate the model.
    """
    # Calculate the silhouette score
    score = silhouette_score(data, model.labels_)

    print(f'Silhouette score: {score}')

def main():
    data = load_data('datos_desercion.csv')
    data = preprocess_data(data)
    model = train_model(data, n_clusters=3)
    evaluate_model(model, data)

if __name__ == "__main__":
    main()

