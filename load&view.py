import pandas as pd


def load_data(file_path):
    try:
        data= pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None

data = load_data("data/Titanic-Dataset.csv")

def survivors(data):
    if data is not None:
        survived_count = data["Survived"].sum()
        print(f"Number of survivors: {survived_count}")
    else:
        print("Data is None. Cannot compute.")

def Age_count(data):
    if data is not None:
        age_counts = data["Age"].value_counts()
        print("Age counts:")
        print(age_counts)
    else:
        print("Data is None. Cannot compute.")

Age_count(data)

def gender_count(data):
    if data is not None:
        gender_counts = data["Sex"].value_counts()
        print("Gender counts:")
        print(gender_counts)
    else:
        print("Data is None. Cannot compute.")

survivors(data)
Age_count(data)
gender_count(data)