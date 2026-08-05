from src.clients.nse_client import NSEClient


class MarketService:
    """
    Service layer responsible for processing market data.
    """

    def __init__(self):
        self.client = NSEClient()

    def get_top_gainers(self):
        return self.client.get_top_gainers()

    def get_top_losers(self):
        return self.client.get_top_losers()

    def get_all_indices(self):
        return self.client.get_all_indices()

    def get_top_5_gainers(self):
        gainers = self.client.get_top_gainers()

        return gainers[["symbol", "ltp", "perChange"]].head(5)

    def get_market_summary(self):
        """
        Generate a simple market summary.
        """

        gainers = self.client.get_top_gainers()
        losers = self.client.get_top_losers()

        summary = {
            "Top Gainer": gainers.iloc[0]["symbol"],
            "Top Gainer %": gainers.iloc[0]["perChange"],
            "Top Loser": losers.iloc[0]["symbol"],
            "Top Loser %": losers.iloc[0]["perChange"],
            "Average Gain %": round(gainers["perChange"].mean(), 2),
            "Average Loss %": round(losers["perChange"].mean(), 2),
        }

        return summary