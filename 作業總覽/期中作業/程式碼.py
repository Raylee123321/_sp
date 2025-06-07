import requests

# 查詢股票代號（Yahoo 使用 TW 結尾）
symbols = ["2330.TW", "2303.TW", "2317.TW"]  # 台積電、聯電、鴻海

# 將股票代碼組成 URL 查詢字串
symbol_query = "%2C".join(symbols)

url = f"https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.getQuoteListV2?symbols={symbol_query}&fields=ask,bid,regularMarketPrice,regularMarketChange,regularMarketChangePercent"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# 發送 GET 請求
res = requests.get(url, headers=headers)
data = res.json()

# 顯示即時報價資訊
for item in data["data"]["quotes"]:
    print(f"📈 {item['shortName']} ({item['symbol']})")
    print(f"   現價：{item['regularMarketPrice']} 元")
    print(f"   漲跌：{item['regularMarketChange']} 元（{item['regularMarketChangePercent']}%）")
    print(f"   買價：{item.get('bid', 'N/A')}，賣價：{item.get('ask', 'N/A')}")
    print()

