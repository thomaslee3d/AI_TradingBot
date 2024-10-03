import pandas as pd
from backtesting import Backtest, Strategy
from strategies.strategy import generate_signals


class MLStrategy(Strategy):
    def init(self):
        # Initialize indicators or models here if needed
        pass

    def next(self):
        # Generate signals based on model predictions
        prediction = self.data.Close[-1]  # Placeholder for actual model prediction
        signal = generate_signals(prediction, self.data)

        if signal == 1 and not self.position:
            self.buy()
        elif signal == -1 and self.position:
            self.sell()


def run_backtest():
    data = pd.read_csv('data/processed/btc_usdt_processed.csv', index_col='timestamp', parse_dates=True)
    bt = Backtest(data, MLStrategy, cash=10000, commission=.002)
    stats = bt.run()
    bt.plot()
    print(stats)


if __name__ == "__main__":
    run_backtest()
