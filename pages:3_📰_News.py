import streamlit as st
import yfinance as yf

st.title("📰 Latest News & Geopolitical Impact")
ticker = st.text_input("Filter Stock News:", value="NVDA").upper()
news = yf.Search(ticker, news_count=5).news

for n in news:
    st.subheader(n.get('title'))
    st.write(f"Source: {n.get('publisher')} | [Read More]({n.get('link')})")