import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from models.predict import load_model, load_scaler

def evaluate():
    # Load processed data
    data = pd.read_csv('data/processed/btc_usdt_processed.csv')
    X = data.drop(['Target'], axis=1)
    y = data['Target']

    # Load scaler and model
    scaler = load_scaler()
    model = load_model()

    # Scale features
    X_scaled = scaler.transform(X)

    # Make predictions
    predictions = model.predict(X_scaled)
    predicted_classes = predictions.argmax(axis=1) - 1  # Adjusting class indices if necessary

    # Evaluation
    print(confusion_matrix(y, predicted_classes))
    print(classification_report(y, predicted_classes))

if __name__ == "__main__":
    evaluate()
