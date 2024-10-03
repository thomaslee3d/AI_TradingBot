import ccxt
import logging
from utils.config import Config
from utils.logger import get_logger

def initialize_exchange():
    config = Config('config/config.yaml')
    exchange = ccxt.binance({
        'apiKey': config.get('BINANCE_API_KEY'),
        'secret': config.get('BINANCE_SECRET_KEY'),
        'enableRateLimit': True,
    })
    return exchange

def execute_trade(signals):
    exchange = initialize_exchange()
    symbol = 'BTC/USDT'
    amount = 0.001  # Example: Buy/Sell 0.001 BTC

    for signal in signals:
        if signal == 1:
            # Place a buy order
            order = exchange.create_market_buy_order(symbol, amount)
            logging.info(f'Buy Order Executed: {order}')
        elif signal == -1:
            # Place a sell order
            order = exchange.create_market_sell_order(symbol, amount)
            logging.info(f'Sell Order Executed: {order}')
        else:
            logging.info('Hold Signal: No Action Taken')
