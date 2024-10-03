import joblib
from tensorflow.keras.models import load_model as keras_load_model

def load_model(model_path='models/trained_model.h5'):
    return keras_load_model(model_path)

def load_scaler(scaler_path='models/scaler.pkl'):
    return joblib.load(scaler_path)

def save_model(model, scaler, model_path='models/trained_model.h5', scaler_path='models/scaler.pkl'):
    model.save(model_path)
    joblib.dump(scaler, scaler_path)

def make_prediction(model, data):
    return model.predict(data)
