from fastapi import FastAPI, Query, Response
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()

# Enable CORS for all origins and GET requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks from marks.json (should be a list of dicts with "name" and "marks")
with open("marks.json") as f:
    marks_list = json.load(f)
marks_data = {entry["name"]: entry["marks"] for entry in marks_list}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    return {"marks": [marks_data.get(n, None) for n in name]}
