from clients.nse_client import NSEClient

client = NSEClient()

print("===== TOP GAINERS =====")
print(client.get_top_gainers())

print("\n===== TOP LOSERS =====")
print(client.get_top_losers())

print("\n===== ALL INDICES =====")
print(client.get_all_indices())