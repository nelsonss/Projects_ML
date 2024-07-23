from src import descriptive_analysis
from src import supervised_learning
from src import unsupervised_learning

def main():
    while True:
        print("\nStudent Dropout Analysis and Prediction:")
        print("1. Perform descriptive analysis")
        print("2. Perform supervised learning")
        print("3. Perform unsupervised learning")
        print("4. Exit")
        choice = input("Enter your choice ? : ")

        if choice == '1':
            descriptive_analysis.main()
        elif choice == '2':
            supervised_learning.main()
        elif choice == '3':
            unsupervised_learning.main()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


