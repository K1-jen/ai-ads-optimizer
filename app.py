import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Ads Optimizer",
    page_icon="📢",
    layout="wide"
)

st.title("📢 AI Ads Optimizer")
st.caption("Analyze campaign data, uncover wasted spend, and optimize marketing ROI.")

file = st.file_uploader("Upload Campaign CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("📄 Campaign Data")
    st.dataframe(df, use_container_width=True)

    if "spend" in df.columns and "conversions" in df.columns:

        df["CPA"] = df["spend"] / df["conversions"].replace(0,1)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("💰 Total Spend", f"${df['spend'].sum():,.0f}")

        with col2:
            st.metric("🎯 Total Conversions", int(df["conversions"].sum()))

        with col3:
            st.metric("📉 Avg CPA", f"${df['CPA'].mean():.2f}")

        st.subheader("⚠️ Highest Cost Campaigns")
        st.dataframe(
            df.sort_values("CPA", ascending=False).head(3),
            use_container_width=True
        )

        st.subheader("🤖 AI Recommendations")

        st.success("Reduce budget on highest CPA campaigns")
        st.success("Shift spend to best converters")
        st.success("Test fresh audience segments")

        st.success("Reduce budget on highest CPA campaigns")
        st.success("Shift spend to best converters")
        st.success("Test fresh audience segments")
