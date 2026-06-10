import joblib

def load_model():

    return joblib.load(
        "models/sales_forecast_model.pkl"
    )