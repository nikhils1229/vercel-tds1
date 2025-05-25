from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

with open("marks.json") as f:
    marks_list = json.load(f)
marks_data = {entry["name"]: entry["marks"] for entry in marks_list}

@app.get("/api")
def get_marks(name: List[str] = Query(None)):
    if name:
        return {"marks": [marks_data.get(n, None) for n in name]}
    return {"marks": list(marks_data.values())}
