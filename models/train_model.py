import joblib
from sklearn.linear_model import LinearRegression

def train_model(X_train, y_train):

    model = LinearRegression()

    model.fit(X_train, y_train)

    joblib.dump(
        model,
        "models/sales_forecast_model.pkl"
    )

    return model