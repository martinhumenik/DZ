import os

# TABLE_NAME=os.getenv("SP500", "sp500")
sql_columns = ['name', 'symbol', 'sector', 'price', 'market_cap', 'pe', 'pb', 'ps', 'ebitda', 'eps', 'div_yield']

POSTGRES_HOST=os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_DATABASE=os.getenv("POSTGRES_DATABASE", "postgres")
POSTGRES_USER=os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD", "postgres")

TABLE_INVESTOR_NAME = "investors_table"
TABLE_NAME = "sp500"
SECTOR_COLUMN = "sector"
COLUMN_PRICE = "price"
MARKETCAP = "market_cap"
PE = "pe"
PB = "pb"
PS = "ps"
EPS = "eps"

