import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Load the dataset from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def numerical_analysis(data):
    """
    Perform descriptive analysis on numerical features.
    """
    print("Descriptive analysis of numerical features:")
    print(data.describe())

    for column in data.select_dtypes(include=['int64', 'float64']).columns:
        plt.figure(figsize=(9, 8))
        sns.distplot(data[column], color='g', bins=100, hist_kws={'alpha': 0.4})
        plt.title('Distribution of ' + column)
        plt.show()

def categorical_analysis(data):
    """
    Perform descriptive analysis on categorical features.
    """
    print("Descriptive analysis of categorical features:")
    for column in data.select_dtypes(include=['object']).columns:
        print("\n" + column)
        print(data[column].value_counts())

def main():
    data = load_data('datos_desercion.csv')
    numerical_analysis(data)
    categorical_analysis(data)

if __name__ == "__main__":
    main()

