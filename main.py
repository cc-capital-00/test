
import platform
import sys

from config.check_packages import check_and_install

check_and_install()

import numpy as np
import pandas as pd

print("\n=== Environment Information ===")
print("Operating system:", platform.system())
print("Python version:", sys.version.split()[0])
print("Python executable:", sys.executable)
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)

data = {
    "Ticker": ["AAPL", "MSFT", "AMD"],
    "Shares": [10, 5, 20],
    "Price": [250.0, 520.0, 200.0],
}

df = pd.DataFrame(data)
df["MarketValue"] = df["Shares"] * df["Price"]

print("\n=== Portfolio DataFrame ===")
print(df.to_string(index=False))
print("\nTotal portfolio value:", df["MarketValue"].sum())
print("\nTEST PASSED")
