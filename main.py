import pandas as pd
from sklearn.model_selection import train_test_split
import csv

def print_data(x):
    for r in x:
        print(r)



if __name__ == "__main__":   

    data = pd.read_csv('data.csv')
    print(data) 

