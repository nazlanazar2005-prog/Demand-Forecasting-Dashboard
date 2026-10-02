import pandas as pd
from prophet import Prophet

def generate_forecast(df_product, months_to_predict=6):
    # 1. Format data frame explicitly to fit Prophet requirements (columns must be 'ds' and 'y')
    df_prophet = df_product[["Date", "Historical_Sales"]].copy()
    df_prophet = df_prophet.rename(columns={"Date": "ds", "Historical_Sales": "y"})
    
    # 2. Instantiate and train the advanced seasonal algorithm
    model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    model.fit(df_prophet)
    
    # 3. Project timeline dates out into the future
    future_dates = model.make_future_dataframe(periods=months_to_predict, freq='MS')
    
    # 4. Predict expected demand curves mapping historical seasonality spikes
    forecast_raw = model.predict(future_dates)
    
    # 5. Extract only the newly generated future runway dates 
    future_predictions = forecast_raw.iloc[-months_to_predict:][["ds", "yhat"]].copy()
    future_predictions = future_predictions.rename(columns={"ds": "Date", "yhat": "Forecast_Baseline"})
    
    # Clean output parameters: Round floats and ensure no negative counts
    future_predictions["Forecast_Baseline"] = future_predictions["Forecast_Baseline"].round().astype(int)
    future_predictions.loc[future_predictions["Forecast_Baseline"] < 0, "Forecast_Baseline"] = 0
    
    return future_predictions
