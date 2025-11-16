import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#1) Altın fiyatlarının geçmiş verilerini çekEN fonk
gold = yf.download(
    "BTC-USD", #çekilecek hisse maden vb.
    start="2014-01-01",
    end="2025-11-15",
    interval="1wk"
)

gold.index = pd.to_datetime(gold.index)



with pd.ExcelWriter("btcdeger.xlsx", engine='openpyxl') as writer:
    gold.to_excel(writer, sheet_name='btc Fiyatları', index=True)

print("Veri kaydedildi: btcdeger.xlsx")

# --- 4) Grafik çiz ---
plt.figure(figsize=(10,5))
plt.plot(gold['Close'], label='btc usd Fiyatı', color='gold')
plt.title('Haftalık btc usd Fiyatları (10 Yıl)')
plt.xlabel('Tarih')
plt.ylabel('Fiyat (USD)')
plt.legend()
plt.grid(True)
plt.show()
