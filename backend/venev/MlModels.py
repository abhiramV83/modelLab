from fastapi import UploadFile
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import  LabelEncoder
from sklearn.linear_model import LogisticRegression


# supervised = ["K_Nearest_Neighbours","Linear_Regression","Logistic_Regression"]
def knn(file: UploadFile):
        df = pd.read_csv(file.file)
        x = df.iloc[:, :-1]
        y = df.iloc[:, -1]


        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)


        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X_train_scaled, y_train)


        y_pred = knn.predict(X_test_scaled)


        accuracy = accuracy_score(y_test, y_pred)
        return f"Accuracy : {accuracy * 100:.2f} %"
def Linear_Regression(file: UploadFile):
    
        df = pd.read_csv(file.file)
        x = df.iloc[:, :-1]
        y = df.iloc[:, -1]

        if not pd.api.types.is_numeric_dtype(y):
                return "Linear Regression requires numeric target values"


        X_train, X_test, y_train, y_test = train_test_split(
                x, y, test_size=0.2, random_state=42
        )

        lr = LinearRegression()
        lr.fit(X_train, y_train)

        y_pred = lr.predict(X_test)

        score = r2_score(y_test, y_pred)
        return f"R2 Score : {score * 100:.2f}"



def Logistic_Regression(file: UploadFile):
    # Read dataset
    df = pd.read_csv(file.file)
    x = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Encode categorical labels
    if y.dtype == "object":
        le = LabelEncoder()
        y = le.fit_transform(y)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Logistic Regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)

    return f"Accuracy : {accuracy * 100:.2f} %"

import pandas as pd
from fastapi import UploadFile
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def Naive_Bayes(file: UploadFile):
    file.file.seek(0)   # 🔥 IMPORTANT

    df = pd.read_csv(file.file)

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    if y.dtype == "object":
        le = LabelEncoder()
        y = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = GaussianNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    return f"Accuracy : {accuracy * 100:.2f} %"
