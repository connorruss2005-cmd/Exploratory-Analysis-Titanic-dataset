import pandas as pd

def load_data(file_path):
    try:
        data= pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None

data = load_data("data/Titanic-Dataset.csv")

print(data)