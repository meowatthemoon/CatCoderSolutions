import pandas as pd
from sklearn.decomposition import PCA
import numpy as np



# Load data from a CSV file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path, header = 0)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

def filter_mode(data):
    # Filter rows to include only those within the range for each specified column
    data = data[data["MODE"].isin(["auto", "beam","burst", "REDACTED"])]
    return data

def filter_power(data):
    # Filter rows to include only those within the range for each specified column
    
    data = data[data["POWER"].isin(["high", "low"])]
    return data

# Filter rows based on specified ranges
def filter_amps(data):
    # Filter rows to include only those within the range for each specified column
    data = data[(data["AMPS"] >= 0) & (data["AMPS"] <= 1)]
    return data

def filter_volts(data):
    # Filter rows to include only those within the range for each specified column
    data = data[(data["VOLTS"] >= 0.02) & (data["VOLTS"] <= 8.7)]
    return data

def filter_temp(data):
    # Filter rows to include only those within the range for each specified column
    data = data[(data["TEMP"] >= -100) & (data["TEMP"] <= 373.15)]
    return data

def filter_unit(data):
    # Filter rows to include only those within the range for each specified column
    data = data[data["UNIT"].isin(["K", "C","?"])]
    return data

def filter_delta(data):
    # Filter rows to include only those within the range for each specified column
    data = data[(data["DELTA"] >= -1) & (data["DELTA"] <= 1)]
    return data

def filter_gamma(data):
    # Filter rows to include only those within the range for each specified column
    data = data[(data["GAMMA"] >= -2) & (data["GAMMA"] <= 2)]
    return data

def filter_output(data):
    # Filter rows to include only those within the range for each specified column
    data = data[(data["GAMMA"] >= -8.4) & (data["GAMMA"] <= 9.3)]
    return data



if __name__ == "__main__":
    # read csv file
    train_path = "train_data.csv"
    train_data = load_data(train_path)


    #print(train_data)

    # drop na
    train_data = train_data.dropna()
    train_data = filter_mode(train_data)
    train_data = filter_power(train_data)
    train_data = filter_amps(train_data)
    train_data = filter_volts(train_data)
    train_data = filter_temp(train_data)
    train_data = filter_unit(train_data)
    train_data = filter_delta(train_data)
    train_data = filter_gamma(train_data)
    train_data = filter_output(train_data)

    # convert to C
    train_data.loc[train_data["UNIT"] == "K", "TEMP"] = train_data["TEMP"] - 273.15
    cols = train_data[train_data["UNIT"] == "K"]["TEMP"]
    print(np.mean(cols), np.std(cols))
    # -0.69, 48
