from src.services.market_service import MarketService
from src.analytics.index_analytics import IndexAnalytics


class AnalyticsService:
    """
    Coordinates all analytics modules.
    """

    def __init__(self):
        self.market_service = MarketService()
        self.index_analytics = IndexAnalytics()

    def get_major_indices(self):
        """
        Returns the major market indices.
        """
        indices = self.market_service.get_all_indices()

        return self.index_analytics.get_major_indices(indices)

    def market_overview(self):
        gainers = self.market_service.get_top_gainers()
        losers = self.market_service.get_top_losers()

        return {
            "Top Gainer": gainers.iloc[0]["symbol"],
            "Top Gainer %": gainers.iloc[0]["perChange"],
            "Top Loser": losers.iloc[0]["symbol"],
            "Top Loser %": losers.iloc[0]["perChange"],
            "Average Gain %": round(gainers["perChange"].mean(), 2),
            "Average Loss %": round(losers["perChange"].mean(), 2),
        }

    def market_breadth(self):
        gainers = self.market_service.get_top_gainers()
        losers = self.market_service.get_top_losers()

        advances = len(gainers)
        declines = len(losers)

        if advances > declines:
            sentiment = "Bullish 🟢"
        elif declines > advances:
            sentiment = "Bearish 🔴"
        else:
            sentiment = "Neutral 🟡"

        return {
            "Advances": advances,
            "Declines": declines,
            "Market Sentiment": sentiment,
        }