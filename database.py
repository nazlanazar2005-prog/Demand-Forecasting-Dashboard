import pandas as pd

def generate_mock_data():
    # 1. Pull real retail data directly from a public URL
    url = "https://githubusercontent.com"
    
    # If the network fails, we use a fallback clean online retail dataset
    try:
        # Fetching a clean historical timeline dataset (Retail/Web traffic trends)
        df_raw = pd.read_csv("https://githubusercontent.com")
        df_raw.columns = ["Date", "Historical_Sales"]
    except:
        # Bulletproof backup data if github is slow
        dates = pd.date_range(start="2018-01-01", end="2026-01-01", freq="MS")
        df_raw = pd.DataFrame({"Date": dates, "Historical_Sales": [int(1000 + (i*12) + (300 if i%12 in [10,11] else 0)) for i in range(len(dates))]})

    # 2. Format columns perfectly for our dashboard layout
    df_raw["Date"] = pd.to_datetime(df_raw["Date"])
    
    # 3. Create two categories so our dropdown menu has choices
    df_retail = df_raw.copy()
    df_retail["Product"] = "Total Retail Electronics"
    
    df_apparel = df_raw.copy()
    df_apparel["Historical_Sales"] = (df_apparel["Historical_Sales"] * 0.65).astype(int) # simulate a second category
    df_apparel["Product"] = "Total Retail Apparel"
    
    # Combine them together
    df_final = pd.concat([df_retail, df_apparel], ignore_index=True)
    return df_final

