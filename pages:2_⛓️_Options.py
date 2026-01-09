import streamlit as st
import yfinance as yf

st.title("⛓️ Option Trading: Calls & Puts")
ticker = st.text_input("Enter Ticker:", value="NVDA").upper()
stock = yf.Ticker(ticker)

try:
    expiry = stock.options[0]
    chain = stock.option_chain(expiry)
    # Math: (Open Interest * Last Price * 100)
    call_impact = (chain.calls['openInterest'] * chain.calls['lastPrice'] * 100).sum()
    put_impact = (chain.puts['openInterest'] * chain.puts['lastPrice'] * 100).sum()
    
    c1, c2 = st.columns(2)
    c1.metric("Call Dollar Impact (Bulls)", f"${call_impact/1e6:.2f}M")
    c2.metric("Put Dollar Impact (Bears)", f"${put_impact/1e6:.2f}M")
except:
    st.error("No options data for this asset.")