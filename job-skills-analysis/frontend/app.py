import streamlit as st
import pandas as pd
import requests
from urllib.parse import quote
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# -----------------------------
# Streamlit page config
# -----------------------------
st.set_page_config(page_title="Skills by Role", layout="centered")
st.title("Skills by Role")
st.markdown("Select a role from the dropdown below and click 'Get top skills' to call the backend API.")

# -----------------------------
# Hardcoded roles
# -----------------------------
roles = [
    "Software Engineer",
    "Senior Software Engineer",
    "Backend Software Engineer",
    "Frontend Software Engineer",
    "Data Engineer",
    "Data Scientist",
    "Other",
]

role = st.selectbox("Select role", roles)

top_k = st.slider("Top K skills to show", min_value=1, max_value=30, value=10)

# -----------------------------
# Fetch data from backend
# -----------------------------
if st.button("Get top skills"):
    api_url = f"http://127.0.0.1:8000/skills/{quote(role, safe='')}"
    st.info(f"Calling API: {api_url}?top_k={top_k}")
    
    try:
        resp = requests.get(api_url, params={"top_k": top_k}, timeout=5)
    except requests.RequestException as e:
        st.error(f"Error calling API: {e}")
    else:
        if resp.status_code == 200:
            data = resp.json()
            top_skills = data.get("top_skills", {})
            
            if not top_skills:
                st.info("No skills returned for this role.")
            else:
                # Convert to DataFrame
                df = pd.DataFrame.from_dict(top_skills, orient="index", columns=["count"])
                df.index.name = "skill"
                df = df.reset_index().sort_values("count", ascending=False)
                
                # 1️⃣ Table
                st.subheader(f"Top {top_k} skills for {data.get('role')}")
                st.table(df.head(top_k).reset_index(drop=True))
                
                # 2️⃣ Bar chart
                chart_df = df.head(top_k).set_index("skill")
                st.subheader("Bar Chart of Top Skills")
                st.bar_chart(chart_df)
                
                # 3️⃣ Heatmap
                plt.figure(figsize=(10,4))
                sns.heatmap(df.head(top_k).set_index("skill"), annot=True, fmt="d", cmap="YlGnBu", cbar=True)
                plt.title(f"Top {top_k} skills for {role}")
                plt.ylabel("Skill")
            
                st.pyplot(plt)
                plt.clf()

             
                
                # 4️⃣ Word Cloud
                st.subheader("Word Cloud of Top Skills")
                wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(top_skills)
                plt.figure(figsize=(10,5))
                plt.imshow(wordcloud, interpolation="bilinear")
                plt.axis("off")
                st.pyplot(plt)
                plt.clf()
                
        else:
            try:
                err = resp.json()
            except Exception:
                err = resp.text
            st.error(f"API error ({resp.status_code}): {err}")

# -----------------------------
# Footer instructions
# -----------------------------
st.markdown("---")
st.markdown(
    "If the backend isn't running, start it with:\n"
    "`python -m uvicorn backend:app --reload`\n"
    "and make sure it's accessible at http://127.0.0.1:8000"
)
