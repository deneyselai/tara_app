import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


# Hisse senedi verisini çekelim

# symbol = "THYAO.IS"  # BIST'te işlem gören bir hisse 'Türk Hava Yolları'
# symbol = "TSLA"    # TESLA
# symbol = "NVDA"    # NVIDIA
# symbol = "CBK.DE"  # COMMERZBANK
# symbol = "ENR.DE"  # Siemens Energy
# symbol = "ARM"     # Siemens Energy
# symbol = "PLTR"    # Palantir
symbol = "RHM.DE"  # RheinMetall
# symbol = "ALTR"    # Altair Ibnül Vahad
# symbol = "LDO.MI"  # Leonardo 
# symbol = "AMD"     # AMD
# symbol = "MTX.DE"  # MTU
# symbol ="^GSPC"    # S&P 500


# tarih aralığımızı belirliyoruz
start_date = "2023-01-01"  
end_date = "2025-02-28"
data = yf.download(symbol, start=start_date, end=end_date)

# Hareketli ortalamaları hesaplayalım
data["SMA20"] = data["Close"].rolling(window=20).mean()
data["SMA50"] = data["Close"].rolling(window=50).mean()
# Alım ve satım sinyalleri oluşturma
data["Buy_Signal"] = (data["SMA20"] > data["SMA50"]) & (data["SMA20"].shift(1) <= data["SMA50"].shift(1))
data["Sell_Signal"] = (data["SMA20"] < data["SMA50"]) & (data["SMA20"].shift(1) >= data["SMA50"].shift(1))

# Grafiği çizdirme
plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="Kapanış Fiyatı", alpha=0.5)
plt.plot(data["SMA20"], label="Simple Moving Average 20 Gün", linestyle="--")
plt.plot(data["SMA50"], label="Simple Moving Average 50 Gün", linestyle="--")
plt.scatter(data.index[data["Buy_Signal"]], data["Close"][data["Buy_Signal"]], marker="^", color="g", label="Alım", alpha=1)
plt.scatter(data.index[data["Sell_Signal"]], data["Close"][data["Sell_Signal"]], marker="v", color="r", label="Satım", alpha=1)
plt.grid('true')
plt.legend()
plt.title(f"{symbol} Ticaret Sinyalleri")
plt.show()

