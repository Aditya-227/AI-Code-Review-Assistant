import git
import os
import shutil
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time

from repo_loader import load_repository, get_file_change_frequency
from feature_extractor import extract_repo_features
from bug_predictor import BugPredictor
from code_review import analyze_repository
from health_score import calculate_health_score

st.set_page_config(page_title="AI Code Review Assistant", layout="wide")

st.markdown("""

<style>

.main-title {
    text-align:center;
    font-size:48px;
    font-weight:700;
    margin-bottom:10px;
}

.sub-title {
    text-align:center;
    font-size:18px;
    color:gray;
    margin-bottom:40px;
}

.hero {
    padding-top:40px;
    padding-bottom:40px;
}

.metric-card {
    text-align:center;
    padding:10px;
}

</style>

""", unsafe_allow_html=True)

st.markdown('<div class="hero">', unsafe_allow_html=True)

st.markdown(
'<div class="main-title">AI Code Review & Bug Prediction Assistant</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="sub-title">Analyze Git repositories to detect bug risks, code complexity problems and repository health insights.</div>',
unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1,2,1])

with col2:


    repo_url = st.text_input("Enter GitHub Repository URL")
    analyze = st.button("Analyze Repository")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if analyze and repo_url:
    
        progress = st.progress(0)
    
        time.sleep(0.2)
        progress.progress(10)
    
        repo_path = "temp_repo"
    
        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)
    
        git.Repo.clone_from(repo_url, repo_path)
    
        repo = load_repository(repo_path)
    
        progress.progress(20)
    
        freq = get_file_change_frequency(repo)
    
        progress.progress(30)
    
        features = extract_repo_features(repo_path, freq)
    
        progress.progress(45)
    
        predictor = BugPredictor()
    
        predictions = predictor.predict(features)
    
        progress.progress(60)
    
        issues = analyze_repository(repo_path)
    
        progress.progress(75)
    
        score = calculate_health_score(features, predictions, issues)
    
        progress.progress(100)
    
        st.success("Analysis Complete")
    
        predictions["file"] = predictions["file"].apply(lambda x: x.split("/")[-1])
        df = predictions.copy()
    
        st.header("Repository Health Overview")
    
        col1, col2, col3 = st.columns(3)
    
        col1.metric("Health Score", f"{score}%")
        col2.metric("Files Analyzed", len(df))
        col3.metric("Code Issues", len(issues))
    
    
        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": "Repository Health Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "green"},
                "steps": [
                    {"range": [0, 40], "color": "red"},
                    {"range": [40, 70], "color": "orange"},
                    {"range": [70, 100], "color": "green"}
                ],
            },
        ))
    
        st.plotly_chart(gauge, use_container_width=True)
    
    
        st.divider()
    
        st.subheader("Bug Risk Per File")
    
        df_sorted = df.sort_values("bug_probability", ascending=False)
    
        st.dataframe(df_sorted[["file","bug_probability"]], use_container_width=True)
    
    
        st.subheader("Top Risk Files")
    
        top_risk = df_sorted.head(5)
    
        fig_top = px.bar(
            top_risk,
            x="file",
            y="bug_probability",
            color="bug_probability",
            title="Top High-Risk Files"
        )
    
        st.plotly_chart(fig_top, use_container_width=True)
    
    
        st.subheader("Bug Probability Distribution")
    
        fig_hist = px.histogram(
            df,
            x="bug_probability",
            nbins=10,
            title="Bug Probability Distribution"
        )
    
        st.plotly_chart(fig_hist, use_container_width=True)
    
    
        st.subheader("Code Complexity Overview")
    
        feature_df = pd.DataFrame(features)
        feature_df["file"] = feature_df["file"].apply(lambda x: x.split("/")[-1])
    
        fig_complex = px.scatter(
            feature_df,
            x="lines_of_code",
            y="cyclomatic_complexity",
            size="function_count",
            hover_name="file",
            title="Complexity vs File Size"
        )
    
        st.plotly_chart(fig_complex, use_container_width=True)
    
    
        st.subheader("Code Review Issues")
    
        if issues:
            st.dataframe(pd.DataFrame(issues), use_container_width=True)
        else:
            st.success("No major code review issues detected")
    
    
        st.divider()
    
        st.header("AI Repository Summary")
    
        avg_bug = df["bug_probability"].mean()
    
        if score > 80:
            status = "Excellent"
        elif score > 60:
            status = "Moderate"
        else:
            status = "Needs Attention"
    
        st.info(f"""
    ```
    
    Repository Health Status: {status}
    
    Average Bug Probability: {round(avg_bug,2)}
    
    Total Files Analyzed: {len(df)}
    
    Detected Code Issues: {len(issues)}
    
    This AI system analyzed repository structure, commit history, code complexity and predicted potential bug risk using automated analysis techniques.
    
    """)
    
