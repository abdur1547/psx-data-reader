# Run this in Python interpreter or create a test script
from psx import stocks
import datetime

# Get all available tickers
# all_tickers = tickers()
# print(f"Found {len(all_tickers)} tickers")

# Test downloading sample data
data = stocks("SILK", start=datetime.date(2023, 1, 1), end=datetime.date(2023, 1, 31))
print(data)
print(f"Downloaded {len(data)} rows of data for SILK")
