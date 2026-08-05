from src.services.market_service import MarketService

service = MarketService()

indices = service.get_all_indices()

print(type(indices))

print("\nShape:")
print(indices.shape)

print("\nColumns:")
print(indices.columns.tolist())

print("\nFirst 15 Rows:")
print(indices.head(15))