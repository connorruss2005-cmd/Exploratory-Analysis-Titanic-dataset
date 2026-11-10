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

survivors(data)