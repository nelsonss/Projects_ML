import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

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
    # Split the data into features and target
    X = data.drop('desertion', axis=1)
    y = data['desertion']

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train the model.
    """
    # Initialize the model
    model = LogisticRegression()

    # Train the model
    model.fit(X_train, y_train)

    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model.
    """
    # Make predictions
    y_pred = model.predict(X_test)

    # Print the classification report
    print(classification_report(y_test, y_pred))

    # Print the confusion matrix
    print(confusion_matrix(y_test, y_pred))

def main():
    data = load_data('datos_desercion.csv')
    X_train, X_test, y_train, y_test = preprocess_data(data)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()

