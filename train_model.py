import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from models.predict import save_model
from models.model_architecture import build_model

def train():
    # Load processed data
    data = pd.read_csv('data/processed/btc_usdt_processed.csv')
    X = data.drop(['Target'], axis=1)
    y = data['Target']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Build model
    model = build_model(input_dim=X_train_scaled.shape[1])

    # Train model
    model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_data=(X_test_scaled, y_test))

    # Save model and scaler
    save_model(model, scaler)

if __name__ == "__main__":
    train()
