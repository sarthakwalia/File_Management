from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from models import FileRecord, SQLModel
from schemas import FileResponseSchema
from database import engine, session
from crud import save_file, list_files, get_file_by_id
from utils import get_file_path, read_file_content
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB
SQLModel.metadata.create_all(engine)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return await save_file(file)


@app.get("/files", response_model=list[FileResponseSchema])
def list_all_files():
    return list_files()


@app.get("/files/{file_id}/download")
def download_file(file_id: int):
    db_file = get_file_by_id(file_id)
    if not db_file:
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(get_file_path(db_file.filename), filename=db_file.filename)


@app.get("/files/{file_id}", response_model=FileResponseSchema)
def get_file_metadata(file_id: int):
    db_file = get_file_by_id(file_id)
    if not db_file:
        raise HTTPException(status_code=404, detail="File not found")

    content = None
    if db_file.filetype in ["text/plain", "application/json"]:
        content = read_file_content(get_file_path(db_file.filename))

    return FileResponseSchema(**db_file.dict(), content=content)
