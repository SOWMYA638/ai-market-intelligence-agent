from nselib import capital_market


class NSEClient:
    """
    Client for fetching market data from NSE using nselib.
    """

    def get_all_indices(self):
        return capital_market.market_watch_all_indices()

    def get_top_gainers(self):
        return capital_market.top_gainers_or_losers("gainers")

    def get_top_losers(self):
        return capital_market.top_gainers_or_losers("loosers")