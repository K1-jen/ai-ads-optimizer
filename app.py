import streamlit as st
import pandas as pd

st.title("📢 AI Ads Optimizer")

file = st.file_uploader("Upload Campaign CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.write("Campaign Data", df)

    if "spend" in df.columns and "conversions" in df.columns:
        df["CPA"] = df["spend"] / df["conversions"].replace(0,1)
        st.write("📊 Cost Per Acquisition", df)

        worst = df.sort_values("CPA", ascending=False).head(3)
        st.subheader("💸 Highest Wasted Spend")
        st.write(worst)

        st.subheader("🤖 Recommendations")
        st.write("- Reduce budget on highest CPA campaigns")
        st.write("- Reallocate to better converters")
        st.write("- Test new audience segments")
