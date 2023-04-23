import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler




if __name__ == "__main__":   

    data = pd.read_csv("data.csv")

    X = data.drop("label_column_name", axis=1)
    y = data["label_column_name"]


    categorical_cols = ["categorical_col1", "categorical_col2"]
    for col in categorical_cols:
        encoder = LabelEncoder()
        X[col] = encoder.fit_transform(X[col])

    numeric_cols = ["numeric_col1", "numeric_col2"]
    scaler = StandardScaler()
    X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    data = pd.read_csv('data.csv')
    print(data)

