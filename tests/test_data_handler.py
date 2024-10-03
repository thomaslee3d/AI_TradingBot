import unittest
from utils.data_handler import fetch_data, preprocess_data

class TestDataHandler(unittest.TestCase):
    def test_fetch_data(self):
        data = fetch_data()
        self.assertIsNotNone(data)
        self.assertFalse(data.empty)

    def test_preprocess_data(self):
        raw_data = fetch_data()
        processed_data = preprocess_data(raw_data)
        self.assertIn('SMA', processed_data.columns)
        self.assertIn('RSI', processed_data.columns)
        self.assertIn('MACD', processed_data.columns)
        self.assertIn('Target', processed_data.columns)
        self.assertFalse(processed_data.empty)

if __name__ == '__main__':
    unittest.main()
