🚀 Project Overview

This project analyzes software engineering job postings to identify the most in-demand skills for each role. It allows users to interactively explore top skills for roles like Software Engineer, Data Scientist, Backend Engineer, and more, using data visualization.

The project showcases data cleaning, aggregation, and visualization skills using Python, Pandas, and Streamlit, combined with a FastAPI backend to serve the data dynamically.

📊 Key Features

Interactive role selection: Choose a role and instantly see top skills.

Top skills table: Sorted list of most demanded skills with counts.

Bar chart: Visual representation of skill demand.

Heatmap: Intensity view of top skills for quick insights.

Word cloud: Skill prominence displayed in a visually engaging way.

FastAPI backend: Provides real-time skill data for selected roles.

Supports multiple roles: Software Engineer, Data Scientist, DevOps, IoT Engineer, etc.

💻 Tech Stack

Python 3.12 – Data processing and backend logic

Pandas – Data cleaning and manipulation

FastAPI – Backend API to serve skill data

Streamlit – Interactive front-end and visualizations

Matplotlib / Seaborn / WordCloud – Charts, heatmaps, and word clouds

Kaggle dataset – Software engineering job postings

📈 Project Flow

Data Cleaning: Normalize job titles and extract skill lists from raw job postings.

Role Standardization: Predefined roles to avoid duplicate rows.

Skill Counting: Aggregate occurrences of each skill per role.

API Serving: FastAPI endpoint provides top skills for a selected role.

Interactive Frontend: Streamlit app fetches data from API and visualizes it.

⚡ How to Run

Clone the repo:

git clone <repo-url>
cd skills-by-role


Install dependencies:

pip install -r requirements.txt


Start FastAPI backend:

python -m uvicorn backend:app --reload


Run Streamlit app:

streamlit run app.py


Open browser → select a role → explore top skills.
