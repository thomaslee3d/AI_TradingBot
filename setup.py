# main.py

import schedule
import time
import logging
from utils.config import Config
from utils.logger import setup_logger
from utils.data_handler import fetch_data, preprocess_data
from models.predict import load_model, make_prediction
from strategies.strategy import generate_signals
from trading.execute_trade import execute_trade

def job():
    try:
        # Fetch raw data
        raw_data = fetch_data()
        logging.info("Fetched raw data.")

        # Preprocess data
        processed_data = preprocess_data(raw_data)
        logging.info("Preprocessed data.")

        # Load model and scaler
        model = load_model()
        scaler = load_scaler()
        logging.info("Loaded model and scaler.")

        # Prepare data for prediction
        features = processed_data.drop(['Target'], axis=1).values
        scaled_features = scaler.transform(features)

        # Make predictions
        predictions = make_prediction(model, scaled_features)
        logging.info("Made predictions.")

        # Generate trading signals
        signals = generate_signals(predictions, processed_data)
        logging.info(f"Generated signals: {signals}")

        # Execute trades
        execute_trade(signals)
        logging.info("Executed trades based on signals.")

    except Exception as e:
        logging.error(f"Error during job execution: {e}")

if __name__ == "__main__":
    # Load configuration
    config = Config('config/config.yaml')

    # Setup logger
    logger = setup_logger(config.get('LOG_FILE'))

    logging.info("Starting Trading Bot.")

    # Schedule the job
    schedule_interval = config.get('SCHEDULE_INTERVAL_MINUTES', 60)
    schedule.every(schedule_interval).minutes.do(job)

    logging.info(f"Scheduled job every {schedule_interval} minutes.")

    # Run the scheduled jobs
    while True:
        schedule.run_pending()
        time.sleep(1)
