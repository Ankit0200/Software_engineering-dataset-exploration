"""Build a skills-by-role matrix from a cleaned job postings DataFrame.

This module exposes a single helper that mirrors the notebook logic at a high level.
"""
import pandas as pd
from .skill_extractor import parse_job_skills


def build_skills_matrix(df: pd.DataFrame, predefined_roles: list, skills: list) -> pd.DataFrame:
    """Return a DataFrame indexed by role with counts per skill.

    df must have columns: 'role' and 'job_skills' (or precomputed 'job_skills_list').
    """
    skills_df = pd.DataFrame(0, index=predefined_roles, columns=skills)
    for _, row in df.iterrows():
        role = row.get('role')
        if pd.isna(role):
            continue
        job_skills = row.get('job_skills_list') if 'job_skills_list' in row else parse_job_skills(row.get('job_skills'))
        job_skills = [s.lower() for s in job_skills]
        for skill in skills:
            if any(skill in s for s in job_skills):
                try:
                    skills_df.at[role, skill] += 1
                except Exception:
                    # ignore missing roles/skills
                    pass
    return skills_df
