import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("📈 Stocks: Bull & Bear Intelligence")
ticker = st.text_input("Search ANY Stock (e.g., NVDA, TSLA):", value="NVDA").upper()
stock = yf.Ticker(ticker)
hist = stock.history(period="6mo")

if not hist.empty:
    # 1. TRADERS' MINDSET & CORPORATE DETECTION
    curr_vol = hist['Volume'].iloc[-1]
    avg_vol = hist['Volume'].mean()
    
    if curr_vol > (avg_vol * 1.5):
        st.warning("🏢 CORPORATE MINDSET: Massive Institutional Volume detected!")
    
    # 2. SUPPORT & RESISTANCE
    res = hist['High'].max()
    sup = hist['Low'].min()
    
    # 3. CHART & SHAPES
    fig = go.Figure(data=[go.Candlestick(x=hist.index[-60:], open=hist['Open'][-60:], 
                    high=hist['High'][-60:], low=hist['Low'][-60:], close=hist['Close'][-60:])])
    fig.add_hline(y=res, line_dash="dash", line_color="red", annotation_text="RESISTANCE")
    fig.add_hline(y=sup, line_dash="dash", line_color="green", annotation_text="SUPPORT")
    st.plotly_chart(fig, use_container_width=True)