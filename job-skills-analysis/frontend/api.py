
from typing import List, Optional

from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
import pandas as pd
from urllib.parse import unquote_plus
from pathlib import Path
import os

app = FastAPI(title="Roles API", version="0.1")

# Resolve the CSV path relative to the repository `data/` folder.
repo_root = Path(__file__).resolve().parents[1]
csv_path = os.environ.get("SKILLS_CSV") or repo_root / "data" / "skills_matrix_by_role.csv"
if not Path(csv_path).exists():
    raise FileNotFoundError(f"Skills CSV not found at {csv_path}. Make sure the file exists under {repo_root}/data or set SKILLS_CSV env var.")
skills_df = pd.read_csv(csv_path, index_col=0)
# Normalize index: remove surrounding whitespace
if hasattr(skills_df.index, "str"):
    skills_df.index = skills_df.index.str.strip()

# Prepare a lowercase lookup map for case-insensitive and encoded lookups
index_lookup = {idx.strip().lower(): idx for idx in skills_df.index}


class RolesRequest(BaseModel):
	roles: List[str]


@app.get("/", summary="Health check")
def read_root():
	return {"status": "ok", "msg": "Roles API is running"}

@app.get("/skills/{role}")
def get_skills_for_role(role: str, top_k: int = 10):
    # Decode URL-encoded values and plus-signs, make lookup case-insensitive
    decoded = unquote_plus(role)
    key = decoded.strip().lower()
    if key not in index_lookup:
        raise HTTPException(status_code=404, detail=f"Role not found: {decoded}")

    canonical_role = index_lookup[key]
    data = (
        skills_df.loc[canonical_role]
        .sort_values(ascending=False)
        .head(top_k)
        .to_dict()
    )

    return {"role": canonical_role, "top_skills": data}




if __name__ == "__main__":
	# Optional: run with `python backend.py` if uvicorn is installed in the same env.
	try:
		import uvicorn

		uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)
	except Exception:
		print("uvicorn is not available. Start the app with: python -m uvicorn backend:app --reload")

