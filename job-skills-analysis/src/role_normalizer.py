"""Role normalizer utilities.

Provides a small normalize_job_title function used in the notebook to map raw job
titles into a set of canonical roles.
"""

def normalize_job_title(title: str) -> str:
    """Normalize a raw job title string into a canonical role.

    This is a compact, deterministic mapping copied/derived from the notebook.
    """
    if not title or not isinstance(title, str):
        return "Other"
    t = title.lower()
    if 'data scientist' in t:
        return 'Data Scientist'
    if 'data engineer' in t:
        return 'Data Engineer'
    if 'machine learning' in t or 'ml engineer' in t:
        return 'Machine Learning Engineer'
    if 'embedded' in t:
        return 'Embedded Engineer'
    if 'data analyst' in t:
        return 'Data Analyst'
    if 'devops' in t:
        return 'DevOps Engineer'
    if 'iot' in t or 'internet of things' in t:
        return 'IoT Engineer'
    # Software-related roles
    if 'software engineer' in t or 'software developer' in t or 'software development' in t or 'software' in t:
        if 'senior' in t:
            return 'Senior Software Engineer'
        if 'junior' in t:
            return 'Junior Software Engineer'
        if 'intern' in t:
            return 'Software Engineer Intern'
        if 'backend' in t:
            return 'Backend Software Engineer'
        if 'frontend' in t:
            return 'Frontend Software Engineer'
        if 'test' in t or 'qa' in t or 'quality assurance' in t:
            return 'Software Test Engineer'
        if 'architect' in t:
            return 'Software Architect'
        return 'Software Engineer'
    return 'Other'
