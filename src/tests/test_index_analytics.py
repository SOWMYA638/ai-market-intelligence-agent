from src.analytics.index_analytics import IndexAnalytics
from src.services.market_service import MarketService

service = MarketService()
analytics = IndexAnalytics()

indices = service.get_all_indices()

major_indices = analytics.get_major_indices(indices)

print(major_indices)