import streamlit as st
import pandas as pd
from job_scraper import get_all_jobs

st.set_page_config(page_title="Multi-Site Job Aggregator")
st.title("🧠 Multi-Site Job Aggregator")

keyword = st.text_input("Enter job keyword")

if keyword.strip():
    with st.spinner("Fetching jobs..."):
        df = get_all_jobs(keyword.strip())

    if df.empty:
        st.warning("No jobs found!")
    else:
        st.success(f"Found {len(df)} jobs!")

        # Filters
        st.sidebar.header("🔍 Filters")
        location_options = ["All"] + sorted(df['location'].dropna().unique())
        type_options = ["All"] + sorted(df['type'].dropna().unique())
        source_options = ["All"] + sorted(df['source'].dropna().unique())

        selected_location = st.sidebar.selectbox("📍 Location", options=location_options, index=0)
        selected_type = st.sidebar.selectbox("🧾 Job Type", options=type_options, index=0)
        selected_source = st.sidebar.selectbox("🌐 Source", options=source_options, index=0)

        filtered_df = df.copy()
        if selected_location != "All":
            filtered_df = filtered_df[filtered_df['location'] == selected_location]
        if selected_type != "All":
            filtered_df = filtered_df[filtered_df['type'] == selected_type]
        if selected_source != "All":
            filtered_df = filtered_df[filtered_df['source'] == selected_source]

        st.write(f"Showing {len(filtered_df)} filtered jobs")
        st.dataframe(filtered_df)

        # Download button
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download as CSV", csv, "job_listings.csv", "text/csv")
