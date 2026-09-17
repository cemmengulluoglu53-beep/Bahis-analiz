import streamlit as st
import pandas as pd

# Sayfa Yapılandırması
st.set_page_config(page_title="Futbol Analiz Platformu", layout="wide")

st.title("⚽ Futbol Analiz Platformu")
st.caption("17 Eylül — 450 Maç Analiz Edildi")

# Sol Panel / Filtreler
st.sidebar.header("Filtreler")
min_guven = st.sidebar.slider("Minimum Güven Yüzdesi (%)", 50, 90, 60)

# Ana Sekmeler
tab1, tab2, tab3 = st.tabs(["📊 Market Analizi", "🔍 Tümünü Tara", "📈 Sistem Performansı"])

# Örnek Veri Seti
data = [
    {"Maç": "Takım A vs Takım B", "Market": "KG", "Tahmin": "KG Var", "Güven": 74, "Durum": "🟢 Güçlü"},
    {"Maç": "Takım C vs Takım D", "Market": "KG", "Tahmin": "KG Var", "Güven": 67, "Durum": "🟢 Güçlü"},
    {"Maç": "Takım E vs Takım F", "Market": "2.5 Üst", "Tahmin": "2.5 Üst", "Güven": 81, "Durum": "🟢 Çok Güçlü"},
    {"Maç": "Takım G vs Takım H", "Market": "MS1", "Tahmin": "MS 1", "Güven": 62, "Durum": "🟡 Orta"},
]
df = pd.DataFrame(data)

with tab1:
    market_secim = st.selectbox("Market Seçin", ["KG", "1.5 Üst", "2.5 Üst", "MS1", "MS2"])
    filtered_df = df[(df["Market"] == market_secim) & (df["Güven"] >= min_guven)]
    st.write(f"{market_secim} için %{min_guven} ve üzeri güvene sahip maçlar:")
    st.dataframe(filtered_df, use_container_width=True)

with tab2:
    if st.button("🔍 TÜM MAÇLARI ANALİZ ET"):
        st.success("450 maç tarandı! Yüksek güvenli fırsatlar listelendi.")
        st.dataframe(df[df["Güven"] >= min_guven], use_container_width=True)

with tab3:
    st.subheader("Geçmiş Model Performansı (Backtest)")
    st.metric(label="KG Başarı Oranı", value="%63.6", delta="0.8%")
    st.metric(label="2.5 Üst Başarı Oranı", value="%80.3", delta="2.1%")
