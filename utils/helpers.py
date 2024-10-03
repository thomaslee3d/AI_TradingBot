def calculate_sharpe_ratio(returns, risk_free_rate=0.0):
    """
    Calculate the Sharpe Ratio of a returns series.
    """
    return (returns.mean() - risk_free_rate) / returns.std()
