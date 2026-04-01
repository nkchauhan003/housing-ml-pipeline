import os
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def train(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def main():
    # Get project root path
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    # Build correct path
    data_path = os.path.join(BASE_DIR, "data", "raw", "housing.csv")

    print("Loading from:", data_path)

    # Step 1: Load data
    df = pd.read_csv(data_path)

    # Step 2: Split features & target
    X = df.drop("price", axis=1)
    y = df["price"]

    # Step 3: Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Step 4: Train model
    model = train(X_train, y_train)

    # Step 5: Save model
    model_dir = os.path.join(BASE_DIR, "models")
    os.makedirs(model_dir, exist_ok=True)  # ensure directory exists

    model_path = os.path.join(model_dir, "housing_model.pkl")

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print("✅ Model trained and saved!")


if __name__ == "__main__":
    main()