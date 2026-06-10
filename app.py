import streamlit as st

st.set_page_config(
    page_title="AI Sales Analytics Platform",
    page_icon="🚀",
    layout="wide"
)

# ===================================
# CUSTOM CSS
# ===================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.hero {
    background: linear-gradient(135deg,#0f172a,#1e293b);
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 20px;
}

.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #334155;
}

.card h3 {
    color: white;
}

.card p {
    color: #38bdf8;
    font-size: 20px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ===================================
# HERO SECTION
# ===================================

st.markdown("""
<div class="hero">

# 🚀 Intelligent Sales Forecasting & Inventory Optimization

### AI-Powered Business Analytics Platform

Analyze Sales • Forecast Revenue • Optimize Inventory

</div>
""", unsafe_allow_html=True)

# ===================================
# KPI CARDS
# ===================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📊 Modules</h3>
    <p>8</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>🤖 ML Models</h3>
    <p>1</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>📄 Reports</h3>
    <p>PDF + Excel</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
    <h3>⚡ Analytics</h3>
    <p>Real-Time</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ===================================
# FEATURES
# ===================================

st.subheader("✨ Platform Features")

c1, c2 = st.columns(2)

with c1:
    st.success("📤 Data Upload")
    st.success("🧹 Data Preprocessing")
    st.success("📊 Exploratory Data Analysis")
    st.success("📦 Inventory Optimization")

with c2:
    st.success("🤖 Machine Learning")
    st.success("📈 Sales Forecasting")
    st.success("📄 PDF & Excel Reports")
    st.success("⚡ Real-Time Dashboard")

st.markdown("---")

st.subheader("🎯 Workflow")

st.info("""
1️⃣ Upload Dataset

2️⃣ Data Preprocessing

3️⃣ Exploratory Data Analysis

4️⃣ Inventory Optimization

5️⃣ Model Training

6️⃣ Sales Forecasting

7️⃣ Generate Reports
""")

st.success("✅ Project Ready for Analysis")