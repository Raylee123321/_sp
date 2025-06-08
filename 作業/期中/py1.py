import yfinance as yf
from concurrent.futures import ThreadPoolExecutor

# 嘗試不同市場代碼組合
def fetch_stock_dynamic(user_input):
    suffixes = ['.TW', '.TWO']  # 上市、上櫃
    for suffix in suffixes:
        full_code = user_input + suffix
        try:
            stock = yf.Ticker(full_code)
            df = stock.history(period="5d")
            if not df.empty:
                df.index = df.index.strftime('%Y-%m-%d')
                df = df[['Open', 'High', 'Low', 'Close']]
                return f"{user_input}（{full_code}）", df
        except Exception:
            continue
    return f"{user_input}（查無資料）", None

# 主查詢函數
def query_stocks(symbols):
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(fetch_stock_dynamic, symbols)

    for name, df in results:
        print(f"\n📈 {name}")
        if df is not None:
            print(df)
        else:
            print("⚠️ 無法取得資料（可能代碼錯誤或沒上市）")

# 使用者輸入多筆代碼
while True:
    user_input = input("\n請輸入多支股票代碼（空格分隔，例如：2330 3008 6869），或輸入 off 離開：")

    if user_input.lower() == "off":
        print("程式結束。")
        break

    codes = user_input.strip().split()
    if codes:
        query_stocks(codes)
    else:
        print("請至少輸入一筆代碼。")
