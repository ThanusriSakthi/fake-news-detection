import streamlit as st
from main import predict_news

st.set_page_config(page_title="Fake News Detector", page_icon="📰", layout="centered")

# 🔥 FINAL FIX CSS
st.markdown("""
<style>

/* Hide header elements */
header, footer {
    display: none !important;
}

[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stHeader"] {
    display: none !important;
}

/* 🔥 Pull content UP to cover top box */
.block-container {
    margin-top: -80px !important;
    padding-top: 0 !important;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #dbeafe, #f1f5f9);
}

/* Card */
.glass {
    background: rgba(255, 255, 255, 0.95);
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    max-width: 700px;
    margin: auto;
}

/* Title */
.title {
    font-size: 32px;
    font-weight: bold;
    text-align: center;
    color: #1e293b;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #64748b;
    margin-bottom: 20px;
}

/* Textarea */
textarea {
    border-radius: 12px !important;
}

/* Button */
.stButton>button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    background: linear-gradient(135deg, #2563eb, #3b82f6);
    color: white;
    font-size: 16px;
    border: none;
}

/* Results */
.result-real {
    background: #dcfce7;
    padding: 15px;
    border-radius: 10px;
    color: #166534;
    font-weight: bold;
    margin-top: 15px;
}

.result-fake {
    background: #fee2e2;
    padding: 15px;
    border-radius: 10px;
    color: #991b1b;
    font-weight: bold;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)

# 🧊 UI
st.markdown('<div class="glass">', unsafe_allow_html=True)

st.markdown('<div class="title">📰 Fake News Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered news verification system</div>', unsafe_allow_html=True)

news = st.text_area("", placeholder="Paste your news here...", height=150)

if st.button("🔍 Analyze News"):
    if news.strip():
        result = predict_news(news)

        if "REAL" in result:
            st.markdown(f'<div class="result-real">{result}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="result-fake">{result}</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter some text")

st.markdown('</div>', unsafe_allow_html=True)