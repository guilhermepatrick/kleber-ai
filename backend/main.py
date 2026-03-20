import tempfile
import os
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.transcribe_agent import transcribe

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/transcribe")
async def transcribe_endpoint(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    transcription, txt_path = transcribe(tmp_path, file.filename)
    os.remove(tmp_path)
    return {"transcription": transcription, "txt_path": txt_path}
