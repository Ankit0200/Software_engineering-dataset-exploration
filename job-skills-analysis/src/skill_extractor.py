"""Small utilities to extract skills from job_postings rows.

This is intentionally small: it provides a helper to parse a 'job_skills' field
that may contain a Python-list-like string (as used in the notebook).
"""
import ast
from typing import List


def parse_job_skills(skills_field) -> List[str]:
    """Return a list of skill strings from a job_skills field.

    If the field is already a list, return it. If it's a string that looks like
    a Python list (e.g. "['python','pandas']"), safely literal_eval it. If
    missing/NaN, return an empty list.
    """
    if skills_field is None:
        return []
    if isinstance(skills_field, list):
        return [s.strip().lower() for s in skills_field if s]
    try:
        parsed = ast.literal_eval(skills_field)
        if isinstance(parsed, list):
            return [str(s).strip().lower() for s in parsed]
    except Exception:
        pass
    # fallback: try to split comma-separated string
    try:
        return [s.strip().lower() for s in str(skills_field).split(',') if s.strip()]
    except Exception:
        return []
